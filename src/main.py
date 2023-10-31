import sqlite3
import app.form_menu_saludable as fms # Importa el formulario de menú saludable

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

# Ejecuta el archivo SQL para crear las tablas
with open('restaurante.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Guarda los cambios en la base de datos
conn.commit()

# Chequear si se crearon las tablas correctamente
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Cierra la conexión con la base de datos
conn.close()
