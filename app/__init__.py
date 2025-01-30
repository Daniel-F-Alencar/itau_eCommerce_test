from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.models import productORM, userORM  

    from app.routes import product_bp
    from app.auth import auth_bp

    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
