from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from config import get_config
import infrastructure.database.entities
from infrastructure.database.db import init_db

# from utils.error_handler import register_error_handlers
# from api.auth.auth_routes import auth_ns
# from api.contacts.contacts_routes import contacts_ns

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(get_config())
    
    # Inicializar las tablas de la base de datos
    init_db()
    
    # Enable CORS
    CORS(app)
    
    # Initialize Swagger with Flask-RESTx
    api = Api(
        app, 
        version='1.0', 
        title='Contacts API', 
        description='API para la gestión de usuarios y contactos',
        doc='/swagger'
    )
    
    # Register namespaces
    # api.add_namespace(auth_ns, path='/auth')
    # api.add_namespace(contacts_ns, path='/contacts')
    
    # Register error handlers
    # register_error_handlers(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)