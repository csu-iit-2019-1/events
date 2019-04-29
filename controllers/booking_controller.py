from database.select_data import insertBooking


def createBooking(event_name, count_adults, count_children):
    return insertBooking(event_name, count_adults, count_children)
