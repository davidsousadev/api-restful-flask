from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Item

app = Flask(__name__)
CORS(app)  # Permite todas as origens
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/items/<int:item_id>', methods=['GET'])
def get_items_by_id(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@app.route('/items/item/<string:item>', methods=['GET'])
def get_items_by_item(item):
    item = Item.query.filter_by(item=item).first_or_404()
    return jsonify(item.to_dict())

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(item=data['item'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)
    item.item = data.get('item', item.item)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

