import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'pollo_control.db')
DB_PATH = os.path.abspath(DB_PATH)

def column_exists(cursor, table, column):
    cursor.execute(f"PRAGMA table_info({table})")
    cols = [row[1] for row in cursor.fetchall()]
    return column in cols

if __name__ == '__main__':
    print('Aplicando migración: añadir columna enfermedad_id a sanidad...')
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        if not column_exists(cur, 'sanidad', 'enfermedad_id'):
            cur.execute('ALTER TABLE sanidad ADD COLUMN enfermedad_id INTEGER')
            conn.commit()
            print('Columna enfermedad_id agregada correctamente.')
        else:
            print('Columna enfermedad_id ya existe, no se realizaron cambios.')
    except Exception as e:
        print('Error aplicando migración:', e)
    finally:
        conn.close()
