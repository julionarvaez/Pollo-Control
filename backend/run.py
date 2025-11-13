"""
Script de inicio para el Sistema de Control de Pollos de Engorde
"""
import os
import sys
from werkzeug.security import generate_password_hash

# Configurar codificación para Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

# Agregar el directorio actual al path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app, db, Usuario, ensure_database_schema
from config import get_config

def init_database():
    """Inicializa la base de datos y crea tablas"""
    print("🔧 Inicializando base de datos...")
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("✅ Tablas creadas exitosamente")

        # Asegurar migraciones ligeras
        ensure_database_schema()
        
        # Verificar si existe el usuario admin
        admin = Usuario.query.filter_by(username='admin').first()
        
        if not admin:
            # Crear usuario administrador
            admin = Usuario(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                nombre_completo='Administrador',
                email='admin@granja.com',
                rol='admin'
            )
            db.session.add(admin)
            db.session.commit()
            
            print("✅ Usuario administrador creado")
            print("   Usuario: admin")
            print("   Contraseña: admin123")
            print("   ⚠️  CAMBIAR CONTRASEÑA EN PRODUCCIÓN")
        else:
            print("ℹ️  Usuario administrador ya existe")

def create_folders():
    """Crea las carpetas necesarias"""
    folders = ['uploads', 'exports', 'backups', 'database']
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Carpeta '{folder}' creada")

def check_dependencies():
    """Verifica las dependencias instaladas"""
    required = {
        'flask': 'Flask',
        'flask_sqlalchemy': 'Flask-SQLAlchemy',
        'flask_cors': 'Flask-CORS',
        'jwt': 'PyJWT',
        'werkzeug': 'Werkzeug'
    }
    
    optional = {
        'reportlab': 'ReportLab (para exportar PDF)',
        'openpyxl': 'openpyxl (para exportar Excel)',
        'pandas': 'Pandas (para análisis avanzado)'
    }
    
    print("\n📦 Verificando dependencias...")
    
    missing_required = []
    for module, name in required.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - REQUERIDO")
            missing_required.append(name)
    
    missing_optional = []
    for module, name in optional.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ⚠️  {name} - OPCIONAL")
            missing_optional.append(name)
    
    if missing_required:
        print("\n❌ Faltan dependencias requeridas:")
        print("   Ejecutar: pip install", " ".join(missing_required))
        return False
    
    if missing_optional:
        print("\nℹ️  Dependencias opcionales no instaladas:")
        print("   Para instalar: pip install", " ".join(missing_optional))
    
    return True

def show_banner():
    """Muestra el banner de inicio"""
    try:
        # Intentar mostrar banner con emojis
        banner_emoji = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     🐔  SISTEMA DE CONTROL DE POLLOS DE ENGORDE 🐔   ║
    ║                                                      ║
    ║              Versión 1.0 - 2025                      ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
        """
        print(banner_emoji)
    except UnicodeEncodeError:
        # Fallback sin emojis para consolas que no soportan UTF-8
        banner_simple = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║      SISTEMA DE CONTROL DE POLLOS DE ENGORDE         ║
    ║                                                      ║
    ║              Versión 1.0 - 2025                      ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
        """
        print(banner_simple)

def show_info():
    """Muestra información de inicio"""
    config = get_config()
    
    try:
        print("\n📊 INFORMACIÓN DEL SISTEMA")
        print("=" * 60)
        print(f"  🔧 Entorno: {os.environ.get('FLASK_ENV', 'development')}")
        print(f"  🗄️  Base de datos: {config.SQLALCHEMY_DATABASE_URI}")
        print(f"  🌐 Host: {os.environ.get('HOST', '0.0.0.0')}")
        print(f"  🔌 Puerto: {os.environ.get('PORT', '5000')}")
        print(f"  🐞 Debug: {config.DEBUG}")
        print("=" * 60)
    except UnicodeEncodeError:
        print("\nINFORMACION DEL SISTEMA")
        print("=" * 60)
        print(f"  Entorno: {os.environ.get('FLASK_ENV', 'development')}")
        print(f"  Base de datos: {config.SQLALCHEMY_DATABASE_URI}")
        print(f"  Host: {os.environ.get('HOST', '0.0.0.0')}")
        print(f"  Puerto: {os.environ.get('PORT', '5000')}")
        print(f"  Debug: {config.DEBUG}")
        print("=" * 60)
    
    print("\n🚀 INSTRUCCIONES DE USO")
    print("=" * 60)
    print("  1. El servidor backend está corriendo")
    print("  2. Abrir frontend/index.html en el navegador")
    print("  3. O usar un servidor local:")
    print("     cd frontend && python -m http.server 8000")
    print("  4. Acceder a: http://localhost:8000")
    print("\n  📱 Para acceder desde móvil:")
    print("     1. Obtener IP del PC: ipconfig (Windows) o ifconfig (Linux/Mac)")
    print("     2. En el móvil abrir: http://TU_IP:8000")
    print("     3. Actualizar API_URL en frontend con http://TU_IP:5000/api")
    print("=" * 60)
    
    print("\n🔐 CREDENCIALES DE ACCESO")
    print("=" * 60)
    print("  Usuario: admin")
    print("  Contraseña: admin123")
    print("=" * 60)
    
    print("\n⚠️  IMPORTANTE")
    print("=" * 60)
    print("  • Cambiar contraseña en producción")
    print("  • Hacer backups regulares de la base de datos")
    print("  • Archivo BD: database/pollo_control.db")
    print("=" * 60)
    
    print("\n✨ El sistema está listo para usar!\n")

def main():
    """Función principal"""
    show_banner()
    
    # Verificar dependencias
    if not check_dependencies():
        print("\n❌ No se puede iniciar el servidor. Instalar dependencias faltantes.\n")
        sys.exit(1)
    
    # Crear carpetas necesarias
    print("\n📁 Creando carpetas necesarias...")
    create_folders()
    
    # Inicializar base de datos
    init_database()
    
    # Mostrar información
    show_info()
    
    # Iniciar servidor
    try:
        port = int(os.environ.get('PORT', 5000))
        host = os.environ.get('HOST', '0.0.0.0')
        debug = bool(app.config.get('DEBUG', True))
        # Autoreload activado por defecto; desactivar con RELOAD=0
        use_reloader = os.environ.get('RELOAD', '1') != '0'

        print(f"🚀 Iniciando servidor en http://{host}:{port}")
        print("   Presiona CTRL+C para detener\n")
        
        # Usar el método run de Flask directamente
        if hasattr(app, 'run'):
            app.run(
                host=host,
                port=port,
                debug=debug,
                use_reloader=use_reloader,
                threaded=True
            )
        else:
            # Alternativa para Flask 3.0+
            from werkzeug.serving import run_simple
            run_simple(
                hostname=host,
                port=port,
                application=app,
                use_debugger=debug,
                use_reloader=use_reloader,
                threaded=True
            )
    except KeyboardInterrupt:
        print("\n\n👋 Servidor detenido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error al iniciar servidor: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()