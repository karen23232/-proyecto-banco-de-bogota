import sqlite3

DB_NAME = 'database.db'

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS practicantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            carrera TEXT NOT NULL,
            semestre INTEGER NOT NULL,
            hoja_vida TEXT NOT NULL,
            estado TEXT DEFAULT 'pendiente'
        )
    ''')
    conn.commit()
    conn.close()

# Guardar un practicante nuevo
def guardar_practicante(nombre, correo, carrera, semestre, hoja_vida):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO practicantes (nombre, correo, carrera, semestre, hoja_vida)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, correo, carrera, semestre, hoja_vida))


# Obtener la lista de practicantes
def obtener_practicantes():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Para que puedas usar nombres de columnas si lo deseas
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM practicantes ORDER BY id DESC")
    practicantes = cursor.fetchall()
    conn.close()
    return practicantes

# Actualizar el estado del practicante
def actualizar_estado(id, estado):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE practicantes SET estado = ? WHERE id = ?", (estado, id))
    conn.commit()
    conn.close()
def eliminar_practicante(id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM practicantes WHERE id = ?", (id,))
