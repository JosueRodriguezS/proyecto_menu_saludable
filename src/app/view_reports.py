from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton, QWidget, QDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QFont
from modules.inventario import FoodElement

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
        self.setGEometry(100, 100, 1700, 1000)


