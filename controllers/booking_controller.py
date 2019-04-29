from database.insert_booking import insert_booking


def create_booking(event_id, user_id, counts):
    return insert_booking(event_id, user_id, counts)
