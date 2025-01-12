import math

import requests
from config import BASE_URL, YANDEX_OAUTH_TOKEN

headers = {
    "Authorization": f"OAuth {YANDEX_OAUTH_TOKEN}",
    "Content-Type": "application/json",
}


def get_contest_problems(contest_id):
    """
    Получаем список задач, доступных в контесте.
    Возвращает словарь, в котором ключ 'problems' содержит массив с данными по задачам.
    """
    url = f"{BASE_URL}/contests/{contest_id}/problems"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data.get("problems", [])


def get_contest_participants(contest_id):
    """
    Получаем список участников для заданного контеста.
    Возвращает JSON-структуру, которая содержит информацию об участниках.
    """
    url = f"{BASE_URL}/contests/{contest_id}/participants"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def get_all_submissions(contest_id, page_size=100):
    """
    Возвращает все посылки (submissions) для заданного контеста Яндекс.Контест,
    используя пагинацию.

    Сначала делается запрос к API, чтобы узнать общее число посылок (count).
    Затем, если посылок больше, чем page_size, последовательно перебираются страницы,
    пока не будут получены все посылки. В итоге функция возвращает полный список посылок.
    """
    url = f"{BASE_URL}/contests/{contest_id}/submissions"

    params = {
        "page": 1,
        "pageSize": page_size,
    }
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()

    total_count = data.get("count", 0)
    submissions = data.get("submissions", [])

    if total_count <= page_size:
        return submissions

    total_pages = math.ceil(total_count / page_size)
    for page in range(2, total_pages + 1):
        params = {
            "page": page,
            "pageSize": page_size,
        }
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        subs = data.get("submissions", [])
        submissions.extend(subs)

    return submissions
