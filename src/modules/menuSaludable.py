from modules.plato import Plato
from modules.inventario import FoodElement


class MenuSaludable(Plato):
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