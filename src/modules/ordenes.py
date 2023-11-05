from abc import ABC, abstractmethod
from modules.plato import Plato
from datetime import datetime
import uuid

"""
NOTA: Esta clase va implementar el patrón de diseño Observer.
La clase  Order va a representar las ordenes que se van a crear en el sistema.
Order va a tener los siguientes atributos:
 - table_number: int
 - customers_name: str
 - status: str
 - dishes: list[Plato] 
"""
class Order:
    table_number: int
    customers_name: str
    status: str
    dishes: list[Plato]

    # Constructor de la clase Order
    def __init__(self, table_number: int, customers_name: str, status: str) -> None:
        self.table_number = table_number
        self.customers_name = customers_name
        self.status = status
        self.dishes = []
    
    def add_dish(self, dish: Plato) -> None:
        self.dishes.append(dish)

"""
NOTA: Esta clase va implementar el patrón de diseño Observer.
La clase payment va a representar los pagos que se van a realizar en el sistema.
Payment va a tener los siguientes atributos:
    - orders: list[Order]
    - is_cash: bool
"""
class Payment:
    id: str
    orders: list[Order]
    is_cash: bool
    billing_amount: int
    status: bool  # True si el pago fue exitoso, False si no lo fue

    # Constructor de la clase Payment
    def __init__(self, orders: list[Order], is_cash: bool) -> None:
        # se debe de generar un id único para cada pago (puede ser un número aleatorio)
        self.id = UniqueIDGenerator.generate_unique_id()
        self.orders = orders
        self.is_cash = is_cash
        self.billing_amount = self.calculate_billing_amount()
        self.status = False

    # Método para calcular el monto de la factura
    def calculate_billing_amount(self) -> None:
        return sum(sum(dish.price for dish in order.dishes) for order in self.orders)

    # Método para cambiar el estado del pago
    def change_status(self, status: bool) -> None:
        self.status = status

"""
Nota: esta clase va implementar el patrón de diseño Observer.
Esta la clase que va a representar a los observadores de los pagos.
Esta clase va a ser observada por PaymentObserver.
La clase Payment va a tener los siguientes atributos:
 - orders: list[Order]
 - is_cash: bool
 
"""

"""
Esta es la clase abstracta que va a representar a los observadores de las ordenes.
"""
class Observer(ABC):
    @abstractmethod
    def update(self, order: Order) -> None:
        pass

"""
NOTA: Esta es la clase observadora del patrón de diseño Observer. Va a funcionar como una bitácora de las ordenes.
La clase OrderLog va a representar a la bitácora de las ordenes. Es el observador.
OrderLog va a contener los siguientes atributos:
    - order_history: {datetime: str, order: Order}
"""
class OrderLog(Observer):
    def __init__(self) -> None:
        self.order_history = {}

    def update(self, order: Order) -> None:
        #Usamos la fecha actual
        today = datetime.now().date()

        #Si la fecha actual no está en el historial de ordenes, la agregamos
        if today not in self.order_history:
            self.order_history[today] = []
        
        #Agregamos la orden al historial
        self.order_history[today].append(order)
"""
NOTA: Esta es la clase observadora del patrón de diseño Observer. Va a funcionar como una bitácora de los pagos.
La clase PaymentLog va a representar a la bitácora de los pagos. Es el observador.
PaymentLog va a contener los siguientes atributos:
    - payment_history: {datetime: str, payment: Payment}
"""
class PaymentLog(Observer):
    def __init__(self) -> None:
        self.payment_history = {}

    def update(self, payment: Payment) -> None:
        #Usamos la fecha actual
        today = datetime.now().date()

        #Si la fecha actual no está en el historial de ordenes, la agregamos
        if today not in self.payment_history:
            self.payment_history[today] = []
        
        #Agregamos la orden al historial
        self.payment_history[today].append(payment)

"""
La clase Table va a representar a las mesas del restaurante.
Table va a tener los siguientes atributos:
 - number: int
 - order_log: OrderLog
 - number_of_customers: int
 - status: str
 - orders: list[Order]
"""
class Table:
    number: int
    order_log: OrderLog
    payment_log: PaymentLog
    number_of_customers: int
    single_bill: bool
    status: str
    orders: list[Order]
    payments: list[Payment]

    # Constructor de la clase Table
    def __init__(self, number: int, order_log: OrderLog, payment_log: PaymentLog, number_of_customers: int, single_bill: bool, status: str) -> None:
        self.number = number
        self.order_log = order_log
        self.payment_log = payment_log
        self.number_of_customers = number_of_customers
        self.single_bill = single_bill
        self.status = status
        self.orders = []
        self.payments = []
    
    # Metos para agregar ordenes y pagos
    def add_order(self, order: Order) -> None:
        self.orders.append(order)
        self.notify_order_log(order=order)

    def add_payment(self, payment: Payment) -> None:
        self.payments.append(payment)
        self.notify_payment_log(payment=payment)

    # Métodos para notificar a los observadores
    def notify_order_log(self, order: Order) -> None:
        self.order_log.update(order=order)

    def notify_payment_log(self, payment: Payment) -> None:
        self.payment_log.update(payment=payment)

    # Metodos para editar el numero de clientes, el estado y la cuenta unica
    def edit_number_of_customers(self, number_of_customers: int) -> None:
        self.number_of_customers = number_of_customers

    def edit_status(self, status: str) -> None:
        self.status = status

    def edit_single_bill(self, single_bill: bool) -> None:
        self.single_bill = single_bill
        

"""
La clase UniqueIdGenerator va a representar a un generador de ids únicos.
La va utilizar la clase Payment para generar un id único para cada pago.
"""

class UniqueIDGenerator:
        used_ids = set()

        @staticmethod
        def generate_unique_id():
            unique_id = str(uuid.uuid4())
            while unique_id in UniqueIDGenerator.used_ids:
                unique_id = str(uuid.uuid4())
            UniqueIDGenerator.used_ids.add(unique_id)
            return unique_id
