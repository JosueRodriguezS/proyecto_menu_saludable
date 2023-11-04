import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QFont
from modules.ordenes import Order, Payment, Table, OrderLog, PaymentLog

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

        # Inicializamos la ventana
        self.setWindowTitle("Ordenes y Pagos")
        self.setGeometry(100, 100, 1200, 1000)

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

        # Botones para agregar platos a la orden
        self.combo_button = QPushButton("Agregar Combo", self)
        self.combo_button.setGeometry(20, 270, 150, 30)
        #self.combo_button.clicked.connect(self.add_combo)

        self.saludable_button = QPushButton("Agregar Menu Saludable", self)
        self.saludable_button.setGeometry(190, 270, 150, 30)
        #self.saludable_button.clicked.connect(self.add_saludable)

        # Tabla de platillos de la orden
        self.order_label = QLabel("Orden:", self)
        

    """
        self.order_label = QLabel("Orden:", self)
        self.order_label.setGeometry(20, 220, 150, 20)
        # Obtener los combos para agregarlos al menu de ordenes
        self.menu_combo_items = []
        for combo_plate in self.combo_platesData:
            self.menu_combo_items.append(combo_plate.name + " " + combo_plate.drink.name + " " + combo_plate.protein.name + " " + combo_plate.side_dish.name + " " + combo_plate.dessert.name + " " + str(combo_plate.price) + " " + str(combo_plate.calories))
        self.menu_combo_checkboxes = []
        for i in range(len(self.menu_combo_items)):
            checkbox = QCheckBox(self.menu_combo_items[i], self)
            checkbox.setGeometry(20, 240 + i * 20, 750, 20)
            self.menu_combo_checkboxes.append(checkbox)
        # Obtener los platos saludables al menu de ordenes
        self.menu_saludable_items = []
        for menu_saludable in self.menu_saludablesData:
            self.menu_saludable_items.append(menu_saludable.name + " " + str(menu_saludable.price) + " " + str(menu_saludable.calories))
        self.menu_saludable_checkboxes = []
        for i in range(len(self.menu_saludable_items)):
            checkbox = QCheckBox(self.menu_saludable_items[i], self)
            checkbox.setGeometry(20, 240 + (i + len(self.menu_combo_items)) * 20, 750, 20)
            self.menu_saludable_checkboxes.append(checkbox)

        # Cerrar orden
        self.close_order_button = QPushButton("Cerrar Orden", self)
        self.close_order_button.setGeometry(20, 250, 150, 30)
        self.close_order_button.clicked.connect(self.close_order)


    def close_order(self):
        # Aquí debes implementar la lógica para cerrar la orden.
        # Esto incluiría registrar los platos seleccionados, detalles de la mesa, etc.
        # Una vez que se cierra la orden, ya no se pueden realizar modificaciones.
        pass
    """