import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from modules.inventario import FoodElement, Inventory

# Clase para manejar el dialogo de agregar un FoodElement
class AddFoodElementDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agregar comida")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Add the neccesary labels
        self.name_label = QLabel("Nombre")
        self.name_imput = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_imput)

        self.food_type_label = QLabel("Tipo de comida")
        self.food_type_imput = QComboBox()
        self.food_type_imput.addItems(["Bebida", "Proteina", "Acompañamiento", "Postre"])
        layout.addWidget(self.food_type_label)
        layout.addWidget(self.food_type_imput)

        self.calories_label = QLabel("Calorias")
        self.calories_imput = QLineEdit()
        layout.addWidget(self.calories_label)
        layout.addWidget(self.calories_imput)

        self.characteristics_label = QLabel("Caracteristicas")
        self.characteristics_imput = QLineEdit()
        layout.addWidget(self.characteristics_label)
        layout.addWidget(self.characteristics_imput)

        self.price_label = QLabel("Precio")
        self.price_imput = QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_imput)

        # Add the neccesary buttons
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def get_name(self):
        return self.name_imput.text()
    
    def get_food_type(self):
        return self.food_type_imput.currentText()

    def get_calories(self):
        return int(self.calories_imput.text())
    
    def get_characteristics(self):
        return self.characteristics_imput.text()
    
    def get_price(self):
        return int(self.price_imput.text())

# Clase para manejar el dialogo de editar un FoodElement
class EditFoodElementDialog(QDialog):
    def __init__(self, food_element: FoodElement):
        super().__init__()

        self.setWindowTitle("Editar comida")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Add the neccesary labels
        self.name_label = QLabel("Nombre")
        self.name_imput = QLineEdit(food_element.name)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_imput)

        self.food_type_label = QLabel("Tipo de comida")
        self.food_type_imput = QComboBox()
        self.food_type_imput.addItems(["Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.food_type_imput.setCurrentText(food_element.food_type)
        layout.addWidget(self.food_type_label)
        layout.addWidget(self.food_type_imput)

        self.calories_label = QLabel("Calorias")
        self.calories_imput = QLineEdit(str(food_element.calories))
        layout.addWidget(self.calories_label)
        layout.addWidget(self.calories_imput)

        self.characteristics_label = QLabel("Caracteristicas")
        self.characteristics_imput = QLineEdit(food_element.characteristics)
        layout.addWidget(self.characteristics_label)
        layout.addWidget(self.characteristics_imput)

        self.price_label = QLabel("Precio")
        self.price_imput = QLineEdit(str(food_element.price))
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_imput)

        # Add the neccesary buttons
        self.add_button = QPushButton("Editar")
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        
    def get_name(self):
        return self.name_imput.text()
        
    def get_food_type(self):
        return self.food_type_imput.currentText()
        
    def get_calories(self):
        return int(self.calories_imput.text())
        
    def get_characteristics(self):
        return self.characteristics_imput.text()
        
    def get_price(self):
        return int(self.price_imput.text())
    
# Clase para manejar el dialogo de eliminar un FoodElement
class DeleteFoodElementDialog(QDialog):
    def __init__(self, food_element_name: str):
        super().__init__()

        self.setWindowTitle("Eliminar comida")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Add the neccesary labels
        self.name_label = QLabel("Nombre")
        self.name_imput = QLineEdit(food_element_name)
        self.name_imput.setReadOnly(True)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_imput)

        # Add the neccesary buttons
        self.add_button = QPushButton("Eliminar")
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

