from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=".env.development")

class Config:
    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'contacts_db')
    DB_USER = os.getenv('DB_USER', 'contacts_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'ContactsPass123!')

    
    # Secret key for JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'SuperSecretKey123!')
    
    # Swagger and Flask-RESTx configuration
    SWAGGER_UI_DOC_EXPANSION = os.getenv('SWAGGER_UI_DOC_EXPANSION', 'list')
    RESTX_MASK_SWAGGER = os.getenv('RESTX_MASK_SWAGGER', False) in ('true', '1', 't')
    
class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    ENV = "testing"

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    

# Dictionary to map the configuration name to the actual configuration object
config_by_env = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

# Function to get the configuration object based on the environment
def get_config():
    # Obtener el entorno desde las variables de entorno, usar 'development' como predeterminado
    env = os.getenv('ENVIRONMENT', 'development')
    
    # Intentar obtener la configuración del diccionario, usar DevelopmentConfig si no existe
    config = config_by_env.get(env, DevelopmentConfig)
    
    if config is None:
        raise ValueError(f"El entorno '{env}' no es válido. Usa 'development', 'testing' o 'production'.")
    
    return config
