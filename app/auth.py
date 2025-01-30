from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
from app import db
from app.models.userORM import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Rota para registrar um novo usuário.
    """
    data = request.get_json()
    name = data.get("name")
    username = data.get("username")
    password = data.get("password")

    if not name or not username or not password:
        return jsonify({"message": "Nome, usuário e senha são obrigatórios"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Usuário já existe"}), 409

    new_user = User(name=name, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Rota para autenticação e geração de token JWT.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=token), 200
    
    return jsonify({"message": "Credenciais inválidas"}), 401
