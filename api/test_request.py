import json

import requests

# get all events

r = requests.post("http://127.0.0.1:5000/events/getEvents",
                  data={"cityId": 5, "startDate": "2019-04-29", "endDate": "2019-04-30"}).content

print(json.loads(r))

r = requests.get('http://127.0.0.1:5000/events/1').content
print(json.loads(r))

r = requests.get('http://127.0.0.1:5000/events/byuing/1').content
print(r)
r = requests.post('http://127.0.0.1:5000/events/booking/1',
                  data={'userId': 456, "countOfPersonsAdults": 48777, "countOfPersonsChildren": 1}).content

print(r)
