from database.buy_event import buy_event


def buyout_booking(bookingId):
    buy_event(bookingId)
    return "True"
