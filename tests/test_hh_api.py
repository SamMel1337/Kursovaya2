import unittest
from unittest.mock import patch, MagicMock
from ваш_модуль import hh_API  # замените на актуальный импорт


class TesthhAPI(unittest.TestCase):
    @patch('ваш_модуль.requests.Session')  # Мокаем requests.Session
    def test_get_vacancies_success(self, mock_session_class):
        # Создаем мок сессии и ответа
        mock_session = MagicMock()
        mock_response = MagicMock()

        # Настраиваем мок ответа
        mock_response.json.return_value = {
            "items": [
                {
                    "name": "Python Developer",
                    "employer": {"name": "OpenAI"},
                    "alternate_url": "https://example.com/vacancy/1",
                    "salary": {"from": 100000, "to": 150000},
                    "id": "123"
                },
                {
                    "name": "Senior Python Developer",
                    "employer": {"name": "DeepMind"},
                    "alternate_url": "https://example.com/vacancy/2",
                    "salary": None,
                    "id": "456"
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        # Мокаем создание сессии
        mock_session_class.return_value = mock_session

        api = hh_API()
        vacancies = api.get_vacancies("Python", 1)

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Python Developer")
        self.assertEqual(vacancies[1]["id"], "456")
        self.assertIn("company", vacancies[0])
        self.assertIn("url", vacancies[0])

    @patch('ваш_модуль.requests.Session')
    def test_get_vacancies_api_error(self, mock_session_class):
        # Настраиваем мок с ошибкой HTTP
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        api = hh_API()

        with self.assertRaises(Exception):
            api.get_vacancies("Python", 1)

    @patch('ваш_модуль.requests.Session')
    def test_connect_method(self, mock_session_class):
        # Проверка вызова _connect и установки сессии
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        api = hh_API()
        response = api._connect()

        self.assertIsNotNone(api._connect())
        self.assertEqual(api._connect(), response)
        self.assertIsInstance(api._connect(), type(mock_response))


if __name__ == '__main__':
    unittest.main()