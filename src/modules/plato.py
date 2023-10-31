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

def create_combo_plate(id, name, price, calories, drink, protein, side_dish, dessert) -> ComboPlate:
    return ComboPlate(id=id, name=name, price=price, calories=calories, drink=drink, protein=protein, side_dish=side_dish, dessert=dessert)