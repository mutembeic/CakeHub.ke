from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Category, Cake, Customer, Order, OrderItem
from datetime import datetime

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Cake.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Create tables in the database (remove or modify this line if you are using migrations)
with app.app_context():
    db.create_all()

# Sample route to render a page
@app.route('/')
def home():
    return 'welcome to cake hub'

# Sample route to retrieve and display cake categories
@app.route('/categories')
def get_categories():
    categories = Category.query.all()
    category_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify({'categories': category_list})

# Sample route to create a new cake
@app.route('/cakes', methods=['POST'])
def create_cake():
    data = request.json
    category_id = data.get('category_id')
    category = Category.query.get(category_id)

    if not category:
        return jsonify({'message': 'Category not found'}), 404

    new_cake = Cake(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category_id=category.id,
        image_url=data.get('image_url')
    )

    db.session.add(new_cake)
    db.session.commit()

    return jsonify({'message': 'Cake created successfully'}), 201

# Sample route to retrieve and display all cakes
@app.route('/cakes')
def get_cakes():
    cakes = Cake.query.all()
    cake_list = [{'id': cake.id, 'name': cake.name, 'price': float(cake.price)} for cake in cakes]
    return jsonify({'cakes': cake_list})

# ... Add more routes as needed for your application ...

if __name__ == '__main__':
    app.run(debug=True)


