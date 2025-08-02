import  abc
from typing import AnyStr
from typing import Dict, Any
import requests
from pprint import pprint

class JobAPI(abc.ABC):
    @abc.abstractmethod
    def _connect(self):
        """Метод для подключения к API"""
        pass

    @abc.abstractmethod
    def get_vacancies(self, keyword: str, page:int) -> None:
        """Метод подключения вакансий по ключевому слову"""
        pass

"""
Класс hh_API предназначен для взаимодействия с API сайта HeadHunter (hh.ru)
для получения вакансий по ключевым словам. Наследует от базового класса JobAPI.
Обеспечивает подключение к API, получение вакансий и обработку ответов.
"""
class hh_API(JobAPI):
    # Базовый URL для API вакансий HeadHunter
    __BASE_URL = 'https://api.hh.ru/vacancies'

    """
    Инициализация объекта hh_API.
    """

    def __init__(self):
        self.__session = None

    """
    Метод для установления соединения с API.

    :return: Объект ответа от requests.Session().
    """

    def _connect(self):
        """Метод для подключения к API"""
        self.__session = requests.Session()
        response = self.__session.get(self.__BASE_URL)
        response.raise_for_status()
        return response

    """
    Метод для получения вакансий по ключевому слову.

    :param keyword: Ключевое слово для поиска вакансий.
    :param page: Номер страницы результатов.
    :param per_page: Количество вакансий на странице (по умолчанию 100).

    :return: Список словарей с информацией о вакансиях.
    """

    def get_vacancies(self, keyword: str, page: int, per_page: int = 100) -> Any:
        """Метод для получения по ключевому слову"""
        self._connect()
        params = {"text": keyword, "per_page": per_page, "page": page}

        response = self.__session.get(self.__BASE_URL, params=params)
        response.raise_for_status()
        vacancies = response.json().get("items", [])

        return [
            {
                "name": vacan["name"],
                "company": vacan["employer"]["name"],
                "url": vacan["alternate_url"],
                "salary": vacan["salary"],
                "id": vacan["id"],
            }
            for vacan in vacancies
        ]


if __name__ == "__main__":
        hh_api = hh_API()
        vacancies = hh_api.get_vacancies("Python", 2)
        try:
            for vacan in vacancies:
                salary = vacan["salary"]
                if salary and salary["from"] is not None and salary["to"] is not None:
                    aver_salary = salary["from"] + (salary["to"] - salary["from"]) / 2
                elif salary and salary["from"] is not None:
                    aver_salary = salary["from"]
                elif salary and salary["to"] is not None:
                    aver_salary = salary["to"]
                else:
                    aver_salary = 0

                pprint(
                    f"Название вакансии: {vacan['name']},"
                    f"Работодатель: {vacan['company']}, "
                    f"Ссылка:{vacan['url']} "
                    f"Средняя зарпалата: {vacan['salary']}"
                    f"id: {vacan['id']}"
                )
        except Exception as e:
            print(f"Произошла ошибка: {e}")

