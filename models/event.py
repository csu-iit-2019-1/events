class Event:
    def __init__(self, event_id, name, cityId, price, description, start_date, end_date, free_space):
        self.event_id = event_id
        self.name = name
        self.cityId = cityId
        self.price = price
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.free_space = free_space
