from typing import Dict, Any
class Vacans:
    # Определение слотов для хранения атрибутов объекта
    slots = ('title', 'firm_com', 'salary', 'url', 'description')

    """
    Инициализация объекта вакансии.

    :param title: Название вакансии.
    :param firm_com: Название компании.
    :param salary: Словарь с ключами 'from' и 'to' для диапазона зарплаты.
    :param url: Ссылка на вакансию.
    :param description: Описание вакансии.
    """

    def __init__(self, title, firm_com, salary, url, description):
        self.title = title
        self.firm_com = firm_com
        self.salary = self.salary_valid(salary)
        self.url = url
        self.description = description

    """
    Внутренний метод для проверки и вычисления средней зарплаты из диапазона.

    :param salary: Словарь с ключами 'from' и 'to'.
    :return: Среднее значение зарплаты или 0, если данные отсутствуют.
    """

    def __salary_valid(self, salary: dict) -> Any:
        if salary and salary["from"] is not None and salary["to"] is not None:
            return salary["from"] + (salary["to"] - salary["from"]) / 2
        elif salary and salary["from"] is not None:
            return salary["from"]
        elif salary and salary["to"] is not None:
            return salary["to"]
        else:
            return 0

    """
    Метод для сравнения вакансий по зарплате (меньше).

    :param other: Другой объект Vacans.
    :return: True, если текущая зарплата меньше другой.
    """

    def __lt(self, other):
        return self.salary < other.salary

    """
    Метод для сравнения вакансий по зарплате (больше).

    :param other: Другой объект Vacans.
    :return: True, если текущая зарплата больше другой.
    """

    def gt(self, other):
        return self.salary > other.salary

    """
    Метод для преобразования объекта в словарь.

    :return: Словарь с атрибутами вакансии.
    """

    def to_dict(self):
        return {
            'title': self.title,
            'firm_com': self.firm_com,
            'salary': self.salary,
            'url': self.url,
            'description': self.description
        }
