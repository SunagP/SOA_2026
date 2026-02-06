from flask import Flask, jsonify, request

app = Flask(__name__)

products = []
next_id = 1

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SOA Lab 1 Service running",
        "endpoints": [
            "GET /products",
            "POST /products",
            "PUT /products/<id>",
            "DELETE /products/<id>"
        ]
    })

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products", methods=["POST"])
def add_product():
    global next_id
    data = request.get_json()

    product = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(product)
    next_id += 1

    return jsonify(product), 201

@app.route("/products/<int:pid>", methods=["PUT"])
def update_product(pid):
    data = request.get_json()

    for product in products:
        if product["id"] == pid:
            product["name"] = data.get("name", product["name"])
            product["price"] = data.get("price", product["price"])
            return jsonify(product)

    return {"error": "Product not found"}, 404

@app.route("/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    global products
    products = [p for p in products if p["id"] != pid]
    return {"message": f"Product {pid} deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
