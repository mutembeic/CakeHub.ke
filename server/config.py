from flask_migrate import Migrate
from flask_restful import Api
from flask import Flask
from models import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os



app = Flask(__name__)
app.config["SECRET_KEY"]="dde75746b06c03788649445cb663e8fcf"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Cake.db'
app.config["JWT_SECRET_KEY"] = "b814b015a3344e69901e9a439712d5cc08bbf"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

migrate=Migrate(app,db)
db.init_app(app)
cors = CORS(app)
api=Api(app)
jwt = JWTManager(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()