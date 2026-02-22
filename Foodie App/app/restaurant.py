from flask import Blueprint, request, jsonify
from app import database as db

restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    if not request.json or "name" not in request.json:
        return jsonify({"error": "Restaurant name required"}), 400

    restaurant = {
        "id": db.restaurant_id_counter,
        "name": request.json["name"],
        "category": request.json.get("category", ""),
        "location": request.json.get("location", ""),
        "contact": request.json.get("contact", ""),
        "approved": False,
        "active": True
    }

    db.restaurants[db.restaurant_id_counter] = restaurant
    db.restaurant_id_counter += 1

    return jsonify(restaurant), 201


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in db.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.json
    db.restaurants[rid]["location"] = data.get("location", db.restaurants[rid]["location"])

    return jsonify(db.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in db.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    db.restaurants[rid]["active"] = False
    return jsonify({"message": "Restaurant disabled"}), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in db.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    return jsonify(db.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants", methods=["GET"])
def view_all_restaurants():
    return jsonify(db.restaurants), 200