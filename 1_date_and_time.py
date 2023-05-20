"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    yesterday = today - timedelta(days=1)
    back_30_days = today - timedelta(days=30)
    print(f"Вчера было {yesterday.strftime('%d %B %Y')}")
    print(f"Сегодня {today.strftime('%d %B %Y')}")
    print(f"30 дней назад было {back_30_days.strftime('%d %B %Y')}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
