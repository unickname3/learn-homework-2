"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {"name": "Иван", "age": 18, "job": "бармен"},
        {"name": "Василий", "age": 45, "job": "таксист"},
        {"name": "Марианна", "age": 23, "job": "ассистент"},
        {"name": "Светлана", "age": 37, "job": "администратор"},
        {"name": "Жорж", "age": 31, "job": "барбер"},
        {"name": "Ленинид", "age": 83, "job": "профессор"},
    ]
    with open("persons.csv", "w", encoding="utf-8", newline="") as out_file:
        fields = list(data[0].keys())
        writer = csv.DictWriter(out_file, fields, delimiter=";")
        writer.writeheader()
        for person in data:
            writer.writerow(person)


if __name__ == "__main__":
    main()
