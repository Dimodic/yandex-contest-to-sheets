from dateutil import parser

from config import CONTEST_IDS
from yandex_contest import (
    get_contest_participants,
    get_contest_problems,
    get_participant_stats
)
from google_sheets import get_gspread_client, get_worksheet
from utils import build_login2row, find_first_successful_runs


def main():
    """
    Основной запуск скрипта:
    1. Инициализируем Google Sheets API-клиент.
    2. По очереди перебираем ID контестов (CONTEST_IDS).
    3. Для каждого контеста получаем:
       - Лист Google Sheets, соответствующий ДЗ (sheet_name = 'ДЗ{index}').
       - Информацию об участниках, задачах и статистике (через Яндекс.Контест API).
    4. Обновляем столбцы со временем первого успешного сабмита для каждой задачи.
    """
    gc = get_gspread_client()

    for index, contest_id in enumerate(CONTEST_IDS, start=1):
        sheet_name = f"ДЗ{index}"
        worksheet = get_worksheet(gc, sheet_name)

        participants = get_contest_participants(contest_id)
        problems = sorted(get_contest_problems(contest_id), key=lambda p: p['alias'])
        problem_aliases = [p["alias"] for p in problems]

        all_values = worksheet.get_all_values()

        header = all_values[0]
        new_header = header + [a for a in problem_aliases if a not in header]
        alias_col = len(header) - len(problem_aliases) if header == new_header else len(header)

        worksheet.update(range_name="A1", values=[new_header])

        logins = build_login2row(all_values)
        num_rows = len(all_values)

        for problem in problems:
            column_values = [[0] for _ in range(1, num_rows)]

            for participant in participants:
                login = participant["login"]

                if login not in logins:
                    continue

                r_i = logins[login]

                stats = get_participant_stats(contest_id, participant["id"])
                runs = stats.get("runs", [])
                first_ok = find_first_successful_runs(runs)

                problem_id = problem["id"]
                if problem_id in first_ok:
                    iso_str = first_ok[problem_id]["submissionTime"]
                    dt = parser.isoparse(iso_str)

                    formula = f"=IF(DATE({dt.year}; {dt.month}; {dt.day}) + TIME({dt.hour}; {dt.minute}; {dt.second}) < L2; 1; 0)"
                    column_values[r_i - 1][0] = formula

            start_row = 2
            end_row = num_rows
            col_letter = chr(65 + alias_col)
            column_range = f"{col_letter}{start_row}:{col_letter}{end_row}"
            alias_col += 1

            worksheet.update(range_name=column_range,
                             values=column_values,
                             value_input_option='USER_ENTERED')
            print(f"Контест {contest_id} -> задача {problem['alias']} обновлена.")

        print(f"{'='*7} Лист '{sheet_name}' обновлён! {'='*7}")


if __name__ == "__main__":
    main()
