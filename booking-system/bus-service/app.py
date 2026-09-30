from flask import Flask, request, jsonify

app = Flask(__name__)

buses = [
    {
        "id": 1,
        "bus_name": "Express Travels",
        "from": "Visakhapatnam",
        "to": "Hyderabad",
        "available_seats": 40
    },
    {
        "id": 2,
        "bus_name": "Orange Travels",
        "from": "Vijayawada",
        "to": "Bangalore",
        "available_seats": 35
    },
    {
        "id": 3,
        "bus_name": "Morning Star",
        "from": "Hyderabad",
        "to": "Chennai",
        "available_seats": 50
    }
]

bookings = []


@app.route("/")
def home():
    return jsonify({
        "service": "Bus Booking Service",
        "status": "running"
    })


@app.route("/buses", methods=["GET"])
def get_buses():
    return jsonify(buses)


@app.route("/book", methods=["POST"])
def book_bus():
    data = request.json

    bus_id = data["bus_id"]
    seats = data["seats"]

    bus = next(
        (bus for bus in buses if bus["id"] == bus_id),
        None
    )

    if bus is None:
        return jsonify({"error": "Bus not found"}), 404

    if bus["available_seats"] < seats:
        return jsonify({"error": "Not enough seats"}), 400

    bus["available_seats"] -= seats

    booking = {
        "booking_id": len(bookings) + 1,
        "customer": data["customer"],
        "bus_id": bus_id,
        "seats": seats
    }

    bookings.append(booking)

    return jsonify({
        "message": "Bus booked successfully",
        "booking": booking
    }), 201


@app.route("/bookings", methods=["GET"])
def get_bookings():
    return jsonify(bookings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
