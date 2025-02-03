from flask import Flask, request, jsonify

app = Flask(__name__)  # Pastikan ini tidak ada karakter aneh

# Contoh database sederhana
items = {
    "123": {"name": "Bundle Legenda", "price": 500},
    "456": {"name": "Skin Senjata", "price": 300},
}

@app.route('/api', methods=['GET'])
def get_item():
    item_id = request.args.get('item_id')
    if item_id in items:
        return jsonify({"status": "success", "data": items[item_id]})
    else:
        return jsonify({"status": "error", "message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)