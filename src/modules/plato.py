from modules.inventario import FoodElement

"""
La clase Plato va a representar la super clase de las cuales van a heredar los platos que se van a crear.
PLato va a tener los siguientes atributos:

 - id: int
 - name: str
 - price: int
 - calories: int
"""

class Plato:
    id: int
    name: str
    price: int
    calories: int
    def __init__(self, id: int, name: str, price: int, calories: int) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.calories = calories

class ComboPlate(Plato):
    drink: FoodElement
    protein: FoodElement
    side_dish: FoodElement
    dessert: FoodElement
    def __init__(self, id: int, name: str, price: int, calories: int, drink: FoodElement, protein: FoodElement, side_dish: FoodElement, dessert: FoodElement) -> None:
        super().__init__(id=id, name=name, price=price, calories=calories)
        self.id = id
        self.name = name
        self.price = price
        self.calories = calories
        self.drink = drink
        self.protein = protein
        self.side_dish = side_dish
        self.dessert = dessert

    def set_drink(self, drink: FoodElement):
        self.drink = drink

    def set_protein(self, protein: FoodElement):
        self.protein = protein

    def set_side_dish(self, side_dish: FoodElement):
        self.side_dish = side_dish

    def set_dessert(self, dessert: FoodElement):
        self.dessert = dessert

    def set_price(self, price: int):
        self.price = price

    def set_calories(self, calories: int):
        self.calories = calories

    def is_combo(self) -> bool:
        return True

# Clase para manejar el factory de combos
class ComboPlateFactory:
    @staticmethod
    # Función para crear un objeto ComboPlate
    def create_combo_plate(id: int, name: str, price: float, calories: float, drink: str, protein: str, side_dish: str, dessert: str) -> ComboPlate:
        return ComboPlate(id=id, name=name, price=price, calories=calories, drink=drink, protein=protein, side_dish=side_dish, dessert=dessert)