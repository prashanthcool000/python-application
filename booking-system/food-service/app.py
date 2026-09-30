from flask import Flask, request, jsonify

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Pizza", "price": 250},
    {"id": 2, "name": "Burger", "price": 150},
    {"id": 3, "name": "Biryani", "price": 220}
]

orders = []


@app.route("/")
def home():
    return jsonify({
        "service": "Food Ordering Service",
        "status": "running"
    })


@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(menu)


@app.route("/order", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "order_id": len(orders) + 1,
        "customer": data["customer"],
        "item_id": data["item_id"],
        "quantity": data["quantity"]
    }

    orders.append(order)

    return jsonify({
        "message": "Food order created",
        "order": order
    }), 201


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
