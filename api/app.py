import json
from http.client import HTTPResponse

from flask import Flask, request

from controllers.buyout_controller import buyout_booking
from controllers.getting_events_controller import get_events
from database.select_data import selectEvents, createBooking
from config import ADDRESS, PORT

app = Flask(__name__)


@app.route('/events/getEvents', methods=['POST'])
def getEvents():
    city = request.args.get('cityId')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    return get_events(city, startDate, endDate)


@app.route('events/booking/<event_id>', methods=['GET'])
def bookingEvent(event_id, count_adults, count_children):
    return createBooking(event_id, count_adults, count_children)


@app.route('events/byuing/<booking_id>', methods=['GET'])
def byuingEvent(booking_id):
    return buyout_booking(booking_id)


if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
