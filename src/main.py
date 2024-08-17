from config import config
from src.DBManager import DBManager
from src.utils import get_employee_data, get_vacancies_data, create_database, save_data_to_database_emp, \
    save_data_to_database_vac


def main():
    params = config()

    data_emp = get_employee_data()
    data_vac = get_vacancies_data()
    create_database('hh', params)
    save_data_to_database_emp(data_emp, 'hh', params)
    save_data_to_database_vac(data_vac, 'hh', params)
    db_manager = DBManager(params)
    print(f"Выберите запрос: \n"
          f"1 - Список всех компаний и количество вакансий у каждой компании\n"
          f"2 - Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
          f"3 - Средняя зарплата по вакансиям\n"
          f"4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
          f"5 - Список всех вакансий, в названии которых содержатся запрашиваемое слово\n"
          f"0 - Выход из программы")


