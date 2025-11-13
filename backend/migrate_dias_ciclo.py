"""
Migración para agregar campo dias_ciclo a tabla lotes existente
"""
import sqlite3
import os

def migrate_add_dias_ciclo():
    """Agrega el campo dias_ciclo a la tabla lotes si no existe"""
    
    # Conectar a la base de datos
    db_path = os.path.join(os.path.dirname(__file__), 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Verificar si la columna ya existe
        cursor.execute("PRAGMA table_info(lotes)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'dias_ciclo' not in columns:
            print("🔧 Agregando campo 'dias_ciclo' a la tabla lotes...")
            cursor.execute("ALTER TABLE lotes ADD COLUMN dias_ciclo INTEGER DEFAULT 42")
            print("✅ Campo 'dias_ciclo' agregado exitosamente")
            
            # Actualizar lotes existentes con valor por defecto
            cursor.execute("UPDATE lotes SET dias_ciclo = 42 WHERE dias_ciclo IS NULL")
            print("✅ Lotes existentes actualizados con dias_ciclo = 42")
            
            conn.commit()
        else:
            print("ℹ️ El campo 'dias_ciclo' ya existe en la tabla lotes")
            
    except Exception as e:
        print(f"❌ Error en migración: {e}")
        conn.rollback()
        raise
    
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_add_dias_ciclo()
    print("🎉 Migración completada")