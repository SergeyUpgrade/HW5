import psycopg2


class DBManager:
    """Класс, который подключается к БД PostgreSQL."""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='hh', **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании.
        """
        self.cur.execute("""
        SELECT employers.employer_name, COUNT(vacancy.employer_id)
        FROM employers
        JOIN vacancy USING (employer_id)
        GROUP BY employers.employer_name
        ORDER BY COUNT DESC
        """)

        return self.cur.fetchall()
