from flask import Flask, request, jsonify

app = Flask(__name__)

movies = [
    {"id": 1, "name": "Avengers", "available_seats": 100},
    {"id": 2, "name": "Inception", "available_seats": 80},
    {"id": 3, "name": "Interstellar", "available_seats": 120}
]

bookings = []


@app.route("/")
def home():
    return jsonify({
        "service": "Movie Booking Service",
        "status": "running"
    })


@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)


@app.route("/book", methods=["POST"])
def book_movie():
    data = request.json

    movie_id = data["movie_id"]
    seats = data["seats"]

    movie = next(
        (movie for movie in movies if movie["id"] == movie_id),
        None
    )

    if movie is None:
        return jsonify({"error": "Movie not found"}), 404

    if movie["available_seats"] < seats:
        return jsonify({"error": "Not enough seats"}), 400

    movie["available_seats"] -= seats

    booking = {
        "booking_id": len(bookings) + 1,
        "customer": data["customer"],
        "movie_id": movie_id,
        "seats": seats
    }

    bookings.append(booking)

    return jsonify({
        "message": "Movie booked successfully",
        "booking": booking
    }), 201


@app.route("/bookings", methods=["GET"])
def get_bookings():
    return jsonify(bookings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
