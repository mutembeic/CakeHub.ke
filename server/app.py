import json
from flask_restful import Resource
from flask import jsonify,session,request
from config import app,db,api, jwt
from models import db, Category, Cake, User, Order, OrderItem, ShoppingCartItem, Admin

from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import base64
from io import BytesIO
from datetime import datetime, timedelta
blacklisted_tokens = set()




# Sample route to render a page
@app.route('/')
def home():
    return 'welcome to cake hub'

class SignUp(Resource):
    def post(self):
        data=request.get_json()
        username=data['username']
        email=data['email']
        password=data['password']
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return {"Error":"Username Already Exists"},401
        else:
            new_user=User(username=username,email=email,password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return {"Message": "Sign-Up Successful!!"},201
        
class Login(Resource):
    def post(self):
        data=request.get_json()
        email=data['email']
        password=data['password']
        # find out if ths admin
        # admin = True
        


        user=User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            #TODO Findout if the user is admin
            claims = {"isAdmin":False}
            if email =='admin@example.com':
                claims['isAdmin'] = True
            token = create_access_token(identity=user.id,expires_delta=timedelta(days = 2),additional_claims=claims)
            blacklisted_tokens.clear()
            return {"Message":"Login Successful!!","token":token},200
        else:
            return {"Error":"Invalid Username or Password!!"},401
        
class Logout(Resource):
    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        blacklisted_tokens.add(current_user)
        return {"Message":"Logout Successful!"}
    

class CakeListing(Resource):
    def get(self):
        cakes = Cake.query.all()
        return jsonify({"cakes": [{"id": cake.id, "name": cake.name, "category_id": cake.category_id, "price": float(cake.price)} for cake in cakes]})

class CakeDetails(Resource):
    def get(self, cake_id):
        cake = Cake.query.get(cake_id)
        if cake:
            return jsonify({"cake": {"id": cake.id, "name": cake.name, "category_id": cake.category_id, "price": float(cake.price)}})
        else:
            return jsonify({"error": "Cake not found"}), 404

class CategoryCakeListing(Resource):
    def get(self, category_id):
        category_cakes = Cake.query.filter_by(category_id=category_id).all()
        category_name = Category.query.get(category_id).name if Category.query.get(category_id) else None
        if category_cakes and category_name:
            return jsonify({"category": category_name, "cakes": [{"id": cake.id, "name": cake.name, "category_id": cake.category_id, "price": float(cake.price)} for cake in category_cakes]})
        else:
            return jsonify({"error": "Category not found"}), 404

class ShoppingCart(Resource):
    def get(self):
        cart_items = ShoppingCartItem.query.all()
        cart_data = [item.to_dict() for item in cart_items]
        return jsonify({"cart": cart_data})

class AddToCart(Resource):
    def post(self, cake_id):
        cake = Cake.query.get(cake_id)
        if cake:
            existing_item = ShoppingCartItem.query.filter_by(cake_id=cake.id).first()
            if existing_item:
                existing_item.quantity += 1
            else:
                cart_item = ShoppingCartItem(cake_id=cake.id)
                db.session.add(cart_item)
            db.session.commit()
            return jsonify({"message": "Cake added to the cart successfully"})
        else:
            return jsonify({"error": "Cake not found"}), 404

class RemoveFromCart(Resource):
    def delete(self, cake_id):
        cart_item = ShoppingCartItem.query.filter_by(cake_id=cake_id).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                db.session.delete(cart_item)
            db.session.commit()
            return jsonify({"message": "Cake removed from the cart successfully"})
        else:
            return jsonify({"error": "Cake not found in the cart"}), 404

class Checkout(Resource):
    def get(self):
        # Retrieve items from the shopping cart for review
        cart_items = ShoppingCartItem.query.all()
        cart_data = [item.to_dict() for item in cart_items]
        total_amount = sum(item.cake.price * item.quantity for item in cart_items)
        return jsonify({"cart": cart_data, "total_amount": float(total_amount)})

class PlaceOrder(Resource):
    def post(self):
        # Create a new order based on items in the shopping cart
        cart_items = ShoppingCartItem.query.all()

        if not cart_items:
            return jsonify({"error": "Shopping cart is empty"}), 400

        total_amount = sum(item.cake.price * item.quantity for item in cart_items)

        # Create a new order
        order = Order(total_amount=total_amount)
        db.session.add(order)
        db.session.commit()

        # Add order items to the order
        for item in cart_items:
            order_item = OrderItem(order=order, cake=item.cake, quantity=item.quantity, unit_price=item.cake.price)
            db.session.add(order_item)

        # Clear the shopping cart
        ShoppingCartItem.query.delete()
        db.session.commit()

        return jsonify({"message": "Order placed successfully"})

class OrderHistory(Resource):
    def get(self):
        # Retrieve the customer's order history
        orders = Order.query.all()
        order_data = [{"order_id": order.id, "total_amount": float(order.total_amount)} for order in orders]
        return jsonify({"orders": order_data})

class AdminDashboard(Resource):
    def get(self):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            return jsonify({"message": "Welcome to the Admin Dashboard!"})
        else:
            return jsonify({"error": "Unauthorized"}), 401

class AddCake(Resource):
    def post(self):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if not admin or not check_password_hash(admin.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()

        # Create a new cake
        new_cake = Cake(name=data['name'], category_id=data['category_id'], price=data['price'])
        db.session.add(new_cake)
        db.session.commit()

        return jsonify({"message": "Cake added successfully"})

class EditCake(Resource):
    def put(self, cake_id):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if not admin or not check_password_hash(admin.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()

        # Find the cake by ID
        cake = Cake.query.get(cake_id)

        if cake:
            # Update cake details
            cake.name = data['name']
            cake.category_id = data['category_id']
            cake.price = data['price']
            db.session.commit()
            return jsonify({"message": "Cake updated successfully"})
        else:
            return jsonify({"error": "Cake not found"}), 404
        
class AdminOrders(Resource):
    def get(self):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if not admin or not check_password_hash(admin.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        # Retrieve all orders
        orders = Order.query.all()
        order_data = [{"order_id": order.id, "total_amount": float(order.total_amount)} for order in orders]
        return jsonify({"orders": order_data})

class AdminUser(Resource):
    def get(self):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if not admin or not check_password_hash(admin.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        # Retrieve all customers
        user = user.query.all()
        user_data = [{"user": user.id, "first_name": user.first_name, "last_name": user.last_name} for user in user]
        return jsonify({"user": user_data})

class AdminOrderDetails(Resource):
    def get(self, order_id):
        # Check if the user is an admin (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        admin = Admin.query.filter_by(username=username).first()
        if not admin or not check_password_hash(admin.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        # Retrieve order details
        order = Order.query.get(order_id)

        if order:
            order_data = {
                "order_id": order.id,
                "total_amount": float(order.total_amount),
                # Add more fields as needed
            }
            return jsonify({"order": order_data})
        else:
            return jsonify({"error": "Order not found"}), 404
        
class UserAccountDashboard(Resource):
    def get(self):
        # Check if the user is a customer (simple authentication example)
        username = request.authorization.username
        password = request.authorization.password

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        # Retrieve customer information
        user_data = {
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address": user.address,
            # Add more fields as needed
        }

        # Retrieve order history for the customer
        orders = Order.query.filter_by(user_id=user.id).all()
        order_history = [{"order_id": order.id, "total_amount": float(order.total_amount)} for order in orders]

        return jsonify({"user": user_data, "order_history": order_history})

 
api.add_resource(CakeListing, '/cakes')
api.add_resource(CakeDetails, '/cakes/<int:cake_id>')
api.add_resource(CategoryCakeListing, '/cakes/category/<int:category_id>')
api.add_resource(ShoppingCart, '/cart')
api.add_resource(AddToCart, '/cart/add/<int:cake_id>')
api.add_resource(RemoveFromCart, '/cart/remove/<int:cake_id>')
api.add_resource(Checkout, '/checkout')
api.add_resource(PlaceOrder, '/checkout/place-order')
api.add_resource(OrderHistory, '/orders')
api.add_resource(AdminDashboard, '/admin')
api.add_resource(AddCake, '/admin/cakes/add')
api.add_resource(EditCake, '/admin/cakes/edit/<int:cake_id>')
api.add_resource(AdminOrders, '/admin/orders')
api.add_resource(AdminUser, '/admin/user')
api.add_resource(AdminOrderDetails, '/admin/orders/<int:order_id>')
api.add_resource(UserAccountDashboard, '/account')

if __name__ == '__main__':
    app.run(debug=True)


