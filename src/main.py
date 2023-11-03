import sqlite3
import app.form_menu_saludable as fms # Importa el formulario de menú saludable

from modules.inventario import FoodElement, Inventory
from modules.plato import ComboPlate
from modules.menuSaludable import MenuSaludable

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

# Ejecuta el archivo SQL para crear las tablas
with open('restaurante.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Guarda los cambios en la base de datos
conn.commit()

# Crear un objeto de tipo inventario y agregar los datos de la base de datos
inventory = Inventory()

# Chequear si se crearon las tablas correctamente
cursor.execute("SELECT name, food_type, calories, characteristics, price FROM FoodElements")
food_elements_data = cursor.fetchall()

# Agregar los FoodElements al inventario
for data in food_elements_data:
    name, food_type, calories, characteristics, price = data
    food_element = FoodElement(name, food_type, calories, characteristics, price)
    inventory.add_food_element(food_element)


for name, food_element in inventory.food_elements.items():
    print(f"Name: {food_element.name}")
    print(f"Food Type: {food_element.food_type}")
    print(f"Calories: {food_element.calories}")
    print(f"Characteristics: {food_element.characteristics}")
    print(f"Price: ${food_element.price / 100:.2f}")
    print()

# Consulta SQL para obtener todos los datos de ComboPlates
cursor.execute("SELECT id, name, price, calories, drink_name, protein_name, side_dish_name, dessert_name FROM ComboPlates")
combo_plates_data = cursor.fetchall()

# Crear una lista de objetos ComboPlate
combo_plates = []
for data in combo_plates_data:
    id, name, price, calories, drink_name, protein_name, side_dish_name, dessert_name = data

    # Busquedas de drink_name, protein_name, side_dish_name, dessert_name en inventario

    drink_temp = inventory.food_elements[drink_name]
    protein_temp = inventory.food_elements[protein_name]
    side_dish_tem = inventory.food_elements[side_dish_name]
    dessert_tem = inventory.food_elements[dessert_name]


    # Crear un objeto ComboPlate y agregarlo a la lista combo_plates
    combo_plate = ComboPlate(id, name, price, calories, drink_temp, protein_temp, side_dish_tem, dessert_tem)
    combo_plates.append(combo_plate)


# Imprime los datos de los ComboPlates
for combo_plate in combo_plates:
    print(f"ComboPlate ID: {combo_plate.id}")
    print(f"Name: {combo_plate.name}")
    print(f"Price: ${combo_plate.price / 100:.2f}")
    print(f"Calories: {combo_plate.calories}")
    print(f"Drink: {combo_plate.drink.name}")
    print(f"Protein: {combo_plate.protein.name}")
    print(f"Side Dish: {combo_plate.side_dish.name}")
    print(f"Dessert: {combo_plate.dessert.name}")
    print()


# Consulta SQL para obtener todos los datos de menu_saludable
cursor.execute("SELECT id, name, price, calories, drink_name, protein_name, side_dish_name, dessert_name FROM MenuSaludable")
menu_saludable_data = cursor.fetchall()

# Crear una lista de objetos MenuSaludable
menu_saludables = []
for data in menu_saludable_data:
    id, name, price, calories, drink_name, protein_name, side_dish_name, dessert_name = data

    # Busquedas de drink_name, protein_name, side_dish_name, dessert_name en inventario

    drink_temp = inventory.food_elements[drink_name]
    protein_temp = inventory.food_elements[protein_name]
    side_dish_tem = inventory.food_elements[side_dish_name]
    dessert_tem = inventory.food_elements[dessert_name]


    # Crear un objeto ComboPlate y agregarlo a la lista combo_plates
    menu_saludable = MenuSaludable(id, name, price, calories, drink_temp, protein_temp, side_dish_tem, dessert_tem)
    menu_saludables.append(menu_saludable)

for menu_saludable in menu_saludables:
    print(f"Menu Saludable ID: {menu_saludable.id}")
    print(f"Name: {menu_saludable.name}")
    print(f"Price: ${menu_saludable.price / 100:.2f}")
    print(f"Calories: {menu_saludable.calories}")
    print(f"Drink: {menu_saludable.drink.name}")
    print(f"Protein: {menu_saludable.protein.name}")
    print(f"Side Dish: {menu_saludable.side_dish.name}")
    print(f"Dessert: {menu_saludable.dessert.name}")
    print()

conn.close()
