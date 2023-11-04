import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from modules.plato import ComboPlate, ComboPlateFactory
from modules.menuSaludable import MenuSaludable
from modules.inventario import FoodElement, Inventory

# region Button Dialog
# Clase para manejar la ventana de agregar combos
class AddComboWindow(QDialog):
    def __init__(self, inventoryData: Inventory) -> None:
        super().__init__()
        
        self.setWindowTitle("Agregar Combo")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Crear los labels y los inputs para agregar un combo
        self.name_label = QLabel("Nombre")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.price_label = QLabel("Precio")
        self.price_input = QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.calories_label = QLabel("Calorias")
        self.calories_input = QLineEdit()
        layout.addWidget(self.calories_label)
        layout.addWidget(self.calories_input)

        # Para bebidas, proteinas, acompañamientos y postres
        # Se crea un combobox para cada uno de los elementos del inventario
        self.drink_label = QLabel("Bebida")
        self.drink_input = QComboBox()
        self.drink_input.addItems(inventoryData.get_food_elements_names("bebida"))
        print(inventoryData.get_food_elements_names("drink"))
        layout.addWidget(self.drink_label)
        layout.addWidget(self.drink_input)

        self.protein_label = QLabel("Proteina")
        self.protein_input = QComboBox()
        # Generar lista de nombres de proteinas usando el inventario
        self.protein_input.addItems(inventoryData.get_food_elements_names("proteina"))
        layout.addWidget(self.protein_label)
        layout.addWidget(self.protein_input)

        self.side_dish_label = QLabel("Acompañamiento")
        self.side_dish_input = QComboBox()
        self.side_dish_input.addItems(inventoryData.get_food_elements_names("acompanamiento"))
        layout.addWidget(self.side_dish_label)
        layout.addWidget(self.side_dish_input)

        self.dessert_label = QLabel("Postre")
        self.dessert_input = QComboBox()
        self.dessert_input.addItems(inventoryData.get_food_elements_names("postre"))    
        layout.addWidget(self.dessert_label)
        layout.addWidget(self.dessert_input)
        
        # Crear el botón para agregar el combo
        self.add_combo_button = QPushButton("Agregar Combo")
        self.add_combo_button.clicked.connect(self.accept)
        layout.addWidget(self.add_combo_button)

        self.setLayout(layout)
    
    # Métodos para obtener los datos del combo
    def get_name(self) -> str:
        return self.name_input.text()
    
    def get_price(self) -> int:
        return int(self.price_input.text())
    
    def get_calories(self) -> int:
        return int(self.calories_input.text())
    
    def get_drink(self) -> str:
        return self.drink_input.currentText()
    
    def get_protein(self) -> str:
        return self.protein_input.currentText()
    
    def get_side_dish(self) -> str:
        return self.side_dish_input.currentText()
    
    def get_dessert(self) -> str:
        return self.dessert_input.currentText()
    
# Clase para manejar la ventana de modificar combos
class ModifyComboWindow(QDialog):
    def __init__(self, combo_plate: ComboPlate, inventoryData: Inventory) -> None:
        super().__init__()
        
        self.setWindowTitle("Modificar Combo")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Crear los labels y los inputs para modificar un combo
        self.name_label = QLabel("Nombre")
        self.name_input = QLineEdit()
        self.name_input.setText(combo_plate.name)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.price_label = QLabel("Precio")
        self.price_input = QLineEdit()
        self.price_input.setText(str(combo_plate.price))
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.calories_label = QLabel("Calorias")
        self.calories_input = QLineEdit()
        self.calories_input.setText(str(combo_plate.calories))
        layout.addWidget(self.calories_label)
        layout.addWidget(self.calories_input)

        # Para bebidas, proteinas, acompañamientos y postres
        # Se crea un combobox para cada uno de los elementos del inventario
        self.drink_label = QLabel("Bebida")
        self.drink_input = QComboBox()
        self.drink_input.addItems(inventoryData.get_food_elements_names("bebida"))
        self.drink_input.setCurrentText(combo_plate.drink.name)
        layout.addWidget(self.drink_label)
        layout.addWidget(self.drink_input)

        self.protein_label = QLabel("Proteina")
        self.protein_input = QComboBox()
        # Generar lista de nombres de proteinas usando el inventario
        self.protein_input.addItems(inventoryData.get_food_elements_names("proteina"))
        self.protein_input.setCurrentText(combo_plate.protein.name)
        layout.addWidget(self.protein_label)
        layout.addWidget(self.protein_input)

        self.side_dish_label = QLabel("Acompañamiento")
        self.side_dish_input = QComboBox()
        self.side_dish_input.addItems(inventoryData.get_food_elements_names("acompanamiento"))
        self.side_dish_input.setCurrentText(combo_plate.side_dish.name)
        layout.addWidget(self.side_dish_label)
        layout.addWidget(self.side_dish_input)

        self.dessert_label = QLabel("Postre")
        self.dessert_input = QComboBox()
        self.dessert_input.addItems(inventoryData.get_food_elements_names("postre"))
        self.dessert_input.setCurrentText(combo_plate.dessert.name)
        layout.addWidget(self.dessert_label)
        layout.addWidget(self.dessert_input)

        # Crear el botón para modificar el combo
        self.modify_combo_button = QPushButton("Modificar Combo")
        self.modify_combo_button.clicked.connect(self.accept)
        layout.addWidget(self.modify_combo_button)

        self.setLayout(layout)

    # Métodos para obtener los datos del combo
    def get_name(self) -> str:
        return self.name_input.text()
    
    def get_price(self) -> int:
        return int(self.price_input.text())
    
    def get_calories(self) -> int:
        return int(self.calories_input.text())
    
    def get_drink(self) -> str:
        return self.drink_input.currentText()
    
    def get_protein(self) -> str:
        return self.protein_input.currentText()
    
    def get_side_dish(self) -> str:
        return self.side_dish_input.currentText()
    
    def get_dessert(self) -> str:
        return self.dessert_input.currentText()

# Clase para manejar la ventana de eliminar combos
class DeleteComboWindow(QDialog):
    def __init__(self, combo_plate: ComboPlate) -> None:
        super().__init__()

        self.setWindowTitle("Eliminar Combo")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Crear los labels y los inputs para eliminar un combo
        self.name_label = QLabel("ID")
        self.name_input = QLineEdit(combo_plate.id)
        self.name_input.setReadOnly(True)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Crear el botón para eliminar el combo
        self.add_button = QPushButton("Eliminar Combo")
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
# endregion

# region Search Dialog
# Clase para manejar la ventana de buscar combos por rango de precio
class SearchComboByPriceWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Buscar por rango de precio")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Crear los labels y los inputs para buscar combos por rango de precio
        self.min_price_label = QLabel("Precio Minimo")
        self.min_price_input = QLineEdit()
        layout.addWidget(self.min_price_label)
        layout.addWidget(self.min_price_input)

        self.max_price_label = QLabel("Precio Maximo")
        self.max_price_input = QLineEdit()
        layout.addWidget(self.max_price_label)
        layout.addWidget(self.max_price_input)

        # Crear el botón para buscar combos por rango de precio
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.accept)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    # Métodos para obtener los datos del combo
    def get_min_price(self) -> int:
        return int(self.min_price_input.text())

    
    def get_max_price(self) -> int:
        return int(self.max_price_input.text())

# Clase para manejar la ventana de buscar combos por caracteristicas
class SearchComboByCharacteristicWindow(QDialog):
    def __init__(self, inventoryData: Inventory) -> None:
        super().__init__()

        self.setWindowTitle("Buscar por caracteristicas")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Crear la ComboBox para seleccionar la de caracteristica a buscar
        self.characteristic_label = QLabel("Tipo de caracteristica")
        self.characteristic_input = QComboBox()
        self.characteristic_input.addItems(inventoryData.get_all_characteristics())
        print(inventoryData.get_all_characteristics())
        layout.addWidget(self.characteristic_label)
        layout.addWidget(self.characteristic_input)

        # Crear el botón para buscar combos por caracteristicas
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.accept)
        layout.addWidget(self.search_button)

        self.setLayout(layout)
    
    # Método para obtener la caracteristica a buscar
    def get_characteristic(self) -> str:
        return self.characteristic_input.currentText()

