from database.select_data import select_events, select_event_by_id


def get_events(cityId, startDate, endDate):
    return select_events(cityId, startDate, endDate)


def get_event_by_id(id):
    return select_event_by_id(id)
