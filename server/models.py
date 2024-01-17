from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)

    category = db.relationship('Category', backref='cakes')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total_amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    order_status = db.Column(db.String(200))
    shipping_address = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    modified_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='orders', foreign_keys=[user_id])
    creator = db.relationship('User', foreign_keys=[created_by], backref='created_orders')
    modifier = db.relationship('User', foreign_keys=[modified_by], backref='modified_orders')

class OrderItem(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    cake_id = db.Column(db.Integer, db.ForeignKey('cake.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    order = db.relationship('Order', backref='order_items', foreign_keys=[order_id])
    cake = db.relationship('Cake', backref='order_items', foreign_keys=[cake_id])


class ShoppingCartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cake_id = db.Column(db.Integer, db.ForeignKey('cake.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    cake = db.relationship('Cake', backref='cart_items')

    def to_dict(self):
        return {
            "id": self.id,
            "cake_id": self.cake_id,
            "cake_name": self.cake.name,
            "price": float(self.cake.price),
            "quantity": self.quantity
        }
    
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Admin(id={self.id}, username={self.username})"
     