# Clase para visualizar el inventario de comidas
class InventoryWindow(QWidget):
    def __init__(self, inventory: Inventory) -> None:
        super().__init__()
        self.inventory = inventory
        self.setWindowTitle("Inventario de comidas")
        self.setGeometry(100, 100, 1200, 1000)
        
        # Add the neccesary buttons
        self.add_button = QPushButton("Agregar", self)
        self.add_button.setGeometry(50, 10, 100, 30)
        self.add_button.clicked.connect(self.add_food)

        self.edit_button = QPushButton("Editar", self)
        self.edit_button.setGeometry(150, 10, 100, 30)
        self.edit_button.clicked.connect(self.edit_food)

        self.delete_button = QPushButton("Eliminar", self)
        self.delete_button.setGeometry(250, 10, 100, 30)
        self.delete_button.clicked.connect(self.delete_food)

        self.add_button = QPushButton("Refresh", self)
        self.add_button.setGeometry(350, 10, 100, 30)
        self.add_button.clicked.connect(self.populate_table)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 650, 650)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Tipo de comida", "Calorias", "Caracteristicas", "Precio"])

        # Populate the table with the data from the inventory
        self.populate_table()

        # Set the table to not editable
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the table headers to resize to the content
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    # Método para poblar la tabla con los datos del inventario
    def populate_table(self) -> None:
        # Obtain the food elements from the inventory
        food_elements = self.inventory.food_elements.values()

        # Configurar el número de filas de la tabla
        self.tableWidget.setRowCount(len(food_elements))

        # Poblar la tabla con los datos de los FoodElements
        for row, food_element in enumerate(food_elements):
            name = QTableWidgetItem(food_element.name)
            food_type = QTableWidgetItem(food_element.food_type)
            calories = QTableWidgetItem(str(food_element.calories))
            characteristics = QTableWidgetItem(food_element.characteristics)
            price = QTableWidgetItem(str(food_element.price))

            self.tableWidget.setItem(row, 0, name)
            self.tableWidget.setItem(row, 1, food_type)
            self.tableWidget.setItem(row, 2, calories)
            self.tableWidget.setItem(row, 3, characteristics)
            self.tableWidget.setItem(row, 4, price)


    # Método para agregar un FoodElement al inventario
    def add_food(self):
        
        dialog = AddFoodElementDialog()

        if dialog.exec_() == QDialog.Accepted:
            name = dialog.get_name()
            food_type = dialog.get_food_type()
            calories = dialog.get_calories()
            characteristics = dialog.get_characteristics()
            price = dialog.get_price()

            food_element = FoodElement(name, food_type, calories, characteristics, price)
            self.inventory.add_food_element(food_element)

            # Guardar los cambios en la base de datos
            conn = sqlite3.connect('restaurante.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FoodElements(name, food_type, calories, characteristics, price) VALUES (?, ?, ?, ?, ?)", (name, food_type, calories, characteristics, price))
            conn.commit()
            conn.close()

            # Actualizar la tabla
            self.populate_table()


    # Método para editar un FoodElement del inventario
    def edit_food(self):
        # Obtener el nombre del FoodElement seleccionado
        # Exepcion por si no se selecciona nada mostrar un mensaje
        try:
            selected_food_element_name = self.tableWidget.selectedItems()[0].text()

            try:
                # Obtener el FoodElement seleccionado del inventario
                selected_food_element = self.inventory.food_elements[selected_food_element_name]

                # Crear el dialogo para editar el FoodElement
                dialog = EditFoodElementDialog(selected_food_element)

                if dialog.exec_() == QDialog.Accepted:
                    # Obtener los nuevos datos del FoodElement
                    name = dialog.get_name()
                    food_type = dialog.get_food_type()
                    calories = dialog.get_calories()
                    characteristics = dialog.get_characteristics()
                    price = dialog.get_price()

                    # Crear el nuevo FoodElement
                    new_food_element = FoodElement(name, food_type, calories, characteristics, price)

                    # Editar el FoodElement en el inventario
                    self.inventory.modify_food_element(selected_food_element_name, new_food_element)

                    # Guardar los cambios en la base de datos
                    conn = sqlite3.connect('restaurante.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE FoodElements SET name = ?, food_type = ?, calories = ?, characteristics = ?, price = ? WHERE name = ?", (name, food_type, calories, characteristics, price, selected_food_element_name))
                    conn.commit()
                    conn.close()

                    # Actualizar la tabla
                    self.populate_table()
            except KeyError:
                QMessageBox.about(self, "Error", "No se encontro el elemento en el inventario o no se selecciono ningun elemento valido")

        except IndexError:
            QMessageBox.about(self, "Error", "No se selecciono ningun elemento")

    # Método para eliminar un FoodElement del inventario
    def delete_food(self):

        try:
            # Obtener el nombre del FoodElement seleccionado
            selected_food_element_name = self.tableWidget.selectedItems()[0].text()

            # verificamos que el elemento exista en el inventario
            if selected_food_element_name in self.inventory.food_elements:
                # Eliminar el FoodElement del inventario
                self.inventory.remove_food_element(selected_food_element_name)


                # Guardar los cambios en la base de datos
                conn = sqlite3.connect('restaurante.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM FoodElements WHERE name = ?", (selected_food_element_name,))
                conn.commit()
                conn.close()

                # Actualizar la tabla
                self.populate_table()
            else:
                QMessageBox.about(self, "Error", "No se encontro el elemento en el inventario o no se selecciono ningun elemento valido")

        except IndexError:
            QMessageBox.about(self, "Error", "No se selecciono ningun elemento")