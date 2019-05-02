import sqlite3 as lite
from config import DATABASE_NAME
from tqdm import tqdm

cities = [
    'Челябинск',
    'Санкт-Петербург',
    'Сочи',
    'Казань',
    'Анапа',
    'Геленджик',
    'Сочи',
    'Краснодар',
    'Ялта',
    'Лондон',
    'Дубай',
    'Париж',
    'Нью-Йорк',
    'Рим',
    'Токио',
    'Стамбул',
    'Сеул',
    'Прага',
    'Майами',
    'Дели',
    'Барселона',
    'Лас-Вегас',
    'Милан',
    'Амстердам',
    'Вена',
    'Лос-Анджелес',
    'Берлин',
    'Венеция',
    'Мадрид',
    'Орландо',
    'Дублин',
    'Флоренция',
    'Афины',
    'Пекин',
    'Будапешт',
    'Мюнхен',
    'Каир',
    'Копенгаген',
    'Иерусалим',
    'Варшава',
    'Краков',
    'Тель-Авив',
    'Брюссель',
    'Ванкувер',
    'Стокгольм',
    'Рио-де-Жанейро',
    'Буэнос-Айрес',
    'Вашингтон'
]
with lite.connect(DATABASE_NAME) as con:
    result = list()
    cur = con.cursor()
    task = '''SELECT * FROM main.EVENTS'''

    cur.execute(task)
    rows = cur.fetchall()
    for i in tqdm(range(2, len(cities))):
        for x in rows:
            event_id = x[0]
            name = x[1]
            price = x[3]
            description = x[4]
            start_date = x[5]
            end_date = x[6]
            free_space = x[7]
            task1 = '''INSERT INTO main.EVENTS(Name, City_ID, Price, Description, StartDate, EndDate, FreeSpace, city) VALUES (?,?,?,?,?,?,?,?)'''
            values = (name, i, price, description, start_date, end_date, free_space, cities[i])
            cur.execute(task1, values)
            con.commit()
