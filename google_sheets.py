import gspread
from google.oauth2.service_account import Credentials
from config import SERVICE_ACCOUNT_FILE, SPREADSHEET_ID


def get_gspread_client():
    """
    Возвращает авторизованный клиент Google Sheets (gspread),
    используя учетные данные из сервисного аккаунта JSON-файла.
    """
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    gc = gspread.authorize(creds)
    return gc


def get_worksheet(gc, sheet_name):
    """
    Открывает таблицу по ключу (SPREADSHEET_ID) и возвращает worksheet по названию листа (sheet_name).
    """
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet
