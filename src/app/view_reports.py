import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from functools import reduce
from collections import Counter
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QVBoxLayout, QLabel, QDialog, QDateEdit
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from modules.inventario import FoodElement
from modules.plato import ComboPlate
from modules.menuSaludable import MenuSaludable

# clase para el grafico de combos
class ComboStatsWindow(QDialog):
    def __init__(self, top_drink, top_protein, top_side, top_dessert) -> None:
        super().__init__()

        # Inicializa la ventana
        self.setWindowTitle("Estadísticas de combos")
        self.setGeometry(100, 100, 1700, 1000)

         # Crea el gráfico de barras
        self.create_bar_chart(top_drink, top_protein, top_side, top_dessert)
    
    def create_bar_chart(self, top_drink, top_protein, top_side, top_dessert):
        # Desempaqueta los elementos más solicitados y sus cantidades
        (drink_name, drink_count), (protein_name, protein_count), (side_name, side_count), (dessert_name, dessert_count) = top_drink, top_protein, top_side, top_dessert

        categories = [drink_name, protein_name, side_name, dessert_name]
        counts = [drink_count, protein_count, side_count, dessert_count]

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.bar(categories, counts)
        ax.set_xlabel('Categoría')
        ax.set_ylabel('Cantidad')
        ax.set_title('Productos Más Solicitados')

        # Anota los nombres de los elementos en el gráfico
        for i in range(len(categories)):
            ax.annotate(f'{categories[i]}: {counts[i]}', (categories[i], counts[i]), textcoords="offset points", xytext=(0, 10), ha='center')

        # Crea el gráfico de barras y lo muestra
        canvas = FigureCanvas(fig)

        # Agrega el widget de matplotlib al layout
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)

# Clase para el grafico de menu saludable
class HealthyMenuStatsWindow(QDialog):
    def __init__(self, top_drink, top_protein, top_side, top_dessert) -> None:
        super().__init__()

        # Inicializa la ventana
        self.setWindowTitle("Estadísticas de combos")
        self.setGeometry(100, 100, 1700, 1000)

         # Crea el gráfico de barras
        self.create_bar_chart(top_drink, top_protein, top_side, top_dessert)

    def create_bar_chart(self, top_drink, top_protein, top_side, top_dessert):
        # Desempaqueta los elementos más solicitados y sus cantidades
        (drink_name, drink_count), (protein_name, protein_count), (side_name, side_count), (dessert_name, dessert_count) = top_drink, top_protein, top_side, top_dessert

        categories = [drink_name, protein_name, side_name, dessert_name]
        counts = [drink_count, protein_count, side_count, dessert_count]

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.bar(categories, counts)
        ax.set_xlabel('Categoría')
        ax.set_ylabel('Cantidad')
        ax.set_title('Productos Más Solicitados')

        # Anota los nombres de los elementos en el gráfico
        for i in range(len(categories)):
            ax.annotate(f'{categories[i]}: {counts[i]}', (categories[i], counts[i]), textcoords="offset points", xytext=(0, 10), ha='center')

        # Crea el gráfico de barras y lo muestra
        canvas = FigureCanvas(fig)

        # Agrega el widget de matplotlib al layout
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)

