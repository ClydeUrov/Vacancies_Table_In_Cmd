from terminaltables import AsciiTable

import get_vacancies_dict_for_hh
import get_vacancies_dict_for_sj


def get_list(vacancies, line=0):
    head_line = [
        "Язык программирование",
        "Вакансий найдено",
        "Вакансий обработано",
        "Средняя зарплата",
    ]
    salaries = []
    for language in vacancies:
        salaries.append(list(vacancies[language].values()))
        salaries[line].insert(0, language)
        line += 1
    salaries.insert(0, head_line)
    return salaries


def main():
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
    table_instance_hh = AsciiTable(get_list(vacancies_hh), title_for_hh)

    title_for_sj = "SuperJob Moscow"
    vacancies_sj = get_vacancies_dict_for_sj.main(languages)
    table_instance_sj = AsciiTable(get_list(vacancies_sj), title_for_sj)
    print(table_instance_hh.table, "\n", table_instance_sj.table)


if __name__ == "__main__":
    main()
