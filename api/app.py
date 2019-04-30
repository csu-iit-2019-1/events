import json

import requests
import logging
from flask import Flask, request
from controllers.buyout_controller import buyout_booking
from controllers.getting_events_controller import get_events, get_event_by_id
from controllers.booking_controller import create_booking
from config import ADDRESS, PORT

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a',
                    filename="out.log")


@app.route('/events/getEvents', methods=['POST'])
def get_events():
    logging.info("start getting events for period task...")
    try:
        logging.info("start parse request data")
        request_params = request.get_json()
        city = request_params['cityId']
        start_date = request_params['startate']
        end_date = request_params['endDate']
    except requests.exceptions.HTTPError:
        logging.error("invalid request data")
        return "Invalid request data"
    try:
        events = get_events(city, start_date, end_date)
        logging.info("end getting events for period task")
        return json.dumps(events)
    except ValueError:
        logging.error("cannot get events for period")
        return "Cannot get events for period"


@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    logging.info("start getting event by id task...")
    try:
        event = get_event_by_id(event_id)
        logging.info("end getting event by id task")
        return json.dumps(event)
    except ValueError:
        logging.error("event not found")
        return "Event not found"


@app.route('/events/booking/<event_id>', methods=['POST'])
def book_event(event_id):
    logging.info("start booking event task...")
    try:
        logging.info("start parse request data")
        params_data = request.get_json()
        user_id = params_data['userId']
        count_adults = params_data['countOfPersonsAdults']
        counts_children = params_data['countOfPersonsChildren']
    except requests.exceptions.HTTPError:
        logging.error("invalid request data")
        return "Invalid request data"
    try:
        result = str(create_booking(event_id, user_id, int(count_adults) + int(counts_children)))
        logging.info("end booking event by id task")
        return result
    except ValueError:
        logging.error("not enough free space")
        return "Not enough free space"


@app.route('/events/byuing', methods=['POST'])
def buy_event():
    logging.info("start buying booked event task...")
    try:
        logging.info("start parse request data")
        booking_id = request.get_json()['bookingId']
    except requests.exceptions.HTTPError:
        logging.error("invalid request data")
        return "Invalid request data"
    try:
        buyout = buyout_booking(booking_id)
        logging.info("end buying booked task")
        return buyout
    except ValueError:
        logging.error("invalid booking id")
        return "Invalid booking id"


if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
