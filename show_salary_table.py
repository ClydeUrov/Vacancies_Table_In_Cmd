import os
#from terminaltables import AsciiTable
from dotenv import load_dotenv
import get_vacancies_dict_for_hh
import get_vacancies_dict_for_sj


def get_salaries(vacancies, line=1):
    head_line = [
        "Язык программирование",
        "Вакансий найдено",
        "Вакансий обработано",
        "Средняя зарплата",
    ]
    salaries = [head_line]
    for language in vacancies:
        salaries.append(list(vacancies[language].values()))
        salaries[line].insert(0, language)
        line += 1
    return salaries


def main():
    load_dotenv()
    api_id = os.environ["SJ_API_ID"]
    languages = [
        "js",
        "java",
        "python",
        "ruby",
        "php",
        "c++",
        "c#",
        "c",
        "go",
        "1c",
    ]

    title_for_hh = "HeadHunter Moscow"
    vacancies_hh = get_vacancies_dict_for_hh.get_vacancies_hh(languages)
    table_instance_hh = AsciiTable(get_salaries(vacancies_hh), title_for_hh)

    title_for_sj = "SuperJob Moscow"
    vacancies_sj = get_vacancies_dict_for_sj.get_vacancies_sj(languages, api_id)
    table_instance_sj = AsciiTable(get_salaries(vacancies_sj), title_for_sj)
    print(table_instance_hh.table, "\n", table_instance_sj.table)


if __name__ == "__main__":
    main()
