import sys
import logging
from dateutil import parser

from config import CONTEST_IDS, HEADER_ROWS_COUNT, FORMULA_TEMPLATE
from yandex_contest import (
    get_contest_problems,
    get_contest_participants,
    get_all_submissions
)
from google_sheets import (
    get_gspread_client,
    get_worksheet
)
from utils import (
    build_login2row,
    index_to_column_letter,
    parse_homework_headers,
    find_deadline_cell
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)


def main():
    gc = get_gspread_client()
    worksheet = get_worksheet(gc, sheet_name="ДЗ")

    logging.info("Получение всех данных из таблицы")
    all_values = worksheet.get_all_values()

    header = all_values[0]
    homework_names = parse_homework_headers(header)

    logins = build_login2row(all_values)
    num_rows = len(logins)
    logging.info("Количество строк (участников): %d", num_rows)

    for index, contest_id in enumerate(CONTEST_IDS, start=1):
        homework_name = f"ДЗ - {index}"
        deadline_cell = find_deadline_cell(all_values, homework_name)
        logging.info(f"Обработка {homework_name}, ID контеста: {contest_id}")

        problems = sorted(get_contest_problems(contest_id), key=lambda p: p['alias'])
        participants = get_contest_participants(contest_id)
        submissions = get_all_submissions(contest_id)

        logging.info(f"Задачи: {len(problems)},"
                     f"участники: {len(participants)},"
                     f"решения: {len(submissions)}")

        successful_submissions = list(filter(lambda s: s['verdict'] == 'OK', submissions))

        contest_logins = {p["login"]: p for p in participants}
        common_logins = set(logins.keys()) & set(contest_logins.keys())
        filtered_participants = [contest_logins[login] for login in common_logins]
        
        alias_col = homework_names[homework_name]

        for problem in problems:
            column_values = [[0] for _ in range(num_rows)]

            for participant in filtered_participants:
                login = participant["login"]
                participant_id = participant["id"]

                if login not in logins:
                    continue

                participant_successful_submissions = list(
                    filter(
                        lambda s: (
                            s['problemAlias'] == problem['alias']
                            and s['authorId'] == participant_id
                        ),
                        successful_submissions
                    )
                )

                row_index = logins[login]

                if participant_successful_submissions:
                    first_ok_sub = participant_successful_submissions[0]
                    dt = parser.isoparse(first_ok_sub["submissionTime"])

                    formula = FORMULA_TEMPLATE.format(
                        year=dt.year,
                        month=dt.month,
                        day=dt.day,
                        hour=dt.hour,
                        minute=dt.minute,
                        second=dt.second,
                        deadline_cell=deadline_cell
                    )
                    column_values[row_index - 1][0] = formula

            start_row = HEADER_ROWS_COUNT + 1
            end_row = num_rows + HEADER_ROWS_COUNT
            col_letter = index_to_column_letter(alias_col)
            column_range = f"{col_letter}{start_row}:{col_letter}{end_row}"

            worksheet.update(range_name=column_range,
                             values=column_values,
                             value_input_option='USER_ENTERED')
            logging.info(f"Задача {problem['alias']} успешно обновлена")

            alias_col += 1

        logging.info(f"{homework_name} успешно обновлено!")


if __name__ == "__main__":
    main()
