from flask import Blueprint, request, jsonify
from app import database as db

dish_bp = Blueprint("dish", __name__)

@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    if rid not in db.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.json

    dish = {
        "id": db.dish_id_counter,
        "restaurant_id": rid,
        "name": data["name"],
        "price": data["price"],
        "enabled": True
    }

    db.dishes[db.dish_id_counter] = dish
    db.dish_id_counter += 1

    return jsonify(dish), 201


@dish_bp.route("/api/v1/dishes/<int:id>", methods=["PUT"])
def update_dish(id):
    if id not in db.dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    db.dishes[id]["price"] = request.json.get("price")
    return jsonify(db.dishes[id]), 200


@dish_bp.route("/api/v1/dishes/<int:id>/status", methods=["PUT"])
def change_status(id):
    db.dishes[id]["enabled"] = request.json["enabled"]
    return jsonify({"message": "Dish status updated"}), 200


@dish_bp.route("/api/v1/dishes/<int:id>", methods=["DELETE"])
def delete_dish(id):
    del db.dishes[id]
    return jsonify({"message": "Dish deleted"}), 200