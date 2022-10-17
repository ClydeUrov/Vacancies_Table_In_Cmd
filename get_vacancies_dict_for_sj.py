import os

import requests
from contextlib import suppress

import predict_rub_salary  


def get_vacancies_sj(languages, api_id, count=1000):
    vacancies = {}
    for language in languages:
        headers = {"X-Api-App-Id": api_id}
        params = {"keyword": language, "count": count, "town": "Москва"}
        response = requests.get(
            "https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params
        )
        response.raise_for_status()
        contents = response.json()
        salary_prediction = [
            predict_rub_salary.predict_salary(
                content["payment_from"], content["payment_to"]
            )
            for content in contents["objects"]
        ]
        rub_salaries = [salary for salary in salary_prediction if salary]
        with suppress(ZeroDivisionError):
            average_salary = int(sum(rub_salaries) / len(rub_salaries))
        vacancies[language] = {
            "vacancies_found": contents["total"],
            "vacancies_processed": len(rub_salaries),
            "average_salary": average_salary,
        }
    return vacancies
