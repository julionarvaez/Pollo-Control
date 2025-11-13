"""
Migración: Agregar columnas via_administracion (TEXT) y retiro_dias (INTEGER) a sanidad
"""
import sqlite3, os

DB_CANDIDATES = [
    os.path.join(os.path.dirname(__file__), 'instance', 'pollo_control.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'database.db'),
    os.path.join(os.path.dirname(__file__), 'pollo_control.db'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pollo_control.db'),
]

def path():
    for p in DB_CANDIDATES:
        if os.path.exists(p):
            return p
    return DB_CANDIDATES[0]

def migrate():
    db = path()
    print(f"Usando BD: {db}")
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute("PRAGMA table_info(sanidad)")
        cols = [c[1] for c in cur.fetchall()]
        if 'via_administracion' not in cols:
            print("🔧 Agregando via_administracion...")
            cur.execute("ALTER TABLE sanidad ADD COLUMN via_administracion TEXT")
        else:
            print("ℹ️ via_administracion ya existe")
        cur.execute("PRAGMA table_info(sanidad)")
        cols = [c[1] for c in cur.fetchall()]
        if 'retiro_dias' not in cols:
            print("🔧 Agregando retiro_dias...")
            cur.execute("ALTER TABLE sanidad ADD COLUMN retiro_dias INTEGER")
        else:
            print("ℹ️ retiro_dias ya existe")
        conn.commit()
        print("✅ Migración completada")
    except Exception as e:
        print("❌ Error migración:", e)
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    migrate()
