import requests


def predict_salaries_for_hh(vacancies):
    count = sum_salaries = 0
    for num in vacancies:
        number = num["salary"]
        if number and number["currency"] == "RUR":
            count += 1
            if number["to"] and number["from"]:
                sum_salaries += (number["to"] + number["from"]) / 2
            elif number["from"] and not number["to"]:
                sum_salaries += number["from"] * 1.2
            elif not number["from"] and number["to"]:
                sum_salaries += number["to"] * 0.8
        else:
            None
    return int(sum_salaries / count), count


def get_vacancies_dict_hh(languages):
    vacancies_dict = {}
    for language in languages:
        pages_count = page = 0
        pages_number = 1
        items = []
        while pages_count < pages_number:
            params = {
                "text": f"NAME:({language})",
                "area": 1,
                "page": page,
                "per_page": 100,
            }
            response = requests.get("https://api.hh.ru/vacancies/", params=params)
            response.raise_for_status()

            for item in response.json()["items"]:
                items.append(item)
            pages_number = response.json()["found"]
            page += 1
            pages_count = page * 100

        average_salary = predict_salaries_for_hh(items)
        vacancies_dict[language] = {
            "vacancies_found": pages_number,
            "vacancies_processed": average_salary[1],
            "average_salary": average_salary[0],
        }
    return vacancies_dict
