import os

import requests
from dotenv import load_dotenv


def predict_salary_for_sj(payment_from, payment_to):
    if payment_from != 0 and payment_to != 0:
        return int((payment_from + payment_to) / 2)
    elif payment_from != 0 and payment_to == 0:
        return int(payment_from * 1.2)
    elif payment_from == 0 and payment_to != 0:
        return int(payment_to * 0.8)
    else:
        None


def get_vacancies_dict_sj(languages):
    load_dotenv()
    vacancies_dict = {}
    for language in languages:
        headers = {"X-Api-App-Id": os.environ["SJ_API_ID"]}
        params = {"keyword": language, "count": 1000, "town": "Москва"}
        response = requests.get(
            "https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params
        )
        rub_salaries = []
        for item in response.json()["objects"]:
            rub_salary = predict_salary_for_sj(item["payment_from"], item["payment_to"])
            if rub_salary != None:
                rub_salaries.append(rub_salary)

        average_salary = int(sum(rub_salaries) / len(rub_salaries))
        vacancies_dict[language] = {
            "vacancies_found": response.json()["total"],
            "vacancies_processed": len(rub_salaries),
            "average_salary": average_salary,
        }
    return vacancies_dict
