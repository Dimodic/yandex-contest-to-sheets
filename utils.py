def build_login2row(all_values):
    """
    Функция строит словарь соответствия "логин -> индекс строки" на основании данных листа Google Sheets.
    - all_values: все строки листа (список списков), где all_values[0] — это заголовки.

    Предполагается, что логин участника хранится в столбце C (индекс 2).
    Возвращает словарь: {"login_участника": индекс_строки, ...}
    """
    login2row = {}
    for row_index, row_data in enumerate(all_values):
        if row_data[0].isdigit():
            login_in_sheet = row_data[2].strip()
            login2row[login_in_sheet] = row_index

    return login2row


def parse_homework_headers(header):
    """
    Ищет в заголовке листа ячейки, начинающиеся с «ДЗ - »,
    и возвращает соответствие «название ДЗ -> индекс столбца».
    """
    homework_names = {}
    for col_index, cell_value in enumerate(header):
        if cell_value.startswith("ДЗ - "):
            homework_names[cell_value] = col_index
    return homework_names


def index_to_column_letter(index):
    """
    Преобразует индекс столбца (0-based) в буквенное обозначение (например, 0 -> A, 26 -> AA).
    """
    result = ""
    while index >= 0:
        result = chr(index % 26 + ord('A')) + result
        index = index // 26 - 1
    return result