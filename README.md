# DJANGO_SQL
Простое приложение для исполнения SQL запросов в DJANGO проекте через веб интерфейс. 

Как это работает:
1) Скопируйте файлы в свой проект.
2) Добавьте в settings.py в секцию INSTALLED_APPS

'sql_execute'

3) Добавьте в urls.py строки вида

from sql_execute.views import sql_execute

url(r'^sql/$', sql_execute, name = 'sql_execute'),

4) Пользуйтесь по адресу http(s)://Ваш_проект.ru/sql
