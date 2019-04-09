from flask import Flask, request
from database.select_data import selectEvents, createBooking
from config import ADDRESS, PORT

app = Flask(__name__)


@app.route('/events/getEvents', methods=['POST'])
def getEvents():
    city = request.args.get('city')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')

    return selectEvents(city, startDate, endDate)


@app.route('events/booking/<event_id>', methods=['GET'])
def bookingEvent(event_id, count_adults, count_children):
    return createBooking(event_id, count_adults, count_children)


@app.route('events/byuing/<booking_id>', methods=['GET'])
def byuingEvent(booking_id):
    # посылаем запрос на сервер авторизации
    pass


if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