# Clase para manejar la ventana de buscar combos por contenido del nombre
class SearchComboByNameWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Buscar por contenido del nombre")
        self.setGeometry(400, 400, 600, 400)

        layout = QVBoxLayout()

        # Crear los labels y los inputs para buscar combos por contenido del nombre
        self.name_label = QLabel("Nombre o contenido del nombre")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Crear el botón para buscar combos por contenido del nombre
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.accept)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    # Método para obtener el contenido del nombre a buscar
    def get_name(self) -> str:
        return self.name_input.text()
# endregion

# Clase para vizualizar los combos y el menu saludable
class DishWindow(QWidget):
    def __init__(self, restaurant_model) -> None:
        super().__init__()
        self.restaurant_model = restaurant_model
        self.inventoryData: Inventory = restaurant_model.inventory
        self.combo_platesData: list[ComboPlate] = restaurant_model.combo_plates
        self.menu_saludablesData: MenuSaludable = restaurant_model.menu_saludables
        self.setWindowTitle("Combos y Menu Saludable")
        self.setGeometry(100, 100, 1200, 1000)

        # Crear botones para agregar, modificar y eliminar combos
        self.add_combo_button = QPushButton("Agregar Combo", self)
        self.add_combo_button.setGeometry(0, 10, 100, 50)
        self.add_combo_button.clicked.connect(self.add_combo)

        self.modify_combo_button = QPushButton("Modificar Combo", self)
        self.modify_combo_button.setGeometry(105, 10, 100, 50)
        self.modify_combo_button.clicked.connect(self.modify_combo)

        self.delete_combo_button = QPushButton("Eliminar Combo", self)
        self.delete_combo_button.setGeometry(210, 10, 100, 50)
        self.delete_combo_button.clicked.connect(self.delete_combo)

        self.refresh_combo_button = QPushButton("Actualizar", self)
        self.refresh_combo_button.setGeometry(315, 10, 60, 50)
        self.refresh_combo_button.clicked.connect(self.populate_combo_table)

        # Botones para busqueda de combos (son 3 botones)
        # Buscar por rango de precio
        self.add_search_price_button = QPushButton("Buscar por rango de precio", self)
        self.add_search_price_button.setGeometry(385, 10, 200, 50)
        self.add_search_price_button.clicked.connect(self.populate_combo_table_by_price)

        # Buscar por caracteristica de los elementos
        self.add_search_characteristic_button = QPushButton("Buscar por caracteristicas", self)
        self.add_search_characteristic_button.setGeometry(590, 10, 200, 50)
        self.add_search_characteristic_button.clicked.connect(self.populate_combo_table_by_characteristic)

        # Buscar por contenido del nombre
        self.add_search_name_button = QPushButton("Buscar por contenido del nombre", self)
        self.add_search_name_button.setGeometry(795, 10, 200, 50)
        self.add_search_name_button.clicked.connect(self.populate_combo_table_by_name)

        # Crear la tabla para vizualizar los combos
        self.combo_platesTable = QTableWidget(self)
        self.combo_platesTable.setGeometry(0, 75, 1000, 500)
        self.combo_platesTable.setColumnCount(8)
        self.combo_platesTable.setHorizontalHeaderLabels(["ID", "Nombre", "Precio", "Calorias", "Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.combo_platesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        # Crear la tabla para vizualizar el menu saludable
        self.menu_saludablesTable = QTableWidget(self)
        self.menu_saludablesTable.setGeometry(0, 600, 1200, 400)
        self.menu_saludablesTable.setColumnCount(8)
        self.menu_saludablesTable.setHorizontalHeaderLabels(["ID", "Nombre", "Precio", "Calorias", "Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.menu_saludablesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.menu_saludablesTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Populando la tabla de combos
        self.populate_combo_table()

    # region Combo Plate Table
    # Método para poblar la tabla de combos
    def populate_combo_table(self) -> None:

        # Se optienen los combos de la memoria
        combo_plates = self.combo_platesData

        # Se limpia la tabla
        self.combo_platesTable.setRowCount(0)

        # Se agregan los combos a la tabla
        for combo_plate in combo_plates:
            rowPosition = self.combo_platesTable.rowCount()
            self.combo_platesTable.insertRow(rowPosition)

            self.combo_platesTable.setItem(rowPosition, 0, QTableWidgetItem(str(combo_plate.id)))
            self.combo_platesTable.setItem(rowPosition, 1, QTableWidgetItem(combo_plate.name))
            self.combo_platesTable.setItem(rowPosition, 2, QTableWidgetItem(f"${combo_plate.price / 100:.2f}"))
            self.combo_platesTable.setItem(rowPosition, 3, QTableWidgetItem(str(combo_plate.calories)))
            self.combo_platesTable.setItem(rowPosition, 4, QTableWidgetItem(combo_plate.drink.name))
            self.combo_platesTable.setItem(rowPosition, 5, QTableWidgetItem(combo_plate.protein.name))
            self.combo_platesTable.setItem(rowPosition, 6, QTableWidgetItem(combo_plate.side_dish.name))
            self.combo_platesTable.setItem(rowPosition, 7, QTableWidgetItem(combo_plate.dessert.name))

    # Método para poblar la tabla combo según el rango de precio    
    def populate_combo_table_by_price(self) -> None:

        # Se obtienen los combos de la memoria
        combo_plates = self.combo_platesData

        # Se limpia la tabla
        self.combo_platesTable.setRowCount(0)

        dialog = SearchComboByPriceWindow()

        if dialog.exec() == QDialog.Accepted:

            # Se obtienen los precios
            min_price = dialog.get_min_price()
            max_price = dialog.get_max_price()
            print(min_price)
            print(max_price)

            # verificar el range de precio
            if min_price > max_price:
                QMessageBox.warning(self, "Error", "El precio minimo debe ser menor al precio maximo")

            if min_price < 0 or max_price < 0:
                QMessageBox.warning(self, "Error", "Los precios deben ser positivos")

            # Se agregan los combos a la tabla
            for combo_plate in combo_plates:
                print(combo_plate.price)
                if combo_plate.price >= min_price and combo_plate.price <= max_price:
                    rowPosition = self.combo_platesTable.rowCount()
                    self.combo_platesTable.insertRow(rowPosition)

                    self.combo_platesTable.setItem(rowPosition, 0, QTableWidgetItem(str(combo_plate.id)))
                    self.combo_platesTable.setItem(rowPosition, 1, QTableWidgetItem(combo_plate.name))
                    self.combo_platesTable.setItem(rowPosition, 2, QTableWidgetItem(f"${combo_plate.price / 100:.2f}"))
                    self.combo_platesTable.setItem(rowPosition, 3, QTableWidgetItem(str(combo_plate.calories)))
                    self.combo_platesTable.setItem(rowPosition, 4, QTableWidgetItem(combo_plate.drink.name))
                    self.combo_platesTable.setItem(rowPosition, 5, QTableWidgetItem(combo_plate.protein.name))
                    self.combo_platesTable.setItem(rowPosition, 6, QTableWidgetItem(combo_plate.side_dish.name))
                    self.combo_platesTable.setItem(rowPosition, 7, QTableWidgetItem(combo_plate.dessert.name))

    # Método para popular la tabla combo según una caracteristica
    def populate_combo_table_by_characteristic(self) -> None:

        # Se obtienen los combos de la memoria
        combo_plates = self.combo_platesData

        # Se limpia la tabla
        self.combo_platesTable.setRowCount(0)

        dialog = SearchComboByCharacteristicWindow(self.inventoryData)

        try:
            if dialog.exec() == QDialog.Accepted:
                
                # Se obtiene la caracteristica
                characteristic = dialog.get_characteristic()

                # Se agregan los combos a la tabla
                for combo_plate in combo_plates:
                    if characteristic in combo_plate.drink.characteristics or characteristic in combo_plate.protein.characteristics or characteristic in combo_plate.side_dish.characteristics or characteristic in combo_plate.dessert.characteristics:
                        rowPosition = self.combo_platesTable.rowCount()
                        self.combo_platesTable.insertRow(rowPosition)

                        self.combo_platesTable.setItem(rowPosition, 0, QTableWidgetItem(str(combo_plate.id)))
                        self.combo_platesTable.setItem(rowPosition, 1, QTableWidgetItem(combo_plate.name))
                        self.combo_platesTable.setItem(rowPosition, 2, QTableWidgetItem(f"${combo_plate.price / 100:.2f}"))
                        self.combo_platesTable.setItem(rowPosition, 3, QTableWidgetItem(str(combo_plate.calories)))
                        self.combo_platesTable.setItem(rowPosition, 4, QTableWidgetItem(combo_plate.drink.name))
                        self.combo_platesTable.setItem(rowPosition, 5, QTableWidgetItem(combo_plate.protein.name))
                        self.combo_platesTable.setItem(rowPosition, 6, QTableWidgetItem(combo_plate.side_dish.name))
                        self.combo_platesTable.setItem(rowPosition, 7, QTableWidgetItem(combo_plate.dessert.name))
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado una caracteristica")

    # Método para popular la tabla combo según el contenido del nombre
    def populate_combo_table_by_name(self) -> None:

        # Se obtienen los combos de la memoria
        combo_plates = self.combo_platesData

        # Se limpia la tabla
        self.combo_platesTable.setRowCount(0)

        dialog = SearchComboByNameWindow()

        try:

            if dialog.exec() == QDialog.Accepted:

                # Se obtiene el contenido del nombre
                name = dialog.get_name()

                normalized_name_input = name.lower()

                # Se agregan los combos a la tabla
                for combo_plate in combo_plates:
                    normalized_name = combo_plate.name.lower()

                    # se debe validar si el nombre desde el dialogo esta contenido en el nombre del combo
                    if normalized_name_input in normalized_name:
                        rowPosition = self.combo_platesTable.rowCount()
                        self.combo_platesTable.insertRow(rowPosition)

                        self.combo_platesTable.setItem(rowPosition, 0, QTableWidgetItem(str(combo_plate.id)))
                        self.combo_platesTable.setItem(rowPosition, 1, QTableWidgetItem(combo_plate.name))
                        self.combo_platesTable.setItem(rowPosition, 2, QTableWidgetItem(f"${combo_plate.price / 100:.2f}"))
                        self.combo_platesTable.setItem(rowPosition, 3, QTableWidgetItem(str(combo_plate.calories)))
                        self.combo_platesTable.setItem(rowPosition, 4, QTableWidgetItem(combo_plate.drink.name))
                        self.combo_platesTable.setItem(rowPosition, 5, QTableWidgetItem(combo_plate.protein.name))
                        self.combo_platesTable.setItem(rowPosition, 6, QTableWidgetItem(combo_plate.side_dish.name))
        except:
            QMessageBox.warning(self, "Error", "No se ha dado un nombre o contenido del nombre")
    # endregion

    # Método para agregar un combo
    def add_combo(self) -> None:

        try:
            dialog = AddComboWindow(self.inventoryData)
            inventoryData = self.inventoryData

            if dialog.exec() == QDialog.Accepted:
                name = dialog.get_name()
                price = dialog.get_price()
                calories = dialog.get_calories()
                drink = dialog.get_drink()
                protein = dialog.get_protein()
                side_dish = dialog.get_side_dish()
                dessert = dialog.get_dessert()

                # Del inventario se obtienen los elementos para el combo
                drink_temp = inventoryData.food_elements[drink]
                protein_temp = inventoryData.food_elements[protein]
                side_dish_tem = inventoryData.food_elements[side_dish]
                dessert_tem = inventoryData.food_elements[dessert]

                # Se crea el combo
                # Chequear cual es el id del ultimo combo
                id = self.combo_platesData[-1].id + 1
                combo_plate = ComboPlateFactory.create_combo_plate(id=id, name=name, price=price, calories=calories, drink=drink_temp, protein=protein_temp, side_dish=side_dish_tem, dessert=dessert_tem)
                self.combo_platesData.append(combo_plate)

                # Guardar el combo en la base de datos
                conn: sqlite3.Connection = sqlite3.connect("restaurante.db")
                cursor: sqlite3.Cursor = conn.cursor()
                cursor.execute("INSERT INTO ComboPlates(name, price, calories, drink_name, protein_name, side_dish_name, dessert_name) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, price, calories, drink, protein, side_dish, dessert))
                conn.commit()
                conn.close()

                # Actualizar la tabla de combos
                self.populate_combo_table()
        except:
            QMessageBox.warning(self, "Error", "No se ha podido agregar el combo intentalo de nuevo")

    # Método para modificar un combo
    def modify_combo(self) -> None:

        try:
            # Obtener el combo seleccionado
            selected_combo = self.combo_platesTable.selectedItems()
            selected_combo_id = int(selected_combo[0].text())

            # Obtener el combo de la memoria
            if selected_combo_id is not None:
                combo_plate = self.find_combo_plate_by_id(selected_combo_id)	
            else:
                QMessageBox.warning(self, "Error", "No se ha seleccionado un combo")

            dialog = ModifyComboWindow(combo_plate, self.inventoryData)

            if dialog.exec() == QDialog.Accepted:
                name = dialog.get_name()
                price = dialog.get_price()
                calories = dialog.get_calories()
                drink = dialog.get_drink()
                protein = dialog.get_protein()
                side_dish = dialog.get_side_dish()
                dessert = dialog.get_dessert()

                # Del inventario se obtienen los elementos para el combo
                drink_temp = self.inventoryData.food_elements[drink]
                protein_temp = self.inventoryData.food_elements[protein]
                side_dish_tem = self.inventoryData.food_elements[side_dish]
                dessert_tem = self.inventoryData.food_elements[dessert]

                # Se modifica el combo
                combo_plate.name = name
                combo_plate.price = price
                combo_plate.calories = calories
                combo_plate.drink = drink_temp
                combo_plate.protein = protein_temp
                combo_plate.side_dish = side_dish_tem
                combo_plate.dessert = dessert_tem

                # Actualizar el combo en la base de datos
                conn: sqlite3.Connection = sqlite3.connect("restaurante.db")
                cursor: sqlite3.Cursor = conn.cursor()
                cursor.execute("UPDATE ComboPlates SET name = ?, price = ?, calories = ?, drink_name = ?, protein_name = ?, side_dish_name = ?, dessert_name = ? WHERE id = ?", (name, price, calories, drink, protein, side_dish, dessert, selected_combo_id))
                conn.commit()
                conn.close()

                # Actualizar la tabla de combos
                self.populate_combo_table()
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado la id un combo")
        
    # Método para eliminar un combo
    def delete_combo(self) -> None:
        try:
            # Obtener el combo seleccionado
            selected_combo = self.combo_platesTable.selectedItems()
            selected_combo_id = int(selected_combo[0].text())

            # Chequear si existe el combo
            if selected_combo_id is not None:
                combo_plate = self.find_combo_plate_by_id(selected_combo_id)
                self.combo_platesData.remove(combo_plate)

                # Eliminar el combo de la base de datos
                conn: sqlite3.Connection = sqlite3.connect("restaurante.db")
                cursor: sqlite3.Cursor = conn.cursor()
                cursor.execute("DELETE FROM ComboPlates WHERE id = ?", (selected_combo_id,))
                conn.commit()
                conn.close()

                # Actualizar la tabla de combos
                self.populate_combo_table()
            else:
                QMessageBox.warning(self, "Error", "No se ha seleccionado la id de un combo")
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado la id un combo")

    # Método para encontrar un combo por id
    def find_combo_plate_by_id(self, id: int) -> ComboPlate:
        for combo_plate in self.combo_platesData:
            if combo_plate.id == id:
                return combo_plate
        return None
    