from flask import Blueprint, jsonify
from app import database as db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    db.restaurants[rid]["approved"] = True
    return jsonify({"message": "Approved"}), 200


@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    db.restaurants[rid]["active"] = False
    return jsonify({"message": "Disabled"}), 200


@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def feedback():
    return jsonify(list(db.ratings.values())), 200


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def orders():
    return jsonify(list(db.orders.values())), 200