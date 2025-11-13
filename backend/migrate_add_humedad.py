"""
Script de migración: Agregar columna humedad a registros_diarios
"""
import sys
import sqlite3

def migrate():
    print("🔧 Iniciando migración: Agregar columna humedad a registros_diarios...")
    
    import os
    db_path = os.path.join(os.path.dirname(__file__), 'instance', 'pollo_control.db')
    print(f"📁 Ruta de la base de datos: {db_path}")
    
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Verificar si la columna ya existe
        cursor.execute("PRAGMA table_info(registros_diarios)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'humedad' in columns:
            print("ℹ️  La columna 'humedad' ya existe en registros_diarios")
        else:
            # Agregar la columna humedad
            cursor.execute("""
                ALTER TABLE registros_diarios 
                ADD COLUMN humedad REAL
            """)
            conn.commit()
            print("✅ Columna 'humedad' agregada exitosamente a registros_diarios")
        
        conn.close()
        print("✅ Migración completada")
        return True
        
    except Exception as e:
        print(f"❌ Error durante la migración: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = migrate()
    sys.exit(0 if success else 1)
