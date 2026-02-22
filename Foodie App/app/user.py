from flask import Blueprint, request, jsonify
from app import database as db

user_bp = Blueprint("user", __name__)

@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    user = {
        "id": db.user_id_counter,
        "name": request.json["name"],
        "email": request.json["email"],
        "password": request.json["password"]
    }

    db.users[db.user_id_counter] = user
    db.user_id_counter += 1

    return jsonify(user), 201


@user_bp.route("/api/v1/restaurants/search", methods=["GET"])
def search():
    name = request.args.get("name")
    result = [r for r in db.restaurants.values() if name.lower() in r["name"].lower()]
    return jsonify(result), 200