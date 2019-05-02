import json

import requests

# get all events
request = requests.post("http://127.0.0.1:5000/events/getEvents",
                        data=json.dumps({"cityId": 6437, "startDate": "2019-04-29", "endDate": "2019-04-30"})).content

print(json.loads(request))
#
request = requests.get('http://127.0.0.1:5000/events/1').content
print(json.loads(request))
#
request = requests.post('http://127.0.0.1:5000/events/buying', json.dumps({"BookingId": 2})).content
print(request)
r = requests.post('http://127.0.0.1:5000/events/booking',
                  data=json.dumps(
                      {'userId': 456, "eventId": 5, "countOfPersonsAdults": 4, "countOfPersonsChildren": 1})).content

print(json.loads(r))
