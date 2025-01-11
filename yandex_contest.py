import requests
from config import BASE_URL, YANDEX_OAUTH_TOKEN

headers = {
    "Authorization": f"OAuth {YANDEX_OAUTH_TOKEN}",
    "Content-Type": "application/json",
}


def get_contest_participants(contest_id):
    """
    Получаем список участников для заданного контеста.
    Возвращает JSON-структуру, которая содержит информацию об участниках.
    """
    url = f"{BASE_URL}/contests/{contest_id}/participants"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


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


def get_participant_stats(contest_id, participant_id):
    """
    Получаем статистику (runs, баллы и т.д.) конкретного участника в контесте.
    Возвращает JSON со всеми посылками участника.
    """
    url = f"{BASE_URL}/contests/{contest_id}/participants/{participant_id}/stats"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()
