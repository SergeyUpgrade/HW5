import requests

employer_ids = [9694561, 4219, 78638, 80, 15478, 1057, 2748, 1429999, 4181, 1473866]


def get_employee_data():
    """
    функция для получения данных о компаниях с сайта HH.ru
    :return: список компаний
    """
    employers = []
    for employer_id in employer_ids:
        url_emp = f"https://api.hh.ru/employers/{employer_id}"
        employer_info = requests.get(url_emp).json()
        employers.append(employer_info)

    return employers
