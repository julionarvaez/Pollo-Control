"""
Script de debug para probar la creación de registros
"""
import os
import sys
from datetime import datetime, date

# Agregar el directorio actual al path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app, db, RegistroDiario, Lote

def test_create_registro():
    """Prueba crear un registro diario"""
    with app.app_context():
        try:
            # Datos de prueba
            data = {
                'fecha': '2025-10-30',
                'alimento_kg': 100.5,
                'agua_litros': 200.0,
                'mortalidad': 2,
                'causa_mortalidad': 'Enfermedad respiratoria',
                'peso_promedio': 1.5,
                'temperatura_promedio': 25.5,
                'observaciones': 'Test desde debug'
            }
            
            lote_id = 1
            
            print(f"Intentando crear registro para lote {lote_id}")
            print(f"Datos: {data}")
            
            # Verificar si el lote existe
            lote = Lote.query.get(lote_id)
            if not lote:
                print(f"❌ Error: No existe lote con ID {lote_id}")
                return False
            
            print(f"✅ Lote encontrado: {lote.nombre}")
            
            # Convertir fecha
            fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
            print(f"📅 Fecha convertida: {fecha}")
            
            # Verificar si ya existe un registro para esa fecha
            registro_existente = RegistroDiario.query.filter_by(lote_id=lote_id, fecha=fecha).first()
            
            if registro_existente:
                print(f"⚠️  Ya existe un registro para esta fecha: ID {registro_existente.id}")
                return False
            
            # Crear registro
            registro = RegistroDiario(
                lote_id=lote_id,
                fecha=fecha,
                alimento_kg=float(data['alimento_kg']) if data.get('alimento_kg') else None,
                agua_litros=float(data['agua_litros']) if data.get('agua_litros') else None,
                mortalidad=int(data.get('mortalidad', 0)),
                causa_mortalidad=data.get('causa_mortalidad'),
                peso_promedio=float(data['peso_promedio']) if data.get('peso_promedio') else None,
                temperatura_promedio=float(data['temperatura_promedio']) if data.get('temperatura_promedio') else None,
                observaciones=data.get('observaciones')
            )
            
            print("📝 Registro creado en memoria")
            
            db.session.add(registro)
            print("➕ Registro agregado a la sesión")
            
            # Actualizar cantidad actual del lote si hay mortalidad
            if data.get('mortalidad', 0) > 0:
                print(f"☠️  Actualizando mortalidad: -{data['mortalidad']}")
                cantidad_anterior = lote.cantidad_actual or lote.cantidad_inicial
                lote.cantidad_actual = max(0, cantidad_anterior - int(data['mortalidad']))
                lote.updated_at = datetime.utcnow()
                print(f"🔢 Cantidad actualizada: {cantidad_anterior} -> {lote.cantidad_actual}")
            
            db.session.commit()
            print(f"✅ Registro guardado exitosamente con ID: {registro.id}")
            
            return True
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error al crear registro: {str(e)}")
            print(f"Tipo de error: {type(e).__name__}")
            import traceback
            traceback.print_exc()
            return False

def test_db_tables():
    """Verifica que las tablas existan"""
    with app.app_context():
        try:
            # Verificar tablas
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print("📊 Tablas en la base de datos:")
            for table in tables:
                print(f"  - {table}")
            
            # Verificar registros_diarios específicamente
            if 'registros_diarios' in tables:
                columns = inspector.get_columns('registros_diarios')
                print("\n📋 Columnas de registros_diarios:")
                for col in columns:
                    print(f"  - {col['name']}: {col['type']}")
            
            # Contar registros existentes
            count = RegistroDiario.query.count()
            print(f"\n📊 Registros existentes en registros_diarios: {count}")
            
            # Listar lotes disponibles
            lotes = Lote.query.all()
            print(f"\n📦 Lotes disponibles: {len(lotes)}")
            for lote in lotes:
                print(f"  - ID: {lote.id}, Nombre: {lote.nombre}")
            
        except Exception as e:
            print(f"❌ Error verificando DB: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    print("🔧 SCRIPT DE DEBUG - REGISTROS DIARIOS")
    print("=" * 50)
    
    test_db_tables()
    print("\n" + "=" * 50)
    test_create_registro()