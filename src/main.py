import PrettyTable

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

    while True:
        user_input = input('Введите номер запроса\n')
        if user_input == "1":
            companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
            info_in_table = PrettyTable(['Название компании', 'Количество вакансий'])
            for i in companies_and_vacancies_count:
                info_in_table.add_row([i[0], i[1]])
            print(info_in_table)

        elif user_input == "2":
            all_vacancies = db_manager.get_all_vacancies()
            info_in_table = PrettyTable(['Название компании', 'Название вакансий', 'Зарплата', 'Ссылка на вакансию'])
            for i in all_vacancies:
                info_in_table.add_row([i[0], i[1], i[2], i[3]])
            print(info_in_table)

        elif user_input == '3':
            avg_salary = db_manager.get_avg_salary()
            info_in_table = PrettyTable(['Средняя зарплата по вакансиям'])
            for i in avg_salary:
                info_in_table.add_row([i[0]])
            print(info_in_table)



