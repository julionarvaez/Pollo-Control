-- ============================================
-- SCRIPT DE INICIALIZACIÓN
-- Sistema de Control de Pollos de Engorde
-- ============================================

-- Crear tablas
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    email VARCHAR(100),
    rol VARCHAR(20) DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    cantidad_inicial INTEGER NOT NULL,
    cantidad_actual INTEGER,
    genetica VARCHAR(50),
    proveedor VARCHAR(100),
    peso_inicial DECIMAL(5,2),
    galpon VARCHAR(50),
    dias_ciclo INTEGER DEFAULT 42,
    estado VARCHAR(20) DEFAULT 'activo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registros_diarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lote_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    alimento_kg DECIMAL(8,2),
    agua_litros DECIMAL(8,2),
    mortalidad INTEGER DEFAULT 0,
    causa_mortalidad TEXT,
    peso_promedio DECIMAL(5,2),
    temperatura_promedio DECIMAL(4,1),
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lote_id) REFERENCES lotes(id) ON DELETE CASCADE,
    UNIQUE(lote_id, fecha)
);

CREATE TABLE IF NOT EXISTS costos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lote_id INTEGER NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    concepto VARCHAR(200) NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL,
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lote_id) REFERENCES lotes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ingresos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lote_id INTEGER NOT NULL,
    cantidad_vendida INTEGER NOT NULL,
    peso_promedio DECIMAL(5,2) NOT NULL,
    precio_por_kg DECIMAL(8,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL,
    cliente VARCHAR(100),
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lote_id) REFERENCES lotes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sanidad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lote_id INTEGER NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    producto VARCHAR(200) NOT NULL,
    dosis VARCHAR(100),
    fecha DATE NOT NULL,
    edad_dias INTEGER,
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lote_id) REFERENCES lotes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS configuracion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clave VARCHAR(50) UNIQUE NOT NULL,
    valor TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear índices para mejor rendimiento
CREATE INDEX IF NOT EXISTS idx_lote_estado ON lotes(estado);
CREATE INDEX IF NOT EXISTS idx_registro_fecha ON registros_diarios(lote_id, fecha);
CREATE INDEX IF NOT EXISTS idx_costos_lote ON costos(lote_id);
CREATE INDEX IF NOT EXISTS idx_sanidad_lote ON sanidad(lote_id);
CREATE INDEX IF NOT EXISTS idx_ingresos_lote ON ingresos(lote_id);

-- ============================================
-- DATOS DE EJEMPLO (OPCIONAL)
-- ============================================

-- Insertar usuario administrador
-- Contraseña: admin123 (hasheada con Werkzeug)
INSERT OR IGNORE INTO usuarios (username, password_hash, nombre_completo, email, rol)
VALUES ('admin', 'scrypt:32768:8:1$yQz3lKvXhTZB8Xyj$e8f1c3b5a4d2f6e9c7b8a1d4f3e6c9b2a5d8f1e4c7b0a3d6f9e2c5b8a1d4', 'Administrador de Granja', 'admin@granja.com', 'admin');

-- Insertar lote de ejemplo
INSERT INTO lotes (nombre, fecha_inicio, cantidad_inicial, cantidad_actual, genetica, proveedor, peso_inicial, galpon, estado)
VALUES ('Lote Enero 2025', '2025-01-01', 3000, 2920, 'Cobb 500', 'Incubadora Regional', 40.0, 'Galpón 1', 'activo');

-- Obtener el ID del lote insertado
-- En SQLite usamos last_insert_rowid()

