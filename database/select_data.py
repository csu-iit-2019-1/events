import sqlite3 as lite
from config import DATABASE_NAME
from models.event import Event

con = lite.connect(DATABASE_NAME)


def select_events(cityId, startDate, endDate):
    result_events = list()
    with con:
        cur = con.cursor()
        task = '''SELECT * FROM EVENTS WHERE City_ID = ? AND StartDate = ? AND EndDate = ?'''
        values = (cityId, startDate, endDate)

        cur.execute(task, values)
        rows = cur.fetchall()

        for x in rows:
            event_id = x[0]
            name = x[1]
            cityId = x[2]
            price = x[3]
            description = x[4]
            start_date = x[5]
            end_date = x[6]
            free_space = x[7]
            result_events.append(Event(event_id, name, cityId, price, description, start_date, end_date, free_space))
    return result_events


def select_event_by_id(event_id):
    with con:
        cur = con.cursor()
        task = '''SELECT * FROM EVENTS WHERE Event_id = ?'''
        cur.execute(task, (event_id,))
        result = cur.fetchone()
        event_id = result[0]
        name = result[1]
        cityId = result[2]
        price = result[3]
        description = result[4]
        start_date = result[5]
        end_date = result[6]
        free_space = result[7]
        event = Event(event_id, name, cityId, price, description, start_date, end_date, free_space)
    return event


def insertBooking(event_name, count_adults, count_children):
    try:
        with con:
            cur = con.cursor()
            event_id = cur.execute("SELECT Id FROM Events WHERE Name=event_name AND Free_space != 0").fetchall()
            cur.execute("INSERT INTO Booking VALUES(event_id, count_adults, count_children)")
    except:
        return False
