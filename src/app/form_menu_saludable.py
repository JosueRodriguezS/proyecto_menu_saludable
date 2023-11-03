from PyQt5.QtWidgets import QWidget
from app.form_menu_saludable_ui import Ui_menu_saludable_form

class menuSaludableWindow(QWidget):
    def  __init__(self):
        super().__init__()
        self.ui = Ui_menu_saludable_form()
        self.ui.setupUi(self)


    