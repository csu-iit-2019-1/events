import sqlite3 as lite

from config import DATABASE_NAME
from controllers.transport_controller import __get_city_by_name


def select_events(city, startDate, endDate, cityId):
    result_events = list()
    with lite.connect(DATABASE_NAME) as con:
        cur = con.cursor()
        task = '''SELECT * FROM main.EVENTS WHERE city = ? AND date(StartDate) BETWEEN date(?) AND date(?) AND date(EndDate) BETWEEN date(?) AND date(?) AND FreeSpace !=0 '''
        values = (city, startDate, endDate, startDate, endDate)

        cur.execute(task, values)
        rows = cur.fetchall()

        for x in rows:
            event_id = x[0]
            name = x[1]
            price = x[3]
            description = x[4]
            start_date = x[5]
            end_date = x[6]
            free_space = x[7]
            result_events.append(
                {"event_id": event_id, "name": name, "cityId": cityId, "price": price, "description": description,
                 "start_date": start_date, "end_date": end_date, "free_space": free_space})
    return result_events


def select_event_by_id(event_id):
    with lite.connect(DATABASE_NAME) as con:
        cur = con.cursor()
        task = '''SELECT * FROM EVENTS WHERE Event_id = ?'''
        cur.execute(task, (event_id,))
        result = cur.fetchone()
        event_id = result[0]
        name = result[1]
        price = result[3]
        description = result[4]
        start_date = result[5]
        end_date = result[6]
        free_space = result[7]
        cityId = __get_city_by_name(result[8])
        event = {"event_id": event_id, "name": name, "cityId": cityId, "price": price, "description": description,
                 "start_date": start_date, "end_date": end_date, "free_space": free_space}
    return event
#
