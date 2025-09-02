from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

def find_product(product_id):
    return next((p for p in products if p['id'] == product_id), None)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'category' not in data or 'price' not in data:
        return jsonify({'error': 'Name, category və price tələb olunur'}), 400

    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return jsonify({'error': 'Qiymət düzgün deyil'}), 400

    for product in products:
        if product['name'].lower() == data['name'].lower() and product['category'].lower() == data['category'].lower():
            return jsonify({'error': 'Bu məhsul artıq mövcuddur'}), 400

    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'category': data['category'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = find_product(product_id)
    if not product:
        return jsonify({'error': 'Məhsul tapılmadı'}), 404
    return jsonify(product), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Heç bir data göndərilməyib'}), 400

    product = find_product(product_id)
    if not product:
        return jsonify({'error': 'Məhsul tapılmadı'}), 404

    product['name'] = data.get('name', product['name'])
    product['category'] = data.get('category', product['category'])
    product['price'] = data.get('price', product['price'])

    if not isinstance(product['price'], (int, float)) or product['price'] <= 0:
        return jsonify({'error': 'Qiymət düzgün deyil'}), 400

    return jsonify(product), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    product = find_product(product_id)
    if not product:
        return jsonify({'error': 'Məhsul tapılmadı'}), 404

    products = [p for p in products if p['id'] != product_id]
    return jsonify({'message': 'Məhsul uğurla silindi'}), 200

if __name__ == '__main__':
    app.run(debug=True)
