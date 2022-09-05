from application.salary import salary_count as sol
from application.db.people import people_count as pep
from date_time import get_currentdate as cd


def main():
    print('Зарплата всех работников состовляет', pep() * sol(), 'рублей')
    print(cd())


if __name__ == '__main__':
    main()
