import json

import requests
from flask import Flask, request
from controllers.buyout_controller import buyout_booking
from controllers.getting_events_controller import get_events, get_event_by_id
from controllers.booking_controller import create_booking
from config import ADDRESS, PORT

app = Flask(__name__)


@app.route('/events/getEvents', methods=['POST'])
def get_events():
    try:
        request_params = request.get_json()
        city = request_params['cityId']
        start_date = request_params['startate']
        end_date = request_params['endDate']
    except requests.exceptions.HTTPError:
        return "Invalid request data"
    try:
        return json.dumps(get_events(city, start_date, end_date))
    except ValueError:
        return "Cannot get events for period"


@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    try:
        return json.dumps(get_event_by_id(event_id))
    except ValueError:
        return "Event not found"


@app.route('/events/booking/<event_id>', methods=['POST'])
def book_event(event_id):
    try:
        params_data = request.get_json()
        user_id = params_data['userId']
        count_adults = params_data['countOfPersonsAdults']
        counts_children = params_data['countOfPersonsChildren']
    except requests.exceptions.HTTPError:
        return "Invalid request data"
    try:
        result = str(create_booking(event_id, user_id, int(count_adults) + int(counts_children)))
        return result
    except ValueError:
        return "Not enough free space"


@app.route('/events/byuing', methods=['POST'])
def buy_event():
    try:
        booking_id = request.get_json()[0]
    except requests.exceptions.HTTPError:
        return "Invalid request data"
    try:
        return buyout_booking(booking_id)
    except ValueError:
        return "Invalid booking id"


if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
