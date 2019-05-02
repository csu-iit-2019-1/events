import sqlite3 as lite
from config import DATABASE_NAME


def buy_event(booking_id):
    with lite.connect(DATABASE_NAME) as con:
        cur = con.cursor()

        t = '''SELECT COUNT(*) from main.BOOKING where Booking_id = ? and Status=?'''
        v = (booking_id,"Забронировано")
        result = cur.execute(t, v).fetchone()[0]

        if result <= 0:
            return False
        task = '''INSERT INTO main.BYUING(Booking_id, Status) VALUES (?,?)'''
        values = (booking_id, "Куплено")

        cur.execute(task, values)
        task1 = '''UPDATE main.BOOKING SET Status = ? WHERE Booking_id = ? AND Status =?'''
        values1 = ("Куплено", booking_id, "Забронировано")

        cur.execute(task1, values1)

        con.commit()
        return True
