import sqlite3 as lite
from config import DATABASE_NAME

con = lite.connect(DATABASE_NAME)

with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Event(Id INT, Name TEXT, City TEXT, Desc TEXT, Start_date TEXT, End_date TEXT, Free_space INT )")
    cur.execute("CREATE TABLE Booking(Id INT, eventId INT, Count_adulds INT, Count_children INT)")
