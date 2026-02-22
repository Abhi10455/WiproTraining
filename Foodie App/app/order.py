from flask import Blueprint, request, jsonify
from app import database as db

order_bp = Blueprint("order", __name__)

@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    order = {
        "id": db.order_id_counter,
        "user_id": request.json["user_id"],
        "restaurant_id": request.json["restaurant_id"],
        "dish": request.json["dish"],
        "status": "Pending"
    }

    db.orders[db.order_id_counter] = order
    db.order_id_counter += 1

    return jsonify(order), 201


@order_bp.route("/api/v1/ratings", methods=["POST"])
def rating():
    rating = {
        "id": db.rating_id_counter,
        "order_id": request.json["order_id"],
        "rating": request.json["rating"],
        "comment": request.json["comment"]
    }

    db.ratings[db.rating_id_counter] = rating
    db.rating_id_counter += 1

    return jsonify(rating), 201


@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def by_restaurant(rid):
    result = [o for o in db.orders.values() if o["restaurant_id"] == rid]
    return jsonify(result), 200


@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def by_user(uid):
    result = [o for o in db.orders.values() if o["user_id"] == uid]
    return jsonify(result), 200