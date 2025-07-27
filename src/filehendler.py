import abc
import json
import os.path
from pprint import pprint


class FileHendler(abc.ABC):
    def init(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abc.abstractmethod
    def get_vacancy(self, **critery):
        pass

    @abc.abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JsonFileHendler(FileHendler):
    def __init(self, filename="./data/vacancies.json"):
        super().init(filename)


    def get_vacancy(self, **critery):
        """Метод получения вакансии по указаным критериям"""
        if not os.path.exists(self._FileHendler__filename):
            return []
        with open(self._FileHendler__filename, "r", encoding="utf-8") as f:
            vacancys= json.load(f)

        if critery:
            filter_vacancy = []
            for vacancte in vacancys.get("items"):
                for key, value in critery.items():
                    if value in vacancte.get(key):
                        print(vacancte)
                        filter_vacancy.append(vacancte)
            return filter_vacancy
        return vacancys

    def delete_vacancy(self, vacancy_id):
        pass
    def add_vacancy(self, vacancy):
        """Метод о сохрании информации"""
        vacancies = self.get_vacancy()
        if vacancy not in vacancies:
            with open(self._FileHendler__filename, 'r+', encoding='utf-8') as file:
                vacancies = json.load(file)
                vacancies.append(vacancy)


if __name__ == "__main__":
    file_hander = JsonFileHendler()
    vacanes = file_hander.get_vacancy()

    def __lt(self, other):
        return self.salary < other.salary

    def gt(self, other):
        return self.salary > other.salary

    def to_dict(self):
        return {
            'title': self.title,
            'firm_com': self.firm_com,
            'salary':self.salary,
            'url':self.url,
            'description': self.description


        }