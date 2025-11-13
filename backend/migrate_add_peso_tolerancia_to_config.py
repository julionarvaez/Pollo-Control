import sqlite3
import os

DB_PATH = os.environ.get('DATABASE_URL', 'sqlite:///pollo_control.db')

# Extraer ruta de archivo de SQLAlchemy URL si es sqlite:///ruta
if DB_PATH.startswith('sqlite:///'):
    db_file = DB_PATH.replace('sqlite:///', '')
else:
    db_file = 'pollo_control.db'

conn = sqlite3.connect(db_file)
cur = conn.cursor()

try:
    # Revisar columnas existentes en configuracion
    cur.execute("PRAGMA table_info(configuracion);")
    cols = [row[1] for row in cur.fetchall()]

    if 'peso_tolerancia_pct' not in cols:
        print('Agregando columna peso_tolerancia_pct a configuracion...')
        cur.execute("ALTER TABLE configuracion ADD COLUMN peso_tolerancia_pct REAL DEFAULT 5.0;")
        conn.commit()
        print('Columna agregada con valor por defecto 5.0')
    else:
        print('Columna peso_tolerancia_pct ya existe; no se requiere cambio.')
finally:
    conn.close()
