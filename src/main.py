#region imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction
from PyQt5.QtCore import Qt

import sys
import sqlite3

from app.form_menu_saludable import menuSaludableWindow
from modules.inventario import FoodElement, Inventory
from modules.plato import ComboPlate
from modules.menuSaludable import MenuSaludable
from modules.ordenes import Order, Payment, Table, OrderLog, PaymentLog

from app.view_inventory import InventoryWindow
from app.view_dishes import DishWindow
from app.view_orders import OrderPaymentWindow
#endregion

#region connection
# Crear una conexión a la base de datos
conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

# Ejecuta el archivo SQL para crear las tablas
with open('restaurante.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Guarda los cambios en la base de datos
conn.commit()
#endregion

#region de quemado de datos

#Inventario
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

# ComboPlates
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

# MenuSaludable
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

"""
Tables/Orders/Payments
En esta parte del código se van a crear las mesas, las ordenes y los pagos.
Se toma en cuenta la creación de los logs de ordenes y pagos.
"""
# Crear el log de ordenes
order_log = OrderLog()
# Crear el log de pagos
payment_log = PaymentLog()

# Crear las mesas del restaurante 1 a 6
tables = {}
table1 = Table(number=1, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")
table2 = Table(number=2, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")
table3 = Table(number=3, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")
table4 = Table(number=4, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")
table5 = Table(number=5, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")
table6 = Table(number=6, order_log=order_log, payment_log=payment_log, number_of_customers=0, single_bill=False, status="Libre")

# Agregar las mesas al diccionario tables
tables[1] = table1
tables[2] = table2
tables[3] = table3
tables[4] = table4
tables[5] = table5
tables[6] = table6

# agregamos algunas ordenes y pagos a las mesas
# Ordenes
order1 = Order(1, "carlos", "Lista")
order1.add_dish(combo_plates[0])
order1.add_dish(combo_plates[3])
order2 = Order(2, "juan", "Lista")
order2.add_dish(combo_plates[1])
order2.add_dish(combo_plates[4])
table1.add_order(order1)
table3.add_order(order2)

# Pagos
temp_order1 = [order1]
temp_order2 = [order2]
payment1 = Payment(temp_order1, True)
payment2 = Payment(temp_order2, True)
table1.add_payment(payment1)
table3.add_payment(payment2)

#endregion

#region de la clase restaurante para mantener los datos actualizados mientras se usa el programa
class RestauranteModel:
    def __init__(self) -> None:
        self.inventory: Inventory = inventory
        self.combo_plates = combo_plates
        self.menu_saludables = menu_saludables
        self.tables = tables
        self.order_log = order_log
        self.payment_log = payment_log
#endregion

#region main window
# Class for the main window
class MyApp(QMainWindow):
    def __init__(self, restaurant_model) -> None:
        super().__init__()
        self.restaurant_model = restaurant_model

        self.setWindowTitle("Restaurante")
        self.setGeometry(100, 100, 600, 400)

        menubar = self.menuBar()

        # Create the menu items
        inventory_menu = menubar.addMenu("Inventario")
        dish_menu = menubar.addMenu("Platillos")
        order_menu = menubar.addMenu("Ordenes y Pagos")
        report_menu = menubar.addMenu("Reportes")


        # Add the actions to the menus
        inventory_action = QAction("Editar inventario", self)
        inventory_action.triggered.connect(self.open_inventory)
        inventory_menu.addAction(inventory_action)

        dish_action = QAction("Ver platillos", self)
        dish_action.triggered.connect(self.open_dish)
        dish_menu.addAction(dish_action)
        
        order_action = QAction("Ordenar", self)
        order_action.triggered.connect(self.open_order)
        order_menu.addAction(order_action)
    
    def open_inventory(self):
        self.inventory_window = InventoryWindow(self.restaurant_model)
        self.inventory_window.show()

    def open_dish(self):
        self.dish_window = DishWindow(self.restaurant_model)
        self.dish_window.show()
    
    def open_order(self):
        self.order_window = OrderPaymentWindow(self.restaurant_model)
        self.order_window.show()
    
def main():
    app = QApplication(sys.argv)

    restaurant_model = RestauranteModel()
    
    windows = MyApp(restaurant_model=restaurant_model)
    windows.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
#endregion


    

