import abc
import json
import os

class FileHendler(abc.ABC):
    """
    Инициализация класса с указанием имени файла.
    """

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        pass

    @abc.abstractmethod
    def get_vacancy(self, **critery: dict):
        pass

    @abc.abstractmethod
    def delete_vacancy(self, vacancy_id: dict) -> None:
        pass


class JsonFileHendler(FileHendler):
    def __init__(self, filename="./data/vacancies.json"):
        super().__init__(filename)

    def get_vacancy(self, **critery: dict):
        """Метод получения вакансии по указаным критериям"""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r", encoding="utf-8") as f:
            vacancys = json.load(f)

        # Предполагается структура файла — список словарей или словарь с ключом "items"
        items = vacancys.get("items") if isinstance(vacancys, dict) else vacancys

        if critery:
            filter_vacancy = []
            for vacan in items:
                match = True
                for key, value in critery.items():
                    # Проверка наличия ключа и совпадения значения
                    if key not in vacan or value not in str(vacan[key]):
                        match = False
                        break
                if match:
                    filter_vacancy.append(vacan)
            return filter_vacancy
        return items

    def delete_vacancy(self, vacancy_id: dict):
        # Реализация удаления по ID (если нужно)
        pass

    def add_vacancy(self, vacancy: dict):
        """Метод сохранения информации"""
        if not os.path.exists(self.filename):
            vacancies = []
        else:
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    vacancies = json.load(file)
                except json.JSONDecodeError:
                    vacancies = []

        if vacancy not in vacancies:
            vacancies.append(vacancy)
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies, file, ensure_ascii=False, indent=4)