-- Insertar registros diarios de ejemplo (primeras 2 semanas)
INSERT INTO registros_diarios (lote_id, fecha, alimento_kg, agua_litros, mortalidad, peso_promedio, temperatura_promedio, observaciones)
VALUES 
    (1, '2025-01-01', 15.5, 45.0, 5, 40.0, 32.5, 'Inicio del lote, pollitos en buenas condiciones'),
    (1, '2025-01-02', 18.2, 52.0, 3, 55.0, 32.0, 'Adaptación normal'),
    (1, '2025-01-03', 21.5, 58.0, 2, 75.0, 31.5, 'Consumo aumentando'),
    (1, '2025-01-04', 25.8, 65.0, 1, 95.0, 31.0, 'Todo normal'),
    (1, '2025-01-05', 30.2, 72.0, 2, 118.0, 30.5, NULL),
    (1, '2025-01-06', 35.5, 80.0, 1, 145.0, 30.0, NULL),
    (1, '2025-01-07', 42.0, 90.0, 3, 175.0, 29.5, 'Primera semana completada'),
    (1, '2025-01-08', 48.5, 98.0, 1, 208.0, 29.0, NULL),
    (1, '2025-01-09', 55.2, 105.0, 2, 245.0, 28.5, NULL),
    (1, '2025-01-10', 62.8, 112.0, 1, 285.0, 28.0, NULL),
    (1, '2025-01-11', 70.5, 120.0, 2, 328.0, 27.5, NULL),
    (1, '2025-01-12', 78.2, 128.0, 1, 375.0, 27.0, NULL),
    (1, '2025-01-13', 86.5, 135.0, 3, 425.0, 26.5, NULL),
    (1, '2025-01-14', 95.0, 142.0, 2, 478.0, 26.0, 'Segunda semana completada'),
    (1, '2025-01-15', 103.5, 150.0, 1, 535.0, 25.5, NULL),
    (1, '2025-01-16', 112.0, 158.0, 2, 595.0, 25.0, NULL),
    (1, '2025-01-17', 120.8, 165.0, 1, 658.0, 25.0, NULL),
    (1, '2025-01-18', 129.5, 172.0, 2, 724.0, 25.0, NULL),
    (1, '2025-01-19', 138.2, 180.0, 3, 792.0, 24.5, NULL),
    (1, '2025-01-20', 147.0, 188.0, 1, 863.0, 24.5, NULL),
    (1, '2025-01-21', 156.5, 195.0, 2, 937.0, 24.0, 'Tercera semana completada'),
    (1, '2025-01-22', 166.0, 202.0, 1, 1014.0, 24.0, NULL),
    (1, '2025-01-23', 175.8, 210.0, 2, 1093.0, 24.0, NULL),
    (1, '2025-01-24', 185.5, 218.0, 3, 1175.0, 23.5, NULL),
    (1, '2025-01-25', 195.2, 225.0, 1, 1259.0, 23.5, NULL),
    (1, '2025-01-26', 205.0, 232.0, 2, 1346.0, 23.5, NULL),
    (1, '2025-01-27', 215.0, 240.0, 1, 1435.0, 23.0, NULL),
    (1, '2025-01-28', 225.0, 248.0, 2, 1527.0, 23.0, 'Cuarta semana completada - Buen crecimiento');

-- Insertar costos de ejemplo
INSERT INTO costos (lote_id, categoria, concepto, monto, fecha, observaciones)
VALUES
    (1, 'Pollitos', 'Compra de 3000 pollitos BB Cobb 500', 4500000.00, '2025-01-01', 'Proveedor: Incubadora Regional'),
    (1, 'Alimento', 'Alimento iniciación 500kg', 850000.00, '2025-01-01', 'Primera compra'),
    (1, 'Alimento', 'Alimento iniciación 1000kg', 1700000.00, '2025-01-08', 'Segunda compra'),
    (1, 'Alimento', 'Alimento crecimiento 1500kg', 2400000.00, '2025-01-15', 'Cambio a fase crecimiento'),
    (1, 'Alimento', 'Alimento crecimiento 2000kg', 3200000.00, '2025-01-22', 'Reposición'),
    (1, 'Medicamentos', 'Vacuna Newcastle + Bronquitis', 180000.00, '2025-01-05', 'Vacunación día 5'),
    (1, 'Medicamentos', 'Vitaminas ADE', 95000.00, '2025-01-10', 'Suplementación'),
    (1, 'Medicamentos', 'Vacuna Gumboro', 220000.00, '2025-01-14', 'Vacunación día 14'),
    (1, 'Energía', 'Consumo eléctrico enero (estimado)', 450000.00, '2025-01-15', 'Calefacción e iluminación'),
    (1, 'Mano de Obra', 'Salario operario enero', 1200000.00, '2025-01-01', 'Pago mensual'),
    (1, 'Transporte', 'Flete pollitos', 180000.00, '2025-01-01', 'Transporte desde incubadora'),
    (1, 'Otro', 'Viruta para cama', 250000.00, '2025-01-01', '10 bultos de viruta');

-- Insertar registros sanitarios de ejemplo
INSERT INTO sanidad (lote_id, tipo, producto, dosis, fecha, edad_dias, observaciones)
VALUES
    (1, 'Vacuna', 'Newcastle + Bronquitis IB', 'Ocular/Nasal', '2025-01-05', 5, 'Primera vacunación'),
    (1, 'Vitaminas', 'ADE + Electrolitos', '1g/litro de agua', '2025-01-10', 10, 'Refuerzo nutricional'),
    (1, 'Vacuna', 'Gumboro (Bursine)', 'En agua de bebida', '2025-01-14', 14, 'Prevención enfermedad de Gumboro'),
    (1, 'Vitaminas', 'Complejo B + C', '0.5g/litro', '2025-01-20', 20, 'Reducción estrés por calor'),
    (1, 'Antibiótico', 'Enrofloxacina', '10ml/20L agua', '2025-01-24', 24, 'Prevención infecciones respiratorias');

