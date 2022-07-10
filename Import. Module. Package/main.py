from application.salary import calculate_salary
from application.directory_db.people import get_employees
from datetime import datetime, date, time, timezone

if __name__ == '__main__':
    # Вызов первой функции
    days_worked = int(input('Сколько дней отработали: '))
    calculate_salary(days_worked)
    # Вызов второй функции
    name = input('Имя: ')
    surname = input('Фамилия: ')
    get_employees(name, surname)
    # Вызов функции времени
    print(f'Обращение завершено, дата и время обращения: {datetime.now().strftime("%d.%m.%y %H:%M")} ')
