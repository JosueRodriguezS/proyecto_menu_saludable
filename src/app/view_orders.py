import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QFont
from modules.ordenes import Order, Payment, Table, OrderLog, PaymentLog
from modules.menuSaludable import MenuSaludable
from datetime import datetime
import random

class OrderPaymentWindow(QWidget):
    def __init__(self, restaurant_model) -> None:
        super().__init__()

        # Inicializamos el modelo del restaurante
        self.restaurant_model = restaurant_model
        # Inicializamos las mesas, los logs, platisllos y el inventario
        self.tablesData = restaurant_model.tables
        self.order_log = restaurant_model.order_log
        self.payment_log = restaurant_model.payment_log
        self.combo_platesData = restaurant_model.combo_plates
        self.menu_saludablesData = restaurant_model.menu_saludables
        self.inventoryData = restaurant_model.inventory

        # Inicializar lista en la que se van a guardar los platillos de una orden en construcción
        self.order_plates = []

        # Inicializamos la ventana
        self.setWindowTitle("Ordenes y Pagos")
        self.setGeometry(100, 100, 1700, 1000)

        # Registro de ordenes
        self.title_label = QLabel("Registro de Ordenes", self)
        fontTitle = QFont()
        fontTitle.setPointSize(14)
        fontTitle.setBold(True)
        self.title_label.setFont(fontTitle)
        self.title_label.setGeometry(20, 20, 200, 40)
        
        self.table_label = QLabel("Numero de mesa:", self)
        self.table_label.setGeometry(20, 70, 150, 20)

        self.table_input = QLineEdit(self)
        self.table_input.setGeometry(180, 70, 100, 20)

        self.customer_name_annotation = QLabel("(NOTA: En el caso de más de un cliente: separar los nombres por ',')", self)
        font = QFont()
        # ajustar tamaño de la fuente.
        font.setPointSize(6)
        font.setBold(True)
        self.customer_name_annotation.setFont(font)
        self.customer_name_annotation.setGeometry(180, 100, 350, 20)

        self.customer_name_label = QLabel("Nombre del Cliente:", self)
        self.customer_name_label.setGeometry(20, 115, 200, 20)

        self.customer_name_input = QLineEdit(self)
        self.customer_name_input.setGeometry(180, 115, 200, 20)

        self.payment_label = QLabel("Método de Pago:", self)
        self.payment_label.setGeometry(20, 150, 150, 20)

        self.payment_group = QButtonGroup(self)

        self.single_payment = QRadioButton("Pago Único", self)
        self.single_payment.setGeometry(20, 170, 150, 20)
        self.single_payment.setChecked(True)
        self.payment_group.addButton(self.single_payment)

        self.per_person_payment = QRadioButton("Pago por Persona", self)
        self.per_person_payment.setGeometry(20, 190, 150, 20)
        self.payment_group.addButton(self.per_person_payment)

        self.number_of_customers_label = QLabel("Número de Clientes:", self)
        self.number_of_customers_label.setGeometry(20, 230, 150, 20)
        self.number_of_customers_text = QLineEdit(self)
        self.number_of_customers_text.setGeometry(180, 230, 100, 20)

        self.payment_method_label = QLabel("Método de Pago:", self)
        self.payment_method_label.setGeometry(20, 270, 150, 20)
        self.payment_method_combo = QComboBox(self)
        self.payment_method_combo.setGeometry(180, 270, 100, 20)
        self.payment_method_combo.addItem("Efectivo")
        self.payment_method_combo.addItem("No Efectivo")

        # Botones para agregar platos a la orden
        self.combo_button = QPushButton("Agregar Combo", self)
        self.combo_button.setGeometry(20, 320, 150, 30)
        self.combo_button.clicked.connect(self.add_combo)

        self.saludable_button = QPushButton("Agregar Menu Saludable", self)
        self.saludable_button.setGeometry(190, 320, 150, 30)
        self.saludable_button.clicked.connect(self.add_saludable)

        #Boton para eliminar platos de la orden
        self.delete_button = QPushButton("Eliminar Plato", self)
        self.delete_button.setGeometry(360, 320, 150, 30)
        self.delete_button.clicked.connect(self.delete_plate)

        # Tabla de platillos de la orden
        self.order_label = QLabel("Orden:", self)
        self.order_label.setGeometry(20, 400, 150, 20)
        self.order_table = QTableWidget(self)
        self.order_table.setGeometry(20, 370, 750, 200)
        self.order_table.setColumnCount(7)
        self.order_table.setHorizontalHeaderLabels(["Nombre", "Precio", "Calorias", "Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # boton cerrar orden
        self.close_order_button = QPushButton("Cerrar Orden", self)
        self.close_order_button.setGeometry(20, 590, 150, 30)
        self.close_order_button.clicked.connect(self.close_order)

        # Tabla que muestra ordenes existentes
        self.order_log_label = QLabel("Ordenes Existentes:", self)
        self.order_log_label.setGeometry(20, 630, 150, 20)
        self.order_log_table = QTableWidget(self)
        self.order_log_table.setGeometry(20, 650, 750, 200)
        self.order_log_table.setColumnCount(5)
        self.order_log_table.setHorizontalHeaderLabels(["Fecha", "Numero de Mesa", "Nombre del Cliente", "Estado", "Platos"])
        self.order_log_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_log_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate_order_log_table()
        
        # Tabla de combos a elegir
        self.combo_label = QLabel("Combos:", self)
        self.combo_label.setGeometry(800, 20, 150, 20)
        self.combo_table = QTableWidget(self)
        self.combo_table.setGeometry(800, 40, 750, 200)
        self.combo_table.setColumnCount(7)
        self.combo_table.setHorizontalHeaderLabels(["Nombre", "Precio", "Calorias", "Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.combo_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.combo_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.populate_combo_table_no_id()

        # Tabla de menu saludables a elegir
        self.saludable_label = QLabel("Menus Saludables:", self)
        self.saludable_label.setGeometry(800, 270, 150, 20)
        self.saludable_table = QTableWidget(self)
        self.saludable_table.setGeometry(800, 290, 750, 200)
        self.saludable_table.setColumnCount(7)
        self.saludable_table.setHorizontalHeaderLabels(["Nombre", "Precio", "Calorias", "Bebida", "Proteina", "Acompañamiento", "Postre"])
        self.saludable_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.saludable_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.populate_saludable_table_no_id()

        # Boton para generar nuevos menus saludables
        self.generate_saludable_button = QPushButton("Generar Menus Saludables", self)
        self.generate_saludable_button.setGeometry(800, 500, 350, 30)
        self.generate_saludable_button.clicked.connect(self.generate_saludable)
        

        # Tabla de los pagos
        self.payment_log_label = QLabel("Pagos:", self)
        self.payment_log_label.setGeometry(800, 630, 150, 20)
        self.payment_log_table = QTableWidget(self)
        self.payment_log_table.setGeometry(800, 650, 750, 200)
        self.payment_log_table.setColumnCount(6)
        self.payment_log_table.setHorizontalHeaderLabels(["Fecha","Id","Orden", "Es efectivo", "Monto", "Estado"])
        self.payment_log_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.payment_log_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate_payment_log_table()

        # Boton para finalizar un pago/factura
        self.close_payment_button = QPushButton("Cerrar Pago", self)
        self.close_payment_button.setGeometry(800, 590, 150, 30)
        self.close_payment_button.clicked.connect(self.close_payment)

    # Metodo para crear una orden
    """
    Se extraen los datos de la interfaz gráfica y se crea un objeto Order.
    Se debe de validar que los datos sean correctos.
    """
    def create_order(self) -> None:
        # Obtener el número de mesa
        try:
            table_number = int(self.table_input.text())
        except:
            QMessageBox.warning(self, "Error", "El número de mesa debe ser un número entero", QMessageBox.Ok)
            return
        
        # Obtener el nombre del cliente
        try:
            customer_name = str(self.customer_name_input.text())
        except:
            QMessageBox.warning(self, "Error", "El nombre del cliente debe ser un texto", QMessageBox.Ok)
            return
        
        # Obtener platillos de la orden
        if len(self.order_plates) == 0:
            QMessageBox.warning(self, "Error", "La orden debe tener al menos un platillo", QMessageBox.Ok)
            return
        else:
            order_plates = self.order_plates
        
        # Crear el objeto Order
        order = Order(table_number=table_number, customers_name=customer_name, status="Lista")

        # Agregar los platillos a la orden
        for plate in order_plates:
            order.add_dish(plate)

        # Se retorna el objeto Order
        return order

    def close_order(self) -> None:
        """ 
        Esto incluiría registrar los platos seleccionados, detalles de la mesa, etc.
        Una vez que se cierra la orden, ya no se pueden realizar modificaciones.
        Al cerrar una orden, se debe de crear un objeto Order y agregarlo al log de ordenes.
        Se deben generar los pagos correspondientes a la orden.
        """
        # hay que chequear que el numero de clientes no este vacio o sea un entero
        if self.number_of_customers_text.text() == "":
            QMessageBox.warning(self, "Error", "El número de clientes no puede estar vacío", QMessageBox.Ok)
            return
        try:
            int(self.number_of_customers_text.text())
        except:
            QMessageBox.warning(self, "Error", "El número de clientes debe ser un número entero", QMessageBox.Ok)
            return
        
        #region Crear objeto Order
        order = self.create_order()
        if order is None:
            return
        #endregion

        #Lista de pagos que se van a generar
        payments = []

        #region Crear objeto Payment
        if self.single_payment.isChecked():
            # Se agrega la orden a una lista para poder agregarla al pago
            orders = []
            orders.append(order)
            is_cash = True if self.payment_method_combo.currentText() == "Efectivo" else False
            payment = Payment(orders=orders, is_cash=is_cash)
            payments.append(payment)
        else:
            #Es necesario generar un pago por cada cliente y plato
            #Primero validamos que el número de clientes y el número de platos sea el mismo
            if len(order.dishes) != int(self.number_of_customers_text.text()):
                QMessageBox.warning(self, "Error", "El número de clientes debe ser igual al número de platos", QMessageBox.Ok)
                return
            else:        
                # optenemos los nombres de los clientes al separar el string por comas
                customers_names = self.customer_name_input.text().split(",")
                # Se crea una lista de ordenes para cada cliente el cliente del indice i tiene el plato del indice i
                orders = []
                for i in range(len(customers_names)):
                    order_temp = Order(table_number=order.table_number, customers_name=customers_names[i], status="Lista")
                    order_temp.add_dish(order.dishes[i])
                    orders.append(order_temp)
                # Se crea una lista de pagos
                payments = []

                # Se crea un pago por cada cliente
                for i in range(len(customers_names)):
                    is_cash = True if self.payment_method_combo.currentText() == "Efectivo" else False
                    payment = Payment(orders=[orders[i]], is_cash=is_cash)
                    payments.append(payment)
        #endregion

        #region de actualizar la mesa
        # Se obtiene la mesa
        table = self.tablesData[order.table_number]
        # Se actualiza el order_log de la mesa
        table.add_order(order)
        self.populate_order_log_table()
        # Se actualiza el payment_log de la mesa
        for payment in payments:
            table.add_payment(payment)
        self.populate_payment_log_table()
        # Se actualiza el numero de clientes de la mesa
        table.edit_number_of_customers(int(self.number_of_customers_text.text()))
        # Se actualiza si es single_bill o no
        table.edit_single_bill(self.single_payment.isChecked())
        # Se actualiza el status de la mesa
        table.edit_status("Ocupada")
        #endregion

        # Se devuelve la mesa actualizada a la lista de mesas
        self.tablesData[order.table_number] = table

    # Metodo para el boton cerrar pago
    def close_payment(self) -> None:
        """
        Este es el método que permite cerrar/pagar un pago. 
        El método permite que un pago seleccionado cambie su estado de No exitoso a Exitoso.
        Se debe validar que el usuario haya seleccionado un pago y el pago sea no exitoso.
        """
        # Obtenemos el pago al que se le va a cambiar el estado
        selected_payment_row = self.payment_log_table.currentRow()

        # Se valida que se haya seleccionado un pago
        if selected_payment_row == -1:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un pago", QMessageBox.Ok)
            return

        # Obtenemos el ID del pago seleccionado
        selected_payment_id = self.payment_log_table.item(selected_payment_row, 1).text()

        # Buscamos el pago correspondiente en el historial de pagos
        selected_payment = None
        for date, payments in self.payment_log.payment_history.items():
            for payment in payments:
                if payment.id == selected_payment_id:
                    selected_payment = payment
                    break

        # Validamos que el pago se haya encontrado
        if selected_payment is None:
            QMessageBox.warning(self, "Error", "No se encontró el pago seleccionado", QMessageBox.Ok)
            return

        # Obtenemos el estado del pago seleccionado
        selected_payment_status = self.payment_log_table.item(selected_payment_row, 4).text()

        # Se valida que el pago sea no exitoso
        if selected_payment_status == "Exitoso":
            QMessageBox.warning(self, "Error", "El pago seleccionado ya es exitoso", QMessageBox.Ok)
            return

        # Se cambia el estado del pago a exitoso
        selected_payment.change_status(True)

        # No necesitas actualizar el diccionario, ya que el pago en la lista se ha modificado directamente
        self.populate_payment_log_table()

    # para testeos
    def generate_saludable(self) -> None:
        # Se obtiene el inventario
        inventory = self.inventoryData

        # Se obtiene la lista de menus saludables
        menu_saludables = self.menu_saludablesData

        dialog = menu_salusable(menu_saludables, inventory)

        if dialog.exec() == QDialog.Accepted:

            # Se obtienen las caracteristicas de los platillos
            if dialog.get_drink_characteristic() == "" or dialog.get_protein_characteristic() == "" or dialog.get_side_dish_characteristic() == "" or dialog.get_dessert_characteristic() == "":
                QMessageBox.warning(self, "Error", "Las caracteristicas no pueden estar vacias", QMessageBox.Ok)
                return
            
            drink_characteristic = dialog.get_drink_characteristic()
            protein_characteristic = dialog.get_protein_characteristic()
            side_dish_characteristic = dialog.get_side_dish_characteristic()
            dessert_characteristic = dialog.get_dessert_characteristic()

            print(drink_characteristic, protein_characteristic, side_dish_characteristic, dessert_characteristic)

            # Se va a generar todas las combinaciones posibles de food_elements que cumplan con las caracteristicas
            # Se obtienen las bebidas que cumplen con la caracteristica
            drinks = [drink for drink in inventory.food_elements.values() if drink.food_type == "bebida" and drink_characteristic in drink.characteristics]
            # Se obtienen las proteinas que cumplen con la caracteristica
            proteins = [protein for protein in inventory.food_elements.values() if protein.food_type == "proteina" and protein_characteristic in protein.characteristics]
            # Se obtienen los acompañamientos que cumplen con la caracteristica
            side_dishes = [side_dish for side_dish in inventory.food_elements.values() if side_dish.food_type == "acompanamiento" and side_dish_characteristic in side_dish.characteristics]
            # Se obtienen los postres que cumplen con la caracteristica
            desserts = [dessert for dessert in inventory.food_elements.values() if dessert.food_type == "postre" and dessert_characteristic in dessert.characteristics]

            # Se crea una lista de todos los menus saludables que se pueden generar
            new_menu_saludables = []

            # Se generan 5 menus saludables escogiendo una combinacion aleatoria de drink, protein, side_dish y dessert
            for i in range(5):
  
                drink = drinks[random.randint(0, len(drinks) - 1)]
                protein = proteins[random.randint(0, len(proteins) - 1)]
                side_dish = side_dishes[random.randint(0, len(side_dishes) - 1)]
                dessert = desserts[random.randint(0, len(desserts) - 1)]

                # Se crea el menu saludable
                new_menu_saludable = MenuSaludable(id=len(menu_saludables) + len(new_menu_saludables),
                                                   name= f"Menu Saludable {len(menu_saludables) + len(new_menu_saludables)}",
                                                    price=drink.price + protein.price + side_dish.price + dessert.price,
                                                    calories=drink.calories + protein.calories + side_dish.calories + dessert.calories,
                                                    drink=drink,
                                                    protein=protein,
                                                    side_dish=side_dish,
                                                    dessert=dessert)
                # Se agrega el menu saludable a la lista de menus saludables
                new_menu_saludables.append(new_menu_saludable)

            # Se agregan los nuevos menús saludables que no se encuentren en la lista de menús saludables
            for new_menu_saludable in new_menu_saludables:
                if new_menu_saludable not in menu_saludables:
                    menu_saludables.append(new_menu_saludable)

            # Se actualiza la tabla de menus saludables
            self.populate_saludable_table_no_id()

    def add_combo(self) -> None:
        # usar try except para evitar que se caiga el programa si no se selecciona una fila
        try:
            # Obtener nombre del combo seleccionado
            selected_combo_name = self.combo_table.selectedItems()[0].text()
            # Buscar el combo seleccionado en la lista de combos
            selected_combo = next(combo for combo in self.combo_platesData if combo.name == selected_combo_name)
            # Actualizar la lista de platos de la orden
            self.order_plates.append(selected_combo)

            self.populate_order_table()
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un combo", QMessageBox.Ok)

    def add_saludable(self) -> None:
        try:
            selected_saludable_name = self.saludable_table.selectedItems()[0].text()
            selected_saludable = next(saludable for saludable in self.menu_saludablesData if saludable.name == selected_saludable_name)
            self.order_plates.append(selected_saludable)
            self.populate_order_table()
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un menu saludable", QMessageBox.Ok)

    def delete_plate(self) -> None:
        try:
            selected_plate_name = self.order_table.selectedItems()[0].text()
            selected_plate = next(plate for plate in self.order_plates if plate.name == selected_plate_name)
            self.order_plates.remove(selected_plate)
            self.populate_order_table()
        except:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un plato", QMessageBox.Ok)

    def populate_order_table(self) -> None:
        # Se puebla la tabla de ordenes con los platos de la orden
        self.order_table.setRowCount(len(self.order_plates))
        
        for i, plate in enumerate(self.order_plates):
            self.order_table.setItem(i, 0, QTableWidgetItem(plate.name))
            self.order_table.setItem(i, 1, QTableWidgetItem(str(plate.price)))
            self.order_table.setItem(i, 2, QTableWidgetItem(str(plate.calories)))
            self.order_table.setItem(i, 3, QTableWidgetItem(plate.drink.name))
            self.order_table.setItem(i, 4, QTableWidgetItem(plate.protein.name))
            self.order_table.setItem(i, 5, QTableWidgetItem(plate.side_dish.name))
            self.order_table.setItem(i, 6, QTableWidgetItem(plate.dessert.name))

    def populate_combo_table_no_id(self) -> None:

        combo_plates = self.combo_platesData
        
        self.combo_table.setRowCount(len(combo_plates))

        for i, combo_plate in enumerate(combo_plates):
            self.combo_table.setItem(i, 0, QTableWidgetItem(combo_plate.name))
            self.combo_table.setItem(i, 1, QTableWidgetItem(str(combo_plate.price)))
            self.combo_table.setItem(i, 2, QTableWidgetItem(str(combo_plate.calories)))
            self.combo_table.setItem(i, 3, QTableWidgetItem(combo_plate.drink.name))
            self.combo_table.setItem(i, 4, QTableWidgetItem(combo_plate.protein.name))
            self.combo_table.setItem(i, 5, QTableWidgetItem(combo_plate.side_dish.name))
            self.combo_table.setItem(i, 6, QTableWidgetItem(combo_plate.dessert.name))

    def populate_saludable_table_no_id(self) -> None:

        menu_saludables = self.menu_saludablesData
        
        self.saludable_table.setRowCount(len(menu_saludables))

        for i, menu_saludable in enumerate(menu_saludables):
            self.saludable_table.setItem(i, 0, QTableWidgetItem(menu_saludable.name))
            self.saludable_table.setItem(i, 1, QTableWidgetItem(str(menu_saludable.price)))
            self.saludable_table.setItem(i, 2, QTableWidgetItem(str(menu_saludable.calories)))
            self.saludable_table.setItem(i, 3, QTableWidgetItem(menu_saludable.drink.name))
            self.saludable_table.setItem(i, 4, QTableWidgetItem(menu_saludable.protein.name))
            self.saludable_table.setItem(i, 5, QTableWidgetItem(menu_saludable.side_dish.name))
            self.saludable_table.setItem(i, 6, QTableWidgetItem(menu_saludable.dessert.name))

    def populate_order_log_table(self) -> None:
            # Limpiar la tabla existente
        self.order_log_table.setRowCount(0)
        
        # Recorrer el historial de órdenes y agregar las órdenes a la tabla
        for date, orders in self.order_log.order_history.items():
            for order in orders:
                # Obtener detalles de la orden en una cadena
                order_details = ""
                for dish in order.dishes:
                    order_details += f"{dish.name}, "
                order_details = order_details.rstrip(", ")
                
                # Agregar la orden a la tabla
                row_position = self.order_log_table.rowCount()
                self.order_log_table.insertRow(row_position)
                self.order_log_table.setItem(row_position, 0, QTableWidgetItem(date.strftime("%Y-%m-%d")))
                self.order_log_table.setItem(row_position, 1, QTableWidgetItem(str(order.table_number)))
                self.order_log_table.setItem(row_position, 2, QTableWidgetItem(order.customers_name))
                self.order_log_table.setItem(row_position, 3, QTableWidgetItem(order.status))
                self.order_log_table.setItem(row_position, 4, QTableWidgetItem(order_details))

    def populate_payment_log_table(self) -> None:   
        # Limpiar la tabla existente
        self.payment_log_table.setRowCount(0)

        # Recorrer el historial de pagos y agregar los pagos a la tabla
        for date, payments in self.payment_log.payment_history.items():
            for payment in payments:
                # Obtener detalles del pago en una cadena
                payment_id = payment.id
                orders_info = ", ".join([f"{order.table_number} ({order.customers_name})" for order in payment.orders])
                payment_details = f"{'Efectivo' if payment.is_cash else 'No Efectivo'}"
                payment_status = 'Exitoso' if payment.status else 'No Exitoso'

                # Agregar el pago a la tabla
                row_position = self.payment_log_table.rowCount()
                self.payment_log_table.insertRow(row_position)
                self.payment_log_table.setItem(row_position, 0, QTableWidgetItem(date.strftime("%Y-%m-%d")))
                self.payment_log_table.setItem(row_position, 1, QTableWidgetItem(payment_id))
                self.payment_log_table.setItem(row_position, 2, QTableWidgetItem(orders_info))
                self.payment_log_table.setItem(row_position, 3, QTableWidgetItem(payment_details))
                self.payment_log_table.setItem(row_position, 4, QTableWidgetItem(str(payment.billing_amount)))
                self.payment_log_table.setItem(row_position, 5, QTableWidgetItem(payment_status))

# clase para generar los nuevos menus saludables
class menu_salusable(QDialog):
    def __init__(self, menus_saludables, inventory) -> None:
        super().__init__()

        self.setWindowTitle("Generar Menus Saludables")
        self.setGeometry(100, 100, 1000, 700)

        layout = QVBoxLayout()

        self.title_label = QLabel("Generar Menus Saludables")
        fontTitle = QFont()
        fontTitle.setPointSize(14)
        fontTitle.setBold(True)
        self.title_label.setFont(fontTitle)
        self.title_label.setGeometry(20, 20, 300, 40)
        layout.addWidget(self.title_label)

        # Label y espacio de la caracteristica de la bebida
        self.drink_label = QLabel("Bebida:")
        self.drink_label.setGeometry(20, 70, 150, 20)
        self.drink_input = QComboBox()
        self.drink_input.addItems(inventory.get_all_drinks_characteristics())
        self.drink_input.setGeometry(180, 70, 100, 20)
        layout.addWidget(self.drink_label)
        layout.addWidget(self.drink_input)

        # Label y espacio de la caracteristica de la proteina
        self.protein_label = QLabel("Proteina:")
        self.protein_label.setGeometry(20, 110, 150, 20)
        self.protein_input = QComboBox()
        self.protein_input.addItems(inventory.get_all_proteins_characteristics())
        self.protein_input.setGeometry(180, 110, 100, 20)
        layout.addWidget(self.protein_label)
        layout.addWidget(self.protein_input)

        # Label y espacio de la caracteristica del acompañamiento
        self.side_dish_label = QLabel("Acompañamiento:")
        self.side_dish_label.setGeometry(20, 150, 150, 20)
        self.side_dish_input = QComboBox()
        self.side_dish_input.addItems(inventory.get_all_side_dishes_characteristics())
        self.side_dish_input.setGeometry(180, 150, 100, 20)
        layout.addWidget(self.side_dish_label)
        layout.addWidget(self.side_dish_input)

        # Label y espacio de la caracteristica del postre
        self.dessert_label = QLabel("Postre:")
        self.dessert_label.setGeometry(20, 190, 150, 20)
        self.dessert_input = QComboBox()
        self.dessert_input.addItems(inventory.get_all_desserts_characteristics())
        self.dessert_input.setGeometry(180, 190, 100, 20)
        layout.addWidget(self.dessert_label)
        layout.addWidget(self.dessert_input)

        # Botono para generar los menus saludables
        self.generate_button = QPushButton("Generar", self)
        self.generate_button.setGeometry(20, 230, 150, 30)
        self.generate_button.clicked.connect(self.accept)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    # Metodo para obtener la caracteristica de la bebida
    def get_drink_characteristic(self) -> str:
        return self.drink_input.currentText()
    
    # Metodo para obtener la caracteristica de la proteina
    def get_protein_characteristic(self) -> str:
        return self.protein_input.currentText()
    
    def get_side_dish_characteristic(self) -> str:
        return self.side_dish_input.currentText()
    
    def get_dessert_characteristic(self) -> str:
        return self.dessert_input.currentText()