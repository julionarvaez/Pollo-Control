import os
from datetime import timedelta

class Config:
    """Configuración base de la aplicación"""
    
    # Configuración general
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-super-secreta-cambiar-en-produccion-2025'
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    
    # Base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pollo_control.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # True para ver queries SQL
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    
    # CORS
    CORS_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000', 'http://localhost:5500', '*']
    
    # Archivos
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max
    
    # Exportación
    EXPORT_FOLDER = 'exports'
    BACKUP_FOLDER = 'backups'
    
    # Configuración de la granja
    MONEDA = 'COP'
    IDIOMA = 'es'
    
    # Objetivos y alertas
    FCR_OBJETIVO = 1.8
    MORTALIDAD_MAXIMA = 5.0
    ADG_MINIMO = 50.0

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    # En producción usar PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/pollo_control'

class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_pollo_control.db'

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Obtiene la configuración según el entorno"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])