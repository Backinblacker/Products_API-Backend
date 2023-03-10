from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource
from marshmallow import post_load, fields, ValidationError
from dotenv import load_dotenv
from os import environ

load_dotenv()

# Create App instance
app = Flask(__name__)

# Add DB URI from .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

# Registering App w/ Services
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
Migrate(app, db)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    inventory_quantity = db.Column(db.Integer)
    
    def __repr__(self):
        return f'{self.name}{self.description}{self.price}{self.inventory_quantity}'

# Schemas
class ProductSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    name = fields.String(required=True)
    desciption = fields.String(required=True)
    price = fields.String(required=True)
    inventory_quantity = fields.String()
    
    @post_load
    def create_product(self, data, **kwargs):
        return Product(**data)
    
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Resources
class ProductListResource(Resource):
    def get(self):
        all_products = Product.query.all()
        return products_schema.dump(all_products), 200
    
    def post(self):
        form_data = request.get_json()
        try:
            new_product = product_schema(form_data)
            db.session.add(new_product)
            db.session.commit()
            return product_schema.dump(new_product), 201
        except ValidationError as err:
            return err.messages, 400
    
class ProductResource(Resource):
    def get(self, product_id):
        pass
    
    def delete(self, product_id):
        pass
    
    def put(self, product_id):
        pass

# Routes
api.add_resource(ProductListResource, '/api/products/')
api.add_resource(ProductListResource, '/api/products/<int:pk>')