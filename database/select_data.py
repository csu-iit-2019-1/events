import sqlite3 as lite
from config import DATABASE_NAME

con = lite.connect(DATABASE_NAME)


def selectEvents(city, startDate, endDate):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Events WHERE City=city AND Start_date=startDate AND End_date=endDate")

        rows = cur.fetchall()

    return rows


def createBooking(event_name, count_adults, count_children):
    with con:
        cur = con.cursor()
        event_id = cur.execute("SELECT Id FROM Events WHERE Name=event_name AND Free_space != 0").fetchall()
        cur.execute("INSERT INTO Booking VALUES(event_id, count_adults, count_children)")
    return "Booked!"


