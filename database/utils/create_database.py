import sqlite3 as lite
from config import DATABASE_NAME

conn = lite.connect(DATABASE_NAME)
c = conn.cursor()

# Create table - EVENT
c.execute('''CREATE TABLE EVENTS
             ([Event_id] INTEGER PRIMARY KEY,[Name] text, [City_ID] integer, [Price] double, [Description] TEXT,
              [StartDate] date, [EndDate] date, [FreeSpace] integer)''')

c.execute('''CREATE TABLE BOOKING
             ([Booking_id] INTEGER PRIMARY KEY,[Event_id] integer, [Seats] INTEGER, [Status] text, foreign key(Event_id)
              references EVENTS(event_id))''')

c.execute('''CREATE TABLE BYUING
             ([Byuing_id] INTEGER PRIMARY KEY,[Booking_id] integer,  [Status] text, foreign key(Booking_id) references
              BOOKING(Booking_id))''')

conn.commit()
