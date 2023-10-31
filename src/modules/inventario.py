"""
La clase FoodElement va a representar los elementos de comida que se van a guardar en el inventario.
FoodElement va a tener los siguientes atributos:
 - name: str
 - food_type: str (bebida, proteina, acompanamiento, postre)
 - calories: int
 - characteristics: list
 - price: int
"""
class FoodElement:
    name: str
    food_type: str
    calories: int
    characteristics: list 
    price: int

    # Constructor de la clase FoodElement
    def __init__(self, name: str, food_type: str, calories: int, characteristics: list, price: int) -> None:
        self.name = name
        self.food_type = food_type
        self.calories = calories
        self.characteristics = characteristics
        self.price = price

"""
NOTA: Esta clase va implementar el patrón de diseño Singleton.
La clase Inventory va a representar el inventario de FoodElements que se van a guardar en el sistema.
Inventory va a tener los siguientes atributos:
 - food_elements: list
"""
class Inventory:
    _instance = None

    def __new__(cls) -> None:
        if cls._instance is None:
            cls._instance = super(Inventory, cls).__new__(cls)
            cls._instance.food_elements = {}
        return cls._instance
    
    # Método para agregar un FoodElement al inventario
    def add_food_element(self, food_element: FoodElement) -> None:
        if food_element not in self.food_elements:
            self.food_elements[food_element.name] = food_element

    # Método para eliminar un FoodElement del inventario
    def remove_food_element(self, food_element_name: str) -> None:
        if food_element_name in self.food_elements:
            del self.food_elements[food_element_name]
    
    # Método para modificar un FoodElement del inventario
    def modify_food_element(self, food_element_name: str, modified_element: FoodElement) -> None:
        if food_element_name in self.food_elements:
            self.food_elements[food_element_name] = modified_element

