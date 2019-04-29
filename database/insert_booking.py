import sqlite3 as lite
from config import DATABASE_NAME


def insert_booking(event_id, user_id, counts):
    booking_id = 0
    with lite.connect(DATABASE_NAME) as con:
        cur = con.cursor()
        task = '''INSERT INTO main.BOOKING(Event_id, Seats, user_id, Status) VALUES (?,?,?,?)'''
        values = (event_id, user_id, counts, "Куплено")

        cur.execute(task, values)
        current_seats = cur.execute('''SELECT FreeSpace from main.EVENTS where Event_id = ?''', (event_id,)).fetchone()[
            0]
        task1 = '''UPDATE main.EVENTS SET FreeSpace = ? WHERE Event_id = ?'''
        values1 = (current_seats - counts, event_id)

        cur.execute(task1, values1)

        con.commit()
        task2 = '''SELECT Booking_id FROM main.BOOKING WHERE
         Booking_id = (SELECT MAX(Booking_id)  FROM main.BOOKING);'''
        booking_id = cur.execute(task2).fetchone()[0]
    return booking_id
