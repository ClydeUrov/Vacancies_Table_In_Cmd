from terminaltables import AsciiTable

import get_vacancies_dict_for_hh
import get_vacancies_dict_for_sj


def get_list(vacancies_dict):
    head_line = [
        "Язык программирование",
        "Вакансий найдено",
        "Вакансий обработано",
        "Средняя зарплата",
    ]
    vacancies_list = []
    line = 0
    for language in vacancies_dict:
        vacancies_list.append(list(vacancies_dict[language].values()))
        vacancies_list[line].insert(0, language)
        line += 1
    vacancies_list.insert(0, head_line)
    return vacancies_list


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

    title = "HeadHunter Moscow"
    table_instance = AsciiTable(
        get_list(get_vacancies_dict_for_hh.get_vacancies_dict_hh(languages)), title
    )
    print(table_instance.table)

    title = "SuperJob Moscow"
    table_instance = AsciiTable(
        get_list(get_vacancies_dict_for_sj.get_vacancies_dict_sj(languages)), title
    )
    print(table_instance.table)


if __name__ == "__main__":
    main()
