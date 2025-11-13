"""
Servicio de cálculos para estadísticas de lotes
"""
from datetime import datetime, date
from typing import Dict, Optional

def calcular_dias_transcurridos(fecha_inicio: date) -> int:
    """Calcula los días desde el inicio del lote"""
    return (datetime.now().date() - fecha_inicio).days

def calcular_fcr(total_alimento_kg: float, ganancia_peso_kg: float) -> float:
    """
    Calcula el Feed Conversion Ratio (FCR)
    FCR = Alimento consumido (kg) / Ganancia de peso (kg)
    
    Valores de referencia:
    - Excelente: < 1.7
    - Muy bueno: 1.7 - 1.8
    - Bueno: 1.8 - 2.0
    - Regular: 2.0 - 2.3
    - Malo: > 2.3
    """
    if ganancia_peso_kg <= 0:
        return 0.0
    return round(total_alimento_kg / ganancia_peso_kg, 2)

def calcular_adg(peso_final_g: float, peso_inicial_g: float, dias: int) -> float:
    """
    Calcula el Average Daily Gain (ADG)
    ADG = (Peso final - Peso inicial) / Días
    
    Valores de referencia (gramos/día):
    - Excelente: > 60
    - Muy bueno: 55 - 60
    - Bueno: 50 - 55
    - Regular: 45 - 50
    - Malo: < 45
    """
    if dias <= 0:
        return 0.0
    return round((peso_final_g - peso_inicial_g) / dias, 2)

def calcular_mortalidad_porcentaje(total_muertas: int, cantidad_inicial: int) -> float:
    """
    Calcula el porcentaje de mortalidad
    
    Valores de referencia:
    - Excelente: < 3%
    - Muy bueno: 3% - 5%
    - Aceptable: 5% - 8%
    - Alto: > 8%
    """
    if cantidad_inicial <= 0:
        return 0.0
    return round((total_muertas / cantidad_inicial) * 100, 2)

def calcular_ganancia_peso_total(peso_actual_g: float, peso_inicial_g: float, 
                                 cantidad_actual: int) -> float:
    """
    Calcula la ganancia total de peso en kg
    """
    ganancia_por_ave_g = peso_actual_g - peso_inicial_g
    ganancia_total_g = ganancia_por_ave_g * cantidad_actual
    return round(ganancia_total_g / 1000, 2)  # Convertir a kg

def calcular_costo_por_kg(total_costos: float, kg_producidos: float) -> float:
    """Calcula el costo por kilogramo producido"""
    if kg_producidos <= 0:
        return 0.0
    return round(total_costos / kg_producidos, 2)

def calcular_costo_por_pollo(total_costos: float, cantidad_inicial: int) -> float:
    """Calcula el costo por pollo"""
    if cantidad_inicial <= 0:
        return 0.0
    return round(total_costos / cantidad_inicial, 2)

def calcular_rentabilidad(ganancia: float, total_costos: float) -> float:
    """
    Calcula el porcentaje de rentabilidad
    Rentabilidad % = (Ganancia / Costos totales) × 100
    
    Valores de referencia:
    - Excelente: > 30%
    - Muy bueno: 25% - 30%
    - Bueno: 20% - 25%
    - Regular: 15% - 20%
    - Bajo: 10% - 15%
    - Malo: < 10%
    """
    if total_costos <= 0:
        return 0.0
    return round((ganancia / total_costos) * 100, 2)

def calcular_uniformidad(pesos: list, peso_promedio: float) -> float:
    """
    Calcula el coeficiente de uniformidad del lote
    CV = (Desviación estándar / Media) × 100
    
    Uniformidad = 100 - CV
    
    Valores de referencia:
    - Excelente: > 85%
    - Buena: 80% - 85%
    - Regular: 75% - 80%
    - Baja: < 75%
    """
    if not pesos or peso_promedio <= 0:
        return 0.0
    
    # Calcular varianza
    varianza = sum((x - peso_promedio) ** 2 for x in pesos) / len(pesos)
    desviacion_std = varianza ** 0.5
    
    # Calcular coeficiente de variación
    cv = (desviacion_std / peso_promedio) * 100
    
    # Uniformidad
    uniformidad = 100 - cv
    return round(max(0, uniformidad), 2)

def calcular_consumo_promedio_diario(total_alimento_kg: float, dias: int) -> float:
    """Calcula el consumo promedio de alimento por día"""
    if dias <= 0:
        return 0.0
    return round(total_alimento_kg / dias, 2)

def calcular_consumo_por_ave(total_alimento_kg: float, cantidad_aves: int) -> float:
    """Calcula el consumo de alimento por ave en gramos"""
    if cantidad_aves <= 0:
        return 0.0
    return round((total_alimento_kg * 1000) / cantidad_aves, 2)

def calcular_agua_por_alimento(total_agua_litros: float, total_alimento_kg: float) -> float:
    """
    Calcula la relación agua/alimento
    
    Valores de referencia:
    - Normal: 1.8 - 2.2 litros por kg de alimento
    """
    if total_alimento_kg <= 0:
        return 0.0
    return round(total_agua_litros / total_alimento_kg, 2)

