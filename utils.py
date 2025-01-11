def build_login2row(all_values):
    """
    Функция строит словарь соответствия "логин -> индекс строки" на основании данных листа Google Sheets.
    - all_values: все строки листа (список списков), где all_values[0] — это заголовки.

    Предполагается, что логин участника хранится в столбце B (индекс 1).
    Возвращает словарь: {"login_участника": индекс_строки, ...}
    """
    login2row = {}
    for row_index, row_data in enumerate(all_values):
        if row_index == 0:
            continue

        if len(row_data) > 1:
            login_in_sheet = row_data[1]
            login2row[login_in_sheet] = row_index
    return login2row


def find_first_successful_runs(runs):
    """
    Принимает список словарей `runs`, где каждый элемент содержит информацию о попытке решения (run), включая:
      - problemId: идентификатор задачи,
      - runId: уникальный номер посылки,
      - submissionTime: время отправки решения (строка в формате ISO),
      - verdict: вердикт проверки решения ("OK" — успешное решение, и т.д.).

    Функция возвращает словарь вида:
    {
      problemId_1: {
        "runId": <номер первой успешной посылки>,
        "submissionTime": <строка времени первой успешной посылки>,
        "verdict": "OK"
      },
      problemId_2: {
        ...
      },
      ...
    }

    При этом для каждой задачи учитывается ТОЛЬКО самая ранняя (по submissionTime) посылка со статусом "OK".
    """
    first_ok_by_problem = {}

    for run in runs:
        problem_id = run.get("problemId")
        verdict = run.get("verdict")

        if verdict == "OK" and problem_id not in first_ok_by_problem:
            sub_time_str = run.get("submissionTime")

            first_ok_by_problem[problem_id] = {
                "runId": run["runId"],
                "submissionTime": sub_time_str,
                "verdict": verdict
            }

    return first_ok_by_problem
