# Зарплата по языкам.

Выводит в командной строке табличный вариант средней зарплаты в рублях по популярным языкам программирования. Получает данные с сайтов HeadHunter и SuperJob.

### Как установить 

Для получения информации с сайта SuperJob получаем его **X-Api-App-Id** на сайте [API SuperJob](https://api.superjob.ru/).
Пример:
```
SJ_API_ID='v3.r.137047254.cb72d773d660264300af85789be21a7d76917f3a.126484d92a28e9feb58346b450eb32c6'
```
Вносим его в файл `.env`.
___
### Запуск программы
Для запуска программы и получения значения средней заработной платы по языкам программирования `"JS", "Java", "Python", "Ruby", "PHP", "C++", "C#", "C", "Go", "1C"`, вводим следующим образом:
```
..\Vacancies_Table_In_Cmd>python3 show_salary_table.py
```

Пример вывода:
```
+HeadHunter Moscow------+------------------+---------------------+------------------+
| Язык программирования | Найдено вакансий | Обработано вакансий | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| python                | 1068             | 844                 | 131819           |
| c                     | 785              | 660                 | 100098           |
| c#                    | 1367             | 1080                | 117550           |
| c++                   | 329              | 282                 | 109882           |
| java                  | 1592             | 1233                | 141158           |
| js                    | 3696             | 1559                | 114455           |
| ruby                  | 224              | 166                 | 146186           |
| go                    | 267              | 190                 | 165713           |
| 1с                    | 1954             | 1601                | 98862            |
+-----------------------+------------------+---------------------+------------------+

+SuperJob Moscow--------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| python                | 10               | 7                   | 90714            |
| c                     | 19               | 9                   | 103866           |
| c#                    | 38               | 15                  | 95200            |
| c++                   | 26               | 17                  | 89585            |
| java                  | 36               | 12                  | 101791           |
| js                    | 39               | 20                  | 100400           |
| ruby                  | 3                | 3                   | 166000           |
| go                    | 4                | 3                   | 120833           |
| 1с                    | 113              | 64                  | 116129           |
+-----------------------+------------------+---------------------+------------------+
```

### Цель проекта

Код написан в образовательных целях на онлайн курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).