from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants = {}
dishes = {}
users = {}
orders = {}
ratings = {}

restaurant_id_counter = 1
dish_id_counter = 1
user_id_counter = 1
order_id_counter = 1
rating_id_counter = 1


#RESTAURANT MODULE APIs
@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    global restaurant_id_counter

    data = request.json

    if not data or "name" not in data:
        return jsonify({"error": "Restaurant name required"}), 400

    restaurant = {
        "id": restaurant_id_counter,
        "name": data.get("name"),
        "category": data.get("category", ""),
        "location": data.get("location", ""),
        "contact": data.get("contact", ""),
        "approved": False,
        "active": True
    }

    restaurants[restaurant_id_counter] = restaurant
    restaurant_id_counter += 1

    return jsonify(restaurant), 201


@app.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.json
    restaurants[rid]["name"] = data.get("name", restaurants[rid]["name"])
    restaurants[rid]["location"] = data.get("location", restaurants[rid]["location"])

    return jsonify(restaurants[rid]), 200


@app.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    restaurants[rid]["active"] = False

    return jsonify({"message": "Restaurant disabled"}), 200


@app.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    return jsonify(restaurants[rid]), 200

@app.route("/api/v1/restaurants", methods=["GET"])
def view_restaurants():
    return jsonify(restaurants), 200


#DISH MODULE APIs
@app.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    global dish_id_counter

    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Dish name and price required"}), 400

    dish = {
        "id": dish_id_counter,
        "restaurant_id": rid,
        "name": data.get("name"),
        "price": data.get("price"),
        "enabled": True
    }

    dishes[dish_id_counter] = dish
    dish_id_counter += 1

    return jsonify(dish), 201



@app.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    if dish_id not in dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    data = request.json

    dishes[dish_id]["name"] = data.get("name", dishes[dish_id]["name"])
    dishes[dish_id]["price"] = data.get("price", dishes[dish_id]["price"])

    return jsonify(dishes[dish_id]), 200


@app.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def enable_disable_dish(dish_id):
    if dish_id not in dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    data = request.json

    dishes[dish_id]["enabled"] = data["enabled"]

    return jsonify({"message": "Dish status updated"}), 200


@app.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    if dish_id not in dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    del dishes[dish_id]

    return jsonify({"message": "Dish deleted"}), 200

#ADMIN MODULE APIs
@app.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    restaurants[rid]["approved"] = True

    return jsonify({"message": "Restaurant approved"}), 200


@app.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def admin_disable_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    restaurants[rid]["active"] = False

    return jsonify({"message": "Restaurant disabled by admin"}), 200

@app.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(list(ratings.values())), 200

@app.route("/api/v1/admin/orders", methods=["GET"])
def view_all_orders():
    return jsonify(list(orders.values())), 200


#USER/CUSTOMER MODULE APIs
@app.route("/api/v1/users/register", methods=["POST"])
def user_register():
    global user_id_counter

    data = request.json

    if not data or "email" not in data:
        return jsonify({"error": "Email required"}), 400

    user = {
        "id": user_id_counter,
        "name": data.get("name", ""),
        "email": data.get("email"),
        "password": data.get("password", "")
    }

    users[user_id_counter] = user
    user_id_counter += 1

    return jsonify(user), 201


@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name")

    result = [
        r for r in restaurants.values()
        if name.lower() in r["name"].lower()
    ]

    return jsonify(result), 200

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    global order_id_counter

    data = request.json

    if not data or "user_id" not in data or "restaurant_id" not in data:
        return jsonify({"error": "Missing order details"}), 400

    order = {
        "id": order_id_counter,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dish": data.get("dish", ""),
        "status": "Pending"
    }

    orders[order_id_counter] = order
    order_id_counter += 1

    return jsonify(order), 201



@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    global rating_id_counter

    data = request.json
    rating = {
        "id": rating_id_counter,
        "order_id": data["order_id"],
        "rating": data["rating"],
        "comment": data.get("comment")
    }

    ratings[rating_id_counter] = rating
    rating_id_counter += 1

    return jsonify(rating), 201


#ORDER MODULE APIs
@app.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):
    result = [o for o in orders.values() if o["restaurant_id"] == rid]
    return jsonify(result), 200

@app.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):
    result = [o for o in orders.values() if o["user_id"] == uid]
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)