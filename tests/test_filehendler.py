import unittest
import tempfile
import os
import json

from ваш_модуль import JsonFileHendler  # замените на актуальный импорт


class TestJsonFileHendler(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл для тестов
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.temp_file.name
        self.temp_file.close()

        # Инициализация объекта с этим файлом
        self.handler = JsonFileHendler(filename=self.filename)

    def tearDown(self):
        # Удаляем временный файл после тестов
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_vacancy(self):
        vacancy = {
            "title": "Python Developer",
            "firm_com": "OpenAI",
            "salary": 100000,
            "url": "https://example.com",
            "description": "Develop AI models"
        }
        self.handler.add_vacancy(vacancy)
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertIn(vacancy, data)

    def test_get_vacancy_no_file(self):
        # Удаляем файл, чтобы проверить поведение при его отсутствии
        os.remove(self.filename)
        result = self.handler.get_vacancy()
        self.assertEqual(result, [])

    def test_get_vacancy_with_criteria(self):
        vacancies = [
            {
                "title": "Python Developer",
                "firm_com": "OpenAI",
                "salary": 100000,
                "url": "https://example.com",
                "description": "Develop AI models"
            },
            {
                "title": "Java Developer",
                "firm_com": "Google",
                "salary": 90000,
                "url": "https://example.com",
                "description": "Develop Java apps"
            }
        ]
        # Записываем вакансии в файл
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump({"items": vacancies}, f)

        # Ищем вакансии по критерию
        result = self.handler.get_vacancy(title="Python")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Python Developer")

    def test_add_duplicate_vacancy(self):
        vacancy = {
            "title": "Python Developer",
            "firm_com": "OpenAI",
            "salary": 100000,
            "url": "https://example.com",
            "description": "Develop AI models"
        }
        # Добавляем вакансию дважды
        self.handler.add_vacancy(vacancy)
        self.handler.add_vacancy(vacancy)

        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Вакансия должна быть только один раз
        self.assertEqual(data.count(vacancy), 1)


if __name__ == '__main__':
    unittest.main()