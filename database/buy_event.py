import sqlite3 as lite
from config import DATABASE_NAME


def buy_event(booking_id):
    with lite.connect(DATABASE_NAME) as con:
        cur = con.cursor()
        task = '''INSERT INTO main.BYUING(Booking_id, Status) VALUES (?,?)'''
        values = (booking_id, "Куплено")

        cur.execute(task, values)
        task1 = '''UPDATE main.BOOKING SET Status = ? WHERE Booking_id = ?'''
        values1 = ("Куплено", booking_id)

        cur.execute(task1, values1)

        con.commit()
