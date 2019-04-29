import sqlite3
from config import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
c = conn.cursor()


def create_events():
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = '''INSERT INTO main.EVENTS(Event_id, Name,City_ID,Price,Description,StartDate, EndDate, FreeSpace)
                         VALUES(?,?,?,?,?,?,?,?) '''
    task = (2, 'Одиночный пикет', 5, 5000.0, 'подарок для самого слабого', '2019-04-30', '2019-04-30', 10)
    c.execute(sql, task)
    conn.commit()
    return c.lastrowid


print(create_events())
