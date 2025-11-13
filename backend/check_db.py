"""Script para verificar la base de datos"""
import sys
sys.path.insert(0, '.')
from app import db, Lote, app

with app.app_context():
    lotes = Lote.query.all()
    print(f'\n=== Total de lotes: {len(lotes)} ===\n')
    
    for lote in lotes:
        print(f'Lote ID: {lote.id}')
        print(f'  Nombre: {lote.nombre}')
        print(f'  Fecha inicio: {lote.fecha_inicio}')
        print(f'  Peso inicial: {lote.peso_inicial}')
        print(f'  Días ciclo: {lote.dias_ciclo}')
        print(f'  Cantidad inicial: {lote.cantidad_inicial}')
        print(f'  Cantidad actual: {lote.cantidad_actual}')
        print(f'  Estado: {lote.estado}')
        print(f'  Registros: {len(lote.registros)}')
        print(f'  Costos: {len(lote.costos)}')
        print(f'  Ingresos: {len(lote.ingresos)}')
        print()
