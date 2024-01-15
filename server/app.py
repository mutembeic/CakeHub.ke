import json
from flask_restful import Resource
from flask import jsonify,session,request
from config import app,db,api, jwt
from models import db, Category, Cake, User, Order, OrderItem

from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import base64
from io import BytesIO
from datetime import datetime, timedelta
blacklisted_tokens = set()


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
    




# Sample route to render a page
@app.route('/')
def home():
    return 'welcome to cake hub'

# # Sample route to retrieve and display cake categories
# @app.route('/categories')
# def get_categories():
#     categories = Category.query.all()
#     category_list = [{'id': category.id, 'name': category.name} for category in categories]
#     return jsonify({'categories': category_list})

# # Sample route to create a new cake
# @app.route('/cakes', methods=['POST'])
# def create_cake():
#     data = request.json
#     category_id = data.get('category_id')
#     category = Category.query.get(category_id)

#     if not category:
#         return jsonify({'message': 'Category not found'}), 404

#     new_cake = Cake(
#         name=data['name'],
#         description=data['description'],
#         price=data['price'],
#         category_id=category.id,
#         image_url=data.get('image_url')
#     )

#     db.session.add(new_cake)
#     db.session.commit()

#     return jsonify({'message': 'Cake created successfully'}), 201

# # Sample route to retrieve and display all cakes
# @app.route('/cakes')
# def get_cakes():
#     cakes = Cake.query.all()
#     cake_list = [{'id': cake.id, 'name': cake.name, 'price': float(cake.price)} for cake in cakes]
#     return jsonify({'cakes': cake_list})

# # ... Add more routes as needed for your application ...

if __name__ == '__main__':
    app.run(debug=True)


