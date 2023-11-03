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
 - food_elements: dict[food_name, FoodElement]
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

    # Método para obtener una lista de los nombres de los FoodElements por tipo
    def get_food_elements_names(self, food_type: str) -> list[str]:
        return [food_element.name for food_element in self.food_elements.values() if food_element.food_type == food_type]


    # Método para obtener las características posibles de los FoodElements en el inventario
    def get_all_characteristics(self) -> list:
        all_characteristics = set()

        for food_element in self.food_elements.values():
            characteristics = food_element.characteristics.split(', ')  # Dividir las características por comas y espacio
            all_characteristics.update(characteristics)

        return list(all_characteristics)

