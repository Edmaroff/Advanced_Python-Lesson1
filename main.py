from application import salary
from application.db.people import get_employees
from datetime import datetime as dt
# from freegames import flappy


def main():
    current_date = dt.now().strftime("%d-%m-%Y %H:%M")
    print(f'Текущая дата: {current_date}\n')
    salary.calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()

    # # Игра flappy
    # flappy()
