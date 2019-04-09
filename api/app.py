from flask import Flask, request


app = Flask(__name__)

@app.route('/events/getEvents', methods=['POST'])
def getEvents():
    city = request.args.get('city')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')



@app.route('events/booking/<event_id>', methods=['GET'])
def bookingEvent(event_id):
    pass
@app.route('events/byuing/<booking_id>', methods=['GET'])
def byuingEvent(booking_id):
    pass


