import os
from dotenv import load_dotenv

load_dotenv()

# === Yandex Contest API конфигурация ===
YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN")
BASE_URL = os.getenv("BASE_URL")
CONTEST_IDS = {
    int(pair.split(":")[0]): int(pair.split(":")[1])
    for pair in os.getenv("CONTEST_IDS").split(",")
}

# === Google Sheets API конфигурация ===
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), "..", "service_account.json")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

# === Настройки Приложения ===
HEADER_ROWS_COUNT = int(os.getenv("HEADER_ROWS_COUNT"))
FORMULA_TEMPLATE = os.getenv("FORMULA_TEMPLATE")