def proyectar_peso_final(peso_actual: float, dias_transcurridos: int, 
                        dias_objetivo: int = 42) -> float:
    """
    Proyecta el peso final esperado basado en el crecimiento actual
    """
    if dias_transcurridos <= 0:
        return peso_actual
    
    # Calcular ADG actual
    adg_actual = peso_actual / dias_transcurridos
    
    # Proyectar peso al día objetivo
    dias_restantes = dias_objetivo - dias_transcurridos
    if dias_restantes <= 0:
        return peso_actual
    
    peso_proyectado = peso_actual + (adg_actual * dias_restantes)
    return round(peso_proyectado, 2)

def proyectar_fcr_final(fcr_actual: float, dias_transcurridos: int, 
                       dias_objetivo: int = 42) -> float:
    """
    Proyecta el FCR final esperado
    Nota: Esta es una estimación simple, en realidad el FCR tiende a aumentar
    """
    if dias_transcurridos <= 0 or dias_transcurridos >= dias_objetivo:
        return fcr_actual
    
    # El FCR tiende a empeorar (aumentar) hacia el final
    factor_ajuste = 1 + ((dias_objetivo - dias_transcurridos) / dias_objetivo * 0.1)
    fcr_proyectado = fcr_actual * factor_ajuste
    
    return round(fcr_proyectado, 2)

def evaluar_rendimiento(fcr: float, mortalidad_pct: float, adg: float) -> Dict[str, str]:
    """
    Evalúa el rendimiento general del lote
    Retorna un diccionario con las evaluaciones
    """
    evaluacion = {}
    
    # Evaluar FCR
    if fcr < 1.7:
        evaluacion['fcr'] = 'Excelente'
    elif fcr < 1.8:
        evaluacion['fcr'] = 'Muy bueno'
    elif fcr < 2.0:
        evaluacion['fcr'] = 'Bueno'
    elif fcr < 2.3:
        evaluacion['fcr'] = 'Regular'
    else:
        evaluacion['fcr'] = 'Malo'
    
    # Evaluar mortalidad
    if mortalidad_pct < 3:
        evaluacion['mortalidad'] = 'Excelente'
    elif mortalidad_pct < 5:
        evaluacion['mortalidad'] = 'Muy bueno'
    elif mortalidad_pct < 8:
        evaluacion['mortalidad'] = 'Aceptable'
    else:
        evaluacion['mortalidad'] = 'Alto'
    
    # Evaluar ADG
    if adg > 60:
        evaluacion['adg'] = 'Excelente'
    elif adg > 55:
        evaluacion['adg'] = 'Muy bueno'
    elif adg > 50:
        evaluacion['adg'] = 'Bueno'
    elif adg > 45:
        evaluacion['adg'] = 'Regular'
    else:
        evaluacion['adg'] = 'Malo'
    
    return evaluacion

def generar_alertas(lote_data: Dict) -> list:
    """
    Genera alertas basadas en los indicadores del lote
    """
    alertas = []
    
    # Alerta por FCR alto
    if lote_data.get('fcr', 0) > 2.3:
        alertas.append({
            'tipo': 'CRÍTICO',
            'categoria': 'FCR',
            'mensaje': f"FCR muy alto: {lote_data['fcr']}. Revisar calidad y cantidad de alimento.",
            'prioridad': 'alta'
        })
    elif lote_data.get('fcr', 0) > 2.0:
        alertas.append({
            'tipo': 'ADVERTENCIA',
            'categoria': 'FCR',
            'mensaje': f"FCR elevado: {lote_data['fcr']}. Monitorear consumo de alimento.",
            'prioridad': 'media'
        })
    
    # Alerta por mortalidad
    if lote_data.get('mortalidad_porcentaje', 0) > 8:
        alertas.append({
            'tipo': 'CRÍTICO',
            'categoria': 'MORTALIDAD',
            'mensaje': f"Mortalidad alta: {lote_data['mortalidad_porcentaje']}%. Revisar sanidad urgente.",
            'prioridad': 'alta'
        })
    elif lote_data.get('mortalidad_porcentaje', 0) > 5:
        alertas.append({
            'tipo': 'ADVERTENCIA',
            'categoria': 'MORTALIDAD',
            'mensaje': f"Mortalidad elevada: {lote_data['mortalidad_porcentaje']}%. Monitorear condiciones.",
            'prioridad': 'media'
        })
    
    # Alerta por ADG bajo
    if lote_data.get('adg', 0) < 45 and lote_data.get('dias_transcurridos', 0) > 14:
        alertas.append({
            'tipo': 'ADVERTENCIA',
            'categoria': 'CRECIMIENTO',
            'mensaje': f"Ganancia diaria baja: {lote_data['adg']}g/día. Revisar alimentación.",
            'prioridad': 'media'
        })
    
    # Alerta por rentabilidad baja
    if lote_data.get('rentabilidad', 0) < 10 and lote_data.get('dias_transcurridos', 0) > 21:
        alertas.append({
            'tipo': 'ADVERTENCIA',
            'categoria': 'ECONOMÍA',
            'mensaje': f"Rentabilidad baja: {lote_data['rentabilidad']}%. Revisar costos.",
            'prioridad': 'media'
        })
    
    return alertas