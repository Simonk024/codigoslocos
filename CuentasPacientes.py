import sqlite3
from datetime import datetime

# Conexión a la base de datos
conn = sqlite3.connect('cuentas_medicas.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cuentas (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER NOT NULL,
        fecha DATE NOT NULL,
        monto REAL NOT NULL,
        descripcion TEXT NOT NULL,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id INTEGER PRIMARY KEY,
        cuenta_id INTEGER NOT NULL,
        fecha DATE NOT NULL,
        monto REAL NOT NULL,
        FOREIGN KEY (cuenta_id) REFERENCES cuentas (id)
    );
''')

# Función para agregar un paciente
def agregar_paciente(nombre, apellido, fecha_nacimiento):
    cursor.execute('INSERT INTO pacientes (nombre, apellido, fecha_nacimiento) VALUES (?, ?, ?)', (nombre, apellido, fecha_nacimiento))
    conn.commit()

# Función para agregar una cuenta
def agregar_cuenta(paciente_id, fecha, monto, descripcion):
    cursor.execute('INSERT INTO cuentas (paciente_id, fecha, monto, descripcion) VALUES (?, ?, ?, ?)', (paciente_id, fecha, monto, descripcion))
    conn.commit()

# Función para agregar un pago
def agregar_pago(cuenta_id, fecha, monto):
    cursor.execute('INSERT INTO pagos (cuenta_id, fecha, monto) VALUES (?, ?, ?)', (cuenta_id, fecha, monto))
    conn.commit()

# Función para obtener las cuentas de un paciente
def obtener_cuentas_paciente(paciente_id):
    cursor.execute('SELECT * FROM cuentas WHERE paciente_id = ?', (paciente_id,))
    return cursor.fetchall()

# Función para obtener los pagos de una cuenta
def obtener_pagos_cuenta(cuenta_id):
    cursor.execute('SELECT * FROM pagos WHERE cuenta_id = ?', (cuenta_id,))
    return cursor.fetchall()

# Función para ordenar las cuentas por fecha
def ordenar_cuentas_por_fecha():
    cursor.execute('SELECT * FROM cuentas ORDER BY fecha')
    return cursor.fetchall()

# Función para ordenar las cuentas por monto
def ordenar_cuentas_por_monto():
    cursor.execute('SELECT * FROM cuentas ORDER BY monto')
    return cursor.fetchall()

# Interfaz de usuario
while True:
    print('1. Agregar paciente')
    print('2. Agregar cuenta')
    print('3. Agregar pago')
    print('4. Obtener cuentas de un paciente')
    print('5. Obtener pagos de una cuenta')
    print('6. Ordenar cuentas por fecha')
    print('7. Ordenar cuentas por monto')
    print('8. Salir')
    
    opcion = input('Ingrese una opción: ')
    
    if opcion == '1':
        nombre = input('Ingrese el nombre del paciente: ')
        apellido = input('Ingrese el apellido del paciente: ')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ')
        agregar_paciente(nombre, apellido, fecha_nacimiento)
    elif opcion == '2':
        paciente_id = int(input('Ingrese el ID del paciente: '))
        fecha = input('Ingrese la fecha de la cuenta (YYYY-MM-DD): ')
        monto = float(input('Ingrese el monto de la cuenta: '))
        descripcion = input('Ingrese la descripción de la cuenta: ')
        agregar_cuenta(paciente_id, fecha, monto, descripcion)
    elif opcion == '3':
        cuenta_id = int(input('Ingrese el ID de la cuenta: '))
        fecha = input('