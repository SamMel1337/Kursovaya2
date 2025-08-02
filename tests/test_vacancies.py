import unittest
from ваш_модуль import Vacans  # замените на актуальный импорт

class TestVacans(unittest.TestCase):
    def test_initialization_with_full_salary(self):
        salary = {'from': 50000, 'to': 70000}
        vac = Vacans("Python Developer", "OpenAI", salary, "https://example.com", "Develop AI models")
        self.assertEqual(vac.title, "Python Developer")
        self.assertEqual(vac.firm_com, "OpenAI")
        expected_salary = 50000 + (70000 - 50000) / 2
        self.assertEqual(vac.salary, expected_salary)
        self.assertEqual(vac.url, "https://example.com")
        self.assertEqual(vac.description, "Develop AI models")

    def test_salary_valid_with_only_from(self):
        salary = {'from': 60000, 'to': None}
        vac = Vacans("Java Developer", "Google", salary, "https://example.com", "Develop Java apps")
        self.assertEqual(vac.salary, 60000)

    def test_salary_valid_with_only_to(self):
        salary = {'from': None, 'to': 80000}
        vac = Vacans("C++ Developer", "Microsoft", salary, "https://example.com", "Develop C++ applications")
        self.assertEqual(vac.salary, 80000)

    def test_salary_valid_with_none(self):
        salary = {'from': None, 'to': None}
        vac = Vacans("Manager", "CompanyX", salary, "https://example.com", "Manage projects")
        self.assertEqual(vac.salary, 0)

    def test_lt_method(self):
        vac1 = Vacans("Vac1", "Firm1", {'from': 30000}, "", "")
        vac2 = Vacans("Vac2", "Firm2", {'from': 50000}, "", "")
        self.assertTrue(vac1._Vacans__lt(vac2))
        self.assertFalse(vac2._Vacans__lt(vac1))

    def test_gt_method(self):
        vac1 = Vacans("Vac1", "Firm1", {'from': 30000}, "", "")
        vac2 = Vacans("Vac2", "Firm2", {'from': 50000}, "", "")
        self.assertTrue(vac2.gt(vac1))
        self.assertFalse(vac1.gt(vac2))

    def test_to_dict(self):
        salary = {'from': 40000, 'to': 60000}
        vac = Vacans("DevOps Engineer", "CloudCorp", salary, "https://example.com/vacancy/123", "Manage cloud infrastructure")
        expected_dict = {
            'title': "DevOps Engineer",
            'firm_com': "CloudCorp",
            'salary': 40000 + (60000 - 40000) / 2,
            'url': "https://example.com/vacancy/123",
            'description': "Manage cloud infrastructure"
        }
        self.assertEqual(vac.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()