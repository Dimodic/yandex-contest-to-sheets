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
    python = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "python")
    main_file = os.path.join("src", "main.py")
    if not os.path.exists(main_file):
        print(f"Ошибка: файл {main_file} не найден.")
        return
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

def help_message():
    """Выводит справку по доступным командам"""
    print("""
Доступные команды:
  install  - Установить виртуальное окружение и зависимости
  run      - Запустить проект
  clean    - Удалить виртуальное окружение
  help     - Показать эту справку
  exit     - Выйти из интерактивного режима
    """)

def interactive_mode():
    while True:
        command = input(">>> ").strip()
        if command == "install":
            create_venv()
        elif command == "run":
            run_project()
        elif command == "clean":
            clean_venv()
        elif command == "exit":
            break
        else:
            help_message()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_message()
        interactive_mode()
    else:
        command = sys.argv[1]
        if command == "install":
            create_venv()
        elif command == "run":
            run_project()
        elif command == "clean":
            clean_venv()
        else:
            help_message()
