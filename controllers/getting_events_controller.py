from database.select_data import select_events, select_event_by_id


def get_events_on_period(cityId, startDate, endDate):
    city = __get_city_by_id(cityId)
    return select_events(city, startDate, endDate, cityId)


def get_event_by_id(id):
    return select_event_by_id(id)