# Clase para la ventana de reportes d
class ReportWindows(QWidget):
    def __init__(self, restaurant_model) -> None:
        super().__init__()

        # Inicializamos el modelo del restaurante
        self.restaurant_model = restaurant_model

        # Inicializamos los logs
        self.order_log = self.restaurant_model.order_log
        self.payment_log = self.restaurant_model.payment_log

        # Inicializamos la ventana
        self.setWindowTitle("Reportes")
        self.setGeometry(100, 100, 1700, 1000)

        # Los elementos para los reportes de las ordenes
        self.order_report_label = QLabel("Reporte de ordenes", self)
        self.order_report_label.move(10, 10)
        self.order_report_label.setFont(QFont('Arial', 20))

        # Tabla para el reporte de ordenes
        self.order_report_table = QTableWidget(self)
        self.order_report_table.move(10, 50)
        self.order_report_table.setFixedSize(800, 400)
        self.order_report_table.setColumnCount(5)
        self.order_report_table.setHorizontalHeaderLabels(["Nombre", "Mesa", "Cliente", "Estado", "Pedido:"])
        self.order_report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.order_report_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate_order_report_table()

        # Los elementos para los reportes de los pagos
        self.payment_log_label = QLabel("Reporte de pagos", self)
        self.payment_log_label.move(10, 460)
        self.payment_log_label.setFont(QFont('Arial', 20))

        # Tabla para el reporte de pagos
        self.payment_log_table = QTableWidget(self)
        self.payment_log_table.move(10, 500)
        self.payment_log_table.setFixedSize(800, 400)
        self.payment_log_table.setColumnCount(6)
        self.payment_log_table.setHorizontalHeaderLabels(["Fecha", "ID", "Ordenes", "Tipo de pago", "Monto", "Estado"])
        self.payment_log_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.payment_log_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payment_log_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate_payment_log_table()

        # Elementos para las estadisticas de menu combo
        self.combo_stats_label = QLabel("Estadísticas de combos", self)
        self.combo_stats_label.move(850, 10)
        self.combo_stats_label.setFont(QFont('Arial', 20))

        # Boton para generar las estadisticas de menu combo
        self.generate_combo_stats_button = QPushButton("Generar estadísticas", self)
        self.generate_combo_stats_button.move(850, 50)
        self.generate_combo_stats_button.clicked.connect(self.show_combo_stats)

        # Elememtos para las estadisticas de menu saludable
        self.healthy_menu_stats_label = QLabel("Estadísticas de menú saludable", self)
        self.healthy_menu_stats_label.move(1300, 10)
        self.healthy_menu_stats_label.setFont(QFont('Arial', 20))

        # Boton para generar las estadisticas pagos
        self.generate_healthy_menu_stats_button = QPushButton("Generar estadísticas de pagos", self)
        self.generate_healthy_menu_stats_button.move(1300, 50)
        self.generate_healthy_menu_stats_button.clicked.connect(self.show_healthy_menu_stats)

        # Label de las estadisticas de pagos
        self.payment_stats_label = QLabel("Estadísticas de pagos", self)
        self.payment_stats_label.move(850, 260)
        self.payment_stats_label.setFont(QFont('Arial', 20))

        # Espacio para colocar el rango de fechas a filtrar
        self.date_range_label = QLabel("Rango de fechas", self)
        self.date_range_label.move(850, 310)
        self.date_range_label.setFont(QFont('Arial', 20))

        # Fecha inicial
        self.start_date_label = QLabel("Fecha inicial", self)
        self.start_date_label.move(850, 360)
        self.start_date_label.setFont(QFont('Arial', 15))

        self.start_date_input = QDateEdit(self)
        self.start_date_input.move(850, 390)
        self.start_date_input.setFixedSize(200, 30)
        self.start_date_input.setCalendarPopup(True)

        # Fecha final
        self.end_date_label = QLabel("Fecha final", self)
        self.end_date_label.move(850, 430)
        self.end_date_label.setFont(QFont('Arial', 15))

        self.end_date_input = QDateEdit(self)
        self.end_date_input.move(850, 460)
        self.end_date_input.setFixedSize(200, 30)
        self.end_date_input.setCalendarPopup(True)

        # Boton para generar la estadistica segun el rango de fechas de los pagos
        self.generate_payment_stats_button = QPushButton("Generar estadísticas de pagos", self)
        self.generate_payment_stats_button.move(850, 500)
        self.generate_payment_stats_button.clicked.connect(self.show_payment_stats)

        # Tabla para el reporte de pagos
        self.payment_stats_table = QTableWidget(self)
        self.payment_stats_table.move(850, 550)
        self.payment_stats_table.setFixedSize(800, 300)
        self.payment_stats_table.setColumnCount(6)
        self.payment_stats_table.setHorizontalHeaderLabels(["Fecha", "Pagos", "Ventas", "Tatol de pagos", "Total de ventas", "Perdidas"])
        self.payment_stats_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.payment_stats_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payment_stats_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def populate_order_report_table(self) -> None:
            # Limpiar la tabla existente
        self.order_report_table.setRowCount(0)
        
        # Recorrer el historial de órdenes y agregar las órdenes a la tabla
        for date, orders in self.order_log.order_history.items():
            for order in orders:
                # Obtener detalles de la orden en una cadena
                order_details = ""
                for dish in order.dishes:
                    order_details += f"{dish.name}, "
                order_details = order_details.rstrip(", ")
                
                # Agregar la orden a la tabla
                row_position = self.order_report_table.rowCount()
                self.order_report_table.insertRow(row_position)
                self.order_report_table.setItem(row_position, 0, QTableWidgetItem(date.strftime("%Y-%m-%d")))
                self.order_report_table.setItem(row_position, 1, QTableWidgetItem(str(order.table_number)))
                self.order_report_table.setItem(row_position, 2, QTableWidgetItem(order.customers_name))
                self.order_report_table.setItem(row_position, 3, QTableWidgetItem(order.status))
                self.order_report_table.setItem(row_position, 4, QTableWidgetItem(order_details))

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

    #region menu combo
        # Metodo para calcular la bebida, proteina, acompañamiento y postre mas solicitados del los de ordes
        # Este metodo solo va a funcionar para los combos
        # Debe devolver el elemento mas solicitado de cada tipo y la cantidad de veces que fue solicitado
    def show_combo_stats(self) -> None:
        # Calcula los elementos más solicitados
        top_drink, top_protein, top_side, top_dessert = self.calculate_combo_elements()

        # Crea la ventana de estadísticas
        combo_stats_dialog = ComboStatsWindow(top_drink, top_protein, top_side, top_dessert)
        combo_stats_dialog.exec_()

    def calculate_combo_elements(self) -> None:
        # Inicializa un contador para cada categoría
        drink_counts = Counter()
        protein_counts = Counter()
        side_counts = Counter()
        dessert_counts = Counter()

        # Recorre el historial de órdenes
        for date, orders in self.order_log.order_history.items():
            for order in orders:
                # Recorre los platos de la orden
                for dish in order.dishes:
                    if isinstance(dish, ComboPlate):
                        # Accede a los atributos de drink, protein, side_dish y dessert
                        drink_name = dish.drink.name
                        protein_name = dish.protein.name
                        side_dish_name = dish.side_dish.name
                        dessert_name = dish.dessert.name

                        # Incrementa los contadores
                        drink_counts[drink_name] += 1
                        protein_counts[protein_name] += 1
                        side_counts[side_dish_name] += 1
                        dessert_counts[dessert_name] += 1

        # Define una función para encontrar el elemento más solicitado en un contador
        def most_common_item(counter):
            # validar si el contador esta vacio
            if not counter:
                # retornamos un elemento con nombre None y cantidad 0
                return ("None", 0)
            return reduce(lambda x, y: x if x[1] >= y[1] else y, counter.items())

        # Utiliza map y most_common_item para obtener los elementos más solicitados
        top_drink = most_common_item(drink_counts)
        top_protein = most_common_item(protein_counts)
        top_side = most_common_item(side_counts)
        top_dessert = most_common_item(dessert_counts)

        return top_drink, top_protein, top_side, top_dessert
    #endregion

    #region menu saludable
    # Metodo para calcular la bebida, proteina, acompañamiento y postre mas solicitados del los de ordes
    # Este metodo solo va a funcionar para el menu saludable
    # Debe devolver el elemento mas solicitado de cada tipo y la cantidad de veces que fue solicitado
    def show_healthy_menu_stats(self) -> None:
        # Calcula los elementos más solicitados
        top_drink, top_protein, top_side, top_dessert = self.calculate_healthy_menu_elements()

        # Crea la ventana de estadísticas
        healthy_menu_stats_dialog = HealthyMenuStatsWindow(top_drink, top_protein, top_side, top_dessert)
        healthy_menu_stats_dialog.exec_()

    def calculate_healthy_menu_elements(self) -> None:
        # Inicializa un contador para cada categoría
        drink_counts = Counter()
        protein_counts = Counter()
        side_counts = Counter()
        dessert_counts = Counter()

        # Recorre el historial de órdenes de menu saludable
        for date, orders in self.order_log.order_history.items():
            for order in orders:
                # Recorre los platos de la orden
                for dish in order.dishes:
                    if isinstance(dish, MenuSaludable):
                        # Accede a los atributos de drink, protein, side_dish y dessert
                        drink_name = dish.drink.name
                        protein_name = dish.protein.name
                        side_dish_name = dish.side_dish.name
                        dessert_name = dish.dessert.name

                        # Incrementa los contadores
                        drink_counts[drink_name] += 1
                        protein_counts[protein_name] += 1
                        side_counts[side_dish_name] += 1
                        dessert_counts[dessert_name] += 1
        
        def most_common_item(counter):
            # validar si el contador esta vacio
            if not counter:
                # retornamos un elemento con nombre None y cantidad 0
                return ("None", 0)
            return reduce(lambda x, y: x if x[1] >= y[1] else y, counter.items())
        
        top_drink = most_common_item(drink_counts)
        top_protein = most_common_item(protein_counts)
        top_side = most_common_item(side_counts)
        top_dessert = most_common_item(dessert_counts)

        return top_drink, top_protein, top_side, top_dessert
    #endregion

    #region pagos
    # En este apartado todos los pagos van a considerarse ventas, pero solo los pagos exitosos van a ser considerados pagos o finalizados
    # Del boton de generar estadisticas de pagos se debe de generar un grafico de las ventas y pagos en el rango de fechas seleccionado
    # Debe de devolver la grafica de las ventas y pagos en el rango de fechas seleccionado
    def show_payment_stats(self):
        # Obtén las fechas seleccionadas
        start_date = self.start_date_input.date().toPyDate()
        end_date = self.end_date_input.date().toPyDate()

        # Obtén las estadísticas de pagos y ventas en el rango de fechas seleccionado
        payment_stats, sales_stats = self.get_payment_stats_in_range(start_date, end_date)

        # Verificar que los diccionarios no esten vacios
        if not payment_stats and not sales_stats:
            QMessageBox.warning(self, "Error", "No hay datos para las fechas seleccionadas")
            return
        
        # Limpiar la tabla existente
        self.payment_stats_table.setRowCount(0)

        # Fusionar los datos de pagos y ventas en un solo diccionario
        total_stats = {}
        for date, (payment_count, payment_total) in payment_stats.items():
            sales_count, sales_total = sales_stats.get(date, (0, 0))
            total_stats[date] = (payment_count, sales_count, payment_total, sales_total, sales_total - payment_total)

        # Recorrer el diccionario de estadísticas totales y agregar los datos a la tabla
        for date, stats in total_stats.items():
            row_position = self.payment_stats_table.rowCount()
            self.payment_stats_table.insertRow(row_position)
            self.payment_stats_table.setItem(row_position, 0, QTableWidgetItem(date.strftime("%Y-%m-%d")))
            self.payment_stats_table.setItem(row_position, 1, QTableWidgetItem(str(stats[0])))
            self.payment_stats_table.setItem(row_position, 2, QTableWidgetItem(str(stats[1])))
            self.payment_stats_table.setItem(row_position, 3, QTableWidgetItem(str(stats[2])))
            self.payment_stats_table.setItem(row_position, 4, QTableWidgetItem(str(stats[3])))
            self.payment_stats_table.setItem(row_position, 5, QTableWidgetItem(str(stats[4])))
    
    def get_payment_stats_in_range(self, start_date, end_date) -> None:
        
        # Inicializamos donde se va a guardar en un diccionario las fechas y la información de los pagos
        payment_stats = {}

        # Inicializamos donde se va a guardar en un diccionario las fechas y la información de las ventas
        sales_stats = {}

        # Validar que la fecha inicial sea menor o igual a la fecha final
        if start_date > end_date:
            print("La fecha inicial no puede ser mayor a la fecha final")
            return payment_stats, sales_stats

        # Si alguna de las fechas está vacía, retornamos las listas con una tupla None, 0
        if not start_date or not end_date:
            QMessageBox.warning(self, "Error", "Las fechas no pueden estar vacías")

        # Recorremos el historial de pagos
        for date, payments in self.payment_log.payment_history.items():
            # Si la fecha está en el rango de fechas seleccionado
            if start_date <= date <= end_date:
                # Inicializamos las variables para guardar la cantidad de pagos y el monto total de pagos
                payment_count = 0
                payment_total = 0
                sales_count = 0
                sales_total = 0

                # Recorremos los pagos
                for payment in payments:
                    if payment.status:
                        # Incrementamos el contador de pagos
                        payment_count += 1

                        # Si el pago fue exitoso, incrementamos el monto total de pagos
                        payment_total += payment.billing_amount

                    # Siempre incrementamos el contador de ventas y el monto total de ventas
                    sales_count += 1
                    sales_total += payment.billing_amount

                # Agregamos la fecha y la información de los pagos al diccionario
                payment_stats[date] = (payment_count, payment_total)

                # Agregamos la fecha y la información de las ventas al diccionario
                sales_stats[date] = (sales_count, sales_total)

        return payment_stats, sales_stats

    #endregion
    
