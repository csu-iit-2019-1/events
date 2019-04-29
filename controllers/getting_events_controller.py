from database.select_data import selectEvents
def get_events(cityId, startDate, endDate):
    return selectEvents(cityId, startDate, endDate)