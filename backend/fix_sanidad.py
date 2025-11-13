"""
Script para agregar columna enfermedad_id a la tabla sanidad
"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'pollo_control.db')

print(f"Conectando a: {db_path}")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

try:
    # Verificar columnas existentes
    cur.execute("PRAGMA table_info(sanidad)")
    cols = [c[1] for c in cur.fetchall()]
    
    print(f"Columnas actuales: {', '.join(cols)}")
    
    # Agregar enfermedad_id si no existe
    if 'enfermedad_id' not in cols:
        print("🔧 Agregando columna enfermedad_id...")
        cur.execute("ALTER TABLE sanidad ADD COLUMN enfermedad_id INTEGER")
        conn.commit()
        print("✅ Columna enfermedad_id agregada exitosamente")
    else:
        print("ℹ️  Columna enfermedad_id ya existe")
    
    # Verificar resultado
    cur.execute("PRAGMA table_info(sanidad)")
    cols_final = [c[1] for c in cur.fetchall()]
    print(f"\nColumnas finales: {', '.join(cols_final)}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    conn.rollback()
finally:
    conn.close()
    print("\n✅ Completado")
