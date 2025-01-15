import os
from dotenv import load_dotenv

load_dotenv()

# === Yandex Contest API конфигурация ===
YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN", "<token>")
BASE_URL = os.getenv("BASE_URL", "https://api.contest.yandex.net/api/public/v2")
CONTEST_IDS = os.getenv("CONTEST_IDS", "12345").split(",")

# === Google Sheets API конфигурация ===
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), "..", "service_account.json")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "<spreadsheet-id>")

# === Настройки Приложения ===
HEADER_ROWS_COUNT = int(os.getenv("HEADER_ROWS_COUNT", 2))
FORMULA_TEMPLATE = os.getenv(
    "FORMULA_TEMPLATE",
    "=IF(DATE({year}; {month}; {day}) + TIME({hour}; {minute}; {second}) < {deadline_cell}; 1; 0)"
)