-- Insertar configuración de la granja
INSERT INTO configuracion (clave, valor)
VALUES
    ('nombre_granja', 'Granja Avícola Mi Lote'),
    ('ubicacion', 'Montería, Córdoba'),
    ('moneda', 'COP'),
    ('idioma', 'es'),
    ('fcr_objetivo', '1.8'),
    ('mortalidad_maxima', '5.0'),
    ('backup_automatico', 'true'),
    ('frecuencia_backup', 'semanal');

-- ============================================
-- VISTAS ÚTILES PARA REPORTES
-- ============================================

-- Vista: Resumen de lotes con estadísticas básicas
CREATE VIEW IF NOT EXISTS v_resumen_lotes AS
SELECT 
    l.id,
    l.nombre,
    l.fecha_inicio,
    l.cantidad_inicial,
    l.cantidad_actual,
    l.genetica,
    l.galpon,
    l.estado,
    JULIANDAY('now') - JULIANDAY(l.fecha_inicio) as dias_transcurridos,
    (SELECT COUNT(*) FROM registros_diarios WHERE lote_id = l.id) as dias_registrados,
    (SELECT SUM(mortalidad) FROM registros_diarios WHERE lote_id = l.id) as total_mortalidad,
    (SELECT SUM(alimento_kg) FROM registros_diarios WHERE lote_id = l.id) as total_alimento,
    (SELECT SUM(monto) FROM costos WHERE lote_id = l.id) as total_costos,
    (SELECT SUM(total) FROM ingresos WHERE lote_id = l.id) as total_ingresos
FROM lotes l;

-- Vista: Registros diarios con datos del lote
CREATE VIEW IF NOT EXISTS v_registros_completos AS
SELECT 
    r.id,
    r.lote_id,
    l.nombre as lote_nombre,
    r.fecha,
    JULIANDAY(r.fecha) - JULIANDAY(l.fecha_inicio) as dia_ciclo,
    r.alimento_kg,
    r.agua_litros,
    r.mortalidad,
    r.peso_promedio,
    r.temperatura_promedio,
    r.observaciones
FROM registros_diarios r
JOIN lotes l ON r.lote_id = l.id;

-- Vista: Costos agrupados por categoría
CREATE VIEW IF NOT EXISTS v_costos_por_categoria AS
SELECT 
    lote_id,
    categoria,
    COUNT(*) as cantidad_registros,
    SUM(monto) as total,
    AVG(monto) as promedio
FROM costos
GROUP BY lote_id, categoria;

-- ============================================
-- TRIGGERS PARA MANTENER INTEGRIDAD
-- ============================================

-- Trigger: Actualizar cantidad_actual cuando se registra mortalidad
CREATE TRIGGER IF NOT EXISTS trg_actualizar_cantidad_mortalidad
AFTER INSERT ON registros_diarios
WHEN NEW.mortalidad > 0
BEGIN
    UPDATE lotes 
    SET cantidad_actual = cantidad_actual - NEW.mortalidad,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.lote_id;
END;

-- Trigger: Actualizar fecha de modificación del lote
CREATE TRIGGER IF NOT EXISTS trg_actualizar_lote_timestamp
AFTER UPDATE ON lotes
BEGIN
    UPDATE lotes SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- ============================================
-- FUNCIONES DE UTILIDAD (QUERIES)
-- ============================================

-- Query: Obtener FCR de un lote
-- FCR = Alimento Total / Ganancia de Peso Total (kg)
-- Usar en aplicación, no es función SQL nativa

-- Query: Obtener mortalidad % de un lote
-- SELECT 
--     lote_id,
--     (SUM(mortalidad) * 100.0 / (SELECT cantidad_inicial FROM lotes WHERE id = lote_id)) as mortalidad_pct
-- FROM registros_diarios
-- GROUP BY lote_id;

-- Query: Obtener rendimiento diario
-- SELECT 
--     lote_id,
--     fecha,
--     alimento_kg,
--     mortalidad,
--     peso_promedio,
--     (peso_promedio - LAG(peso_promedio, 1) OVER (PARTITION BY lote_id ORDER BY fecha)) as ganancia_diaria
-- FROM registros_diarios;

-- ============================================
-- FINALIZACIÓN
-- ============================================

-- Verificar que todo se creó correctamente
SELECT 'Tablas creadas:', COUNT(*) FROM sqlite_master WHERE type='table';
SELECT 'Índices creados:', COUNT(*) FROM sqlite_master WHERE type='index';
SELECT 'Vistas creadas:', COUNT(*) FROM sqlite_master WHERE type='view';
SELECT 'Triggers creados:', COUNT(*) FROM sqlite_master WHERE type='trigger';

-- Mostrar datos de ejemplo
SELECT 'Usuarios:', COUNT(*) FROM usuarios;
SELECT 'Lotes:', COUNT(*) FROM lotes;
SELECT 'Registros diarios:', COUNT(*) FROM registros_diarios;
SELECT 'Costos:', COUNT(*) FROM costos;
SELECT 'Sanidad:', COUNT(*) FROM sanidad;

COMMIT;