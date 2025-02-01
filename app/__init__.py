from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.url_map.strict_slashes = False
    
    cors.init_app(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:4200"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.models import productORM, userORM  
    from app.routes import product_bp
    from app.auth import auth_bp

    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
