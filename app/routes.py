from flask import Blueprint, request, jsonify
from app import db
from app.models.productORM import Product 
from flask_jwt_extended import jwt_required
from faker import Faker
from flask_jwt_extended import jwt_required

fake = Faker()
product_bp = Blueprint('products', __name__)
@product_bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@product_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_product_by_id(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    product = Product(
        name=data.get("name"),
        description=data.get("description"),
        price=data.get("price"),
        stock=data.get("stock")
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201


@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200


@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get("name")
    product.description = data.get("description")
    product.price = data.get("price")
    product.stock = data.get("stock")
    db.session.commit()
    return jsonify(product.to_dict()), 200