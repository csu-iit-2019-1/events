import sqlite3 as lite
import sys

con = lite.connect('events.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Event(Id INT, Name TEXT, City TEXT, Desc TEXT, Start_date TEXT, End_date TEXT, Free_space INT )")
    cur.execute("CREATE TABLE Booking(Id INT, eventId INT, Count_adulds INT, Count_children INT)")

