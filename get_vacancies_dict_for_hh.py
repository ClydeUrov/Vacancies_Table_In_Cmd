from contextlib import suppress

import requests

import predict_rub_salary


def predict_salaries(vacancies, sum_salaries=0):
    salary = [
        vacancy["salary"]
        for vacancy in vacancies
        if vacancy["salary"] and vacancy["salary"]["currency"] == "RUR"
    ]
    for payment in salary:
        sum_salaries += predict_rub_salary.predict_salary(
            payment["from"], payment["to"]
        )
    with suppress(ZeroDivisionError):
        return int(sum_salaries / len(salary)), len(salary)


def get_vacancies_hh(languages):
    vacancies = {}
    for language in languages:
        pages_count, page, pages_number, area, per_page = 0, 0, 1, 1, 100
        all_vacancies = []
        while pages_count < pages_number and page < 20:
            params = {
                "text": f"NAME:({language})",
                "area": area,
                "page": page,
                "per_page": per_page,
            }
            response = requests.get("https://api.hh.ru/vacancies/", params=params)
            response.raise_for_status()
            answers = response.json()
            all_vacancies += [vacancies for vacancies in answers["items"]]
            pages_number = answers["found"]
            page += 1
            pages_count = page * per_page
        average_salary, vacancies_processed = predict_salaries(all_vacancies)
        vacancies[language] = {
            "vacancies_found": pages_number,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary,
        }
    return vacancies
