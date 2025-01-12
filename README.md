# Yandex Contest to Google Sheets Integration

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Google Sheets API](https://img.shields.io/badge/API-Google%20Sheets-green)
![Yandex Contest API](https://img.shields.io/badge/API-Yandex%20Contest-orange)

Этот проект интегрирует данные с Yandex.Contest в Google Sheets, позволяя отслеживать прогресс студентов по выполнению домашних заданий.

## Функциональность

- Получение данных о контестах из Yandex.Contest API.
- Автоматическое обновление Google Sheets с результатами студентов.
- Использование формул для проверки времени сдачи задач.

---

## Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-repository.git
cd your-repository
```

### 2. Установка зависимостей
Создайте виртуальное окружение и установите необходимые библиотеки:
```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка проекта

#### a. Google Sheets API
1. Создайте проект в Google Cloud Console.
2. Включите Google Sheets API.
3. Создайте ключ сервисного аккаунта (JSON) и сохраните его в файл `service_account.json`.

#### b. Yandex.Contest API
1. Получите OAuth-токен для доступа к API.
2. Укажите токен в файле `config.py`.

#### c. Настройка таблицы Google Sheets
1. Создайте Google Spreadsheet и укажите его ID в `SPREADSHEET_ID`.
2. Убедитесь, что сервисный аккаунт имеет доступ к таблице.

### 4. Запуск проекта
```bash
python main.py
```

---

## Пример структуры Google Sheets

### Заголовки таблицы:
| ID | Имя | Логин | ДЗ - 1 | ДЗ - 2 | ... |
|----|-----|-------|--------|--------|-----|

- Логины участников используются для сопоставления с данными из Yandex.Contest.
- ДЗ обновляются динамически в зависимости от контестов.

---

## Используемые технологии

- **Python 3.8+**
- **Google Sheets API**
- **Yandex.Contest API**
- **dateutil** для парсинга времени.
- **gspread** для работы с Google Sheets.
- **logging** для мониторинга выполнения.

---

## Примечания
- Обратите внимание на безопасность: не храните токены и учетные данные в публичных репозиториях.
- Для изменения идентификаторов контестов отредактируйте `CONTEST_IDS` в `config.py`.

---

## Контакты
Если у вас есть вопросы или предложения, свяжитесь с [smmaximss@gmail.com](mailto:smmaximss@gmail.com).

