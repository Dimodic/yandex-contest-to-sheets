import os
import sys
import subprocess


def create_venv():
    """Создаёт виртуальное окружение и устанавливает зависимости"""
    print("Создание виртуального окружения...")
    subprocess.call([sys.executable, "-m", "venv", "venv"])
    pip = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "pip")
    print("Установка зависимостей...")
    subprocess.call([pip, "install", "--upgrade", "pip", "-q"])
    subprocess.call([pip, "install", "-r", "requirements.txt", "-q"])
    print("Установка завершена!")


def run_project():
    """Запускает основной файл проекта"""
    print("Запуск проекта...")

    if not os.path.isdir("venv"):
        print("Ошибка: Виртуальное окружение не найдено.")
        print("Пожалуйста, выполните команду 'install' для установки окружения.")
        return

    python = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "python")
    main_file = os.path.join("src", "main.py")
    subprocess.call([python, main_file])


def clean_venv():
    """Удаляет виртуальное окружение"""
    print("Удаление виртуального окружения...")
    if os.path.exists("venv"):
        if os.name == "nt":
            subprocess.call(["rmdir", "/s", "/q", "venv"], shell=True)
        else:
            subprocess.call(["rm", "-rf", "venv"])
        print("Виртуальное окружение удалено.")
    else:
        print("Виртуальное окружение не найдено.")


def setup():
    """Настраивает файл .env через удобный интерфейс"""
    env_file = '.env'
    env_vars = {
        'CONTEST_IDS': {
            'question': 'Введите список ID контестов (через запятую)',
            'default': '12345'
        },
        'YANDEX_OAUTH_TOKEN': {
            'question': 'Введите ваш OAuth токен для Yandex Contest API',
            'default': 'your_yandex_oauth_token'
        },
        'BASE_URL': {
            'question': 'Введите базовый URL API Yandex Contest',
            'default': 'https://api.contest.yandex.net/api/public/v2'
        },
        'SERVICE_ACCOUNT_FILE': {
            'question': 'Введите путь к JSON-файлу учетных данных сервисного аккаунта Google',
            'default': 'service_account.json'
        },
        'SPREADSHEET_ID': {
            'question': 'Введите ID вашей Google Таблицы',
            'default': 'your_google_spreadsheet_id'
        },
        'HEADER_ROWS_COUNT': {
            'question': 'Введите количество строк с заголовками в Google Sheets',
            'default': '2'
        }
    }

    env_content = []
    existing_vars = {}

    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            existing_lines = f.readlines()
        for line in existing_lines:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                existing_vars[key] = value

    for key, info in env_vars.items():
        current_value = existing_vars.get(key, info['default'])
        prompt = f"{info['question']} [{current_value}]: "
        user_input = input(prompt).strip()
        if user_input:
            value = user_input
        else:
            value = current_value
        env_content.append(f"{key}={value}\n")

    with open(env_file, 'w', encoding='utf-8') as f:
        f.writelines(env_content)
    print(f"Конфигурация успешно настроена.")


def help_message():
    """Выводит справку по доступным командам"""
    print("""
Доступные команды:
  run        - Запустить проект
  install    - Установить виртуальное окружение и зависимости
  clean      - Удалить виртуальное окружение
  setup      - Настроить конфигурацию проекта
  help       - Показать эту справку
  exit       - Выйти из интерактивного режима
    """)


def interactive_mode():
    while True:
        command = input(">>> ").strip().lower()
        if command == "install":
            create_venv()
        elif command == "run":
            run_project()
        elif command == "clean":
            clean_venv()
        elif command == "setup":
            setup()
        elif command == "help":
            help_message()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда. Введите 'help' для списка доступных команд.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_message()
        interactive_mode()
    else:
        command = sys.argv[1].lower()
        if command == "install":
            create_venv()
        elif command == "run":
            run_project()
        elif command == "clean":
            clean_venv()
        elif command == "setup":
            setup()
        elif command == "help":
            help_message()
        else:
            help_message()
