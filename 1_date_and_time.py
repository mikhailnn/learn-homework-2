"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, date, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = date.today()
    delta_1 = timedelta(days=1)    
    delta_30 = timedelta(days=30)
    print(dt_now - delta_1, end=', ')
    print(dt_now, end=', ')
    print(dt_now - delta_30)
    
def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """    
    date_list = (date_string.split()[0]).split('/')
    date_list[2] += '20'    
    time_list = date_string.split()[1].split('.')[0].split(':') + [(date_string.split()[1]).split('.')[1]]    
    datetime_list = date_list + time_list    
    datetime_list = [int(i) for i in datetime_list]    
    datetime_object = datetime(datetime_list[2], datetime_list[1], datetime_list[0], datetime_list[3], datetime_list[4], datetime_list[5], datetime_list[6])    
    
    return datetime_object

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
