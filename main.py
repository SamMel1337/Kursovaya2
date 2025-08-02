from src.filehendler import JsonFileHendler
from src.hh_api import hh_API
from pprint import pprint
from src.vacancies import Vacans

if __name__ == "__main__":
    # Предположим, что hh_API требует токен или иные параметры, укажите их при необходимости
    hh_api = hh_API()  # или hh_API(token='your_token')

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    count = int(input("Введите количество вакансий для поиска: "))
    area_input = input("Введите код региона (0 для Москвы): ")

    # Преобразуем в число для сравнения
    try:
        area = int(area_input)
    except ValueError:
        print("Некорректный ввод региона. Устанавливаем регион по умолчанию (Москва).")
        area = 113

    vacanciess = hh_api.get_vacancies(keyword, count, area)

    try:
        vacancies_list = []
        for vacin in vacanciess:
            vacancies_list.append(Vacans(
                vacin['name'],
                vacin['company'],
                vacin['salary'],
                vacin['url'],
                vacin['description']
            ))
            salary = vacin["salary"]
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    # Передача имени файла при создании JsonFileHendler
    file_headler = JsonFileHendler('vacancies.json')  # укажите нужный файл

    for v in vacancies_list:
        file_headler.add_vacancy(v.to_dict())

    while True:
        n = int(input("Введите N кол-во вакансий для получения: "))
        vacancy = file_headler.get_vacancy()
        # Обработка зарплаты "Зарплата не указана"
        sorted_vacan = [vacan for vacan in vacancy if vacan['salary'] == 'Зарплата не указана']
        # Предполагается, что зарплата — числовое значение; если нет — нужно обработать
        sorted_vacan = sorted(sorted_vacan, key=lambda x: float(x.get("salary", 0)), reverse=True)[:n]
        if sorted_vacan:
            for vacancys in sorted_vacan:
                print(
                    f"""
                    Название: {vacancys['name']},
                    Компания: {vacancys['employer']['name']},
                    Зарплата: {vacancys['salary']},
                    Ссылка: {vacancys['alternate_url']},
                    id: {vacancys['id']}
                    """
                )
        else:
            print("Вакансия не найдена")

        keyword_search = input("Введите ключевое слово для поиска вакансий: ")
        vacancy_by_keyword = file_headler.get_vacancy(name=keyword_search)
        if vacancy_by_keyword:
            for vacancys in vacancy_by_keyword:
                print(
                    f"""
                    Название: {vacancys['name']},
                    Компания: {vacancys['employer']['name']},
                    Зарплата: {vacancys['salary']},
                    Ссылка: {vacancys['alternate_url']},
                    id: {vacancys['id']}
                    """
                )
        else:
            print("Вакансия не найдена")

        break  # если хотите выйти после одного прохода, иначе уберите