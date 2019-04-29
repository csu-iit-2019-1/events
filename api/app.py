import json

import requests
from flask import Flask, request
from controllers.buyout_controller import buyout_booking
from controllers.getting_events_controller import get_events, get_event_by_id
from controllers.booking_controller import create_booking
from config import ADDRESS, PORT

app = Flask(__name__)


@app.route('/events/getEvents', methods=['POST'])
def getEvents():
    city = request.form['cityId']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    return json.dumps(get_events(city, startDate, endDate))


@app.route('/events/<event_id>', methods=['GET'])
def getEvent(event_id):
    return json.dumps(get_event_by_id(event_id))


@app.route('/events/booking/<event_id>', methods=['POST'])
def bookingEvent(event_id):
    try:
        user_id = request.form['userId']
        count_adults = request.form['countOfPersonsAdults']
        counts_children = request.form['countOfPersonsChildren']
        return str(create_booking(event_id, user_id, int(count_adults) + int(counts_children)))
    except requests.RequestException:
        return "Invalid Data - no such free seats"



@app.route('/events/byuing/<booking_id>', methods=['GET'])
def byuingEvent(booking_id):
    return buyout_booking(booking_id)

if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
