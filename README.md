# Yandex Contest to Google Sheets Integration

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Google Sheets API](https://img.shields.io/badge/API-Google%20Sheets-green)](https://developers.google.com/sheets/api)
[![Yandex Contest API](https://img.shields.io/badge/API-Yandex%20Contest-orange)](https://api.contest.yandex.net/api/public/swagger-ui.html)

Этот проект позволяет интегрировать результаты контестов из Yandex.Contest в Google Sheets, чтобы автоматизировать процесс отслеживания успеваемости студентов.

## Содержание
- [Функциональность](#функциональность)
- [Установка](#установка)
  - [Клонирование репозитория](#1-клонирование-репозитория)
  - [Установка зависимостей](#2-установка-зависимостей)
  - [Настройка проекта](#3-настройка-проекта)
  - [Запуск проекта](#4-запуск-проекта)
- [Пример структуры Google Sheets](#пример-структуры-google-sheets)
- [Используемые технологии](#используемые-технологии)
- [Примечания](#примечания)
- [Контакты](#контакты)

## Функциональность

- Получение данных о контестах из Yandex.Contest API.
- Автоматическое обновление Google Sheets с результатами студентов.
- Использование формул для проверки времени сдачи задач.

## Установка

<details>
<summary><b>1. Клонирование репозитория</b></summary>

```bash
git clone [https://github.com/your-repository.git](https://github.com/Dimodic/yandex-contest-to-sheets)
cd yandex-contest-to-sheets
```

</details>

<details>
<summary><b>2. Установка зависимостей</b></summary>

Создайте виртуальное окружение и установите необходимые библиотеки с помощью `run.py`:

```bash
python run.py install
```

</details>

<details>
<summary><b>3. Настройка проекта</b></summary>

### 3.1. Google Sheets API
1. Перейдите в [Google Cloud Console](https://console.cloud.google.com/).
2. Создайте новый проект или выберите существующий.
3. Включите **Google Sheets API**:
   - Перейдите в раздел **APIs & Services** → **Library**.
   - Найдите **Google Sheets API** и нажмите **Enable**.
4. Создайте учетные данные для сервисного аккаунта:
   - Перейдите в раздел **APIs & Services** → **Credentials**.
   - Нажмите **Create Credentials** → **Service Account**.
   - Заполните форму и нажмите **Create**.
5. Создайте JSON-ключ для сервисного аккаунта:
   - Перейдите в раздел **Keys** учетной записи сервисного аккаунта.
   - Нажмите **Add Key** → **Create New Key** и выберите **JSON**.
   - Сохраните файл `service_account.json` в корневую папку проекта.
6. Поделитесь таблицей Google Sheets с сервисным аккаунтом:
   - Откройте таблицу в Google Sheets.
   - Нажмите **Share** (Поделиться).
   - Введите email-адрес сервисного аккаунта и предоставьте права редактора.

### 3.2. Yandex.Contest API
1. Создайте приложение в Яндекс ID.
2. Укажите свою почту для уведомлений об изменениях API.
3. Выберите права доступа для приложения:
   - `contest:submit` для отправки решений.
   - `contest:manage` для управления контестами и участниками.
4. Получите `client_id` созданного приложения.
5. Получите отладочный токен, следуя инструкциям [Получение OAuth-токена](https://yandex.ru/dev/id/doc/ru/access).
6. Получите токен и укажите его в config.py.

### 3.3. Настройка таблицы Google Sheets
1. Создайте Google Spreadsheet и укажите его ID в `SPREADSHEET_ID`.
2. Убедитесь, что сервисный аккаунт имеет доступ к таблице.

</details>

<details>
<summary><b>4. Запуск проекта</b></summary>

Для запуска проекта используйте команду:

```bash
python run.py run
```

</details>

## Пример структуры Google Sheets

|     |            |             |   ДЗ-1   |        |        |   ДЗ-2   |        |        | ... |
| --- | ---------- | ----------- | -------- | ------ | ------ | -------- | ------ | ------ | --- |
|  №  |    Имя     |    Логин    |     A    |    B   |    C   |    A     |    B   |    C   | ... |
|  1  | Иван Иванов|  ivanov123  |          |        |        |          |        |        | ... |

- Логины участников используются для сопоставления с данными из Yandex.Contest.
- Данные ДЗ обновляются автоматически.

## Используемые технологии

| Технология             | Описание                                | Ссылки                                                                 |
|------------------------|-----------------------------------------|------------------------------------------------------------------------|
| **Python 3.8+**        | Основной язык программирования.         | [Документация Python](https://www.python.org/doc/)                     |
| **Google Sheets API**  | Работа с таблицами Google.              | [Google Sheets API](https://developers.google.com/sheets/api)          |
| **Yandex.Contest API** | Получение данных контестов.             | [Документация Yandex.Contest API](https://yandex.ru/dev/contest/)      |
| **dateutil**           | Парсинг времени.                        | [Python-dateutil](https://dateutil.readthedocs.io/)                    |
| **gspread**            | Работа с Google Sheets.                 | [gspread на GitHub](https://github.com/burnash/gspread)                |
| **logging**            | Логирование выполнения.                 | [Документация logging](https://docs.python.org/3/library/logging.html) |

## Примечания

- Убедитесь, что токены и учетные данные не находятся в публичном доступе.
- Для изменения идентификаторов контестов отредактируйте `CONTEST_IDS` в `config.py`.

## Контакты

Если у вас есть вопросы или предложения, свяжитесь с [smmaximss@gmail.com](mailto:smmaximss@gmail.com).

