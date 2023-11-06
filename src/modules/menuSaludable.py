from modules.plato import Plato
from modules.inventario import FoodElement, Inventory
from pyswip import Prolog

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

    def is_combo(self) -> bool:
        return False

# Metodo para cargar inventario a prolog y generar menu saludables
def generate_sa1udable(inventory: Inventory):

    prolog = Prolog()
    prolog.consult("src\\modules\\menuSaludable.pl")
    for food in inventory.food_elements.values():
        prolog.assertz(f"element({food.name}, {food.food_type}, {food.characteristics})")

    # Ejemplo de consulta para verificar que los elementos se hayan cargado correctamente
    for element in prolog.query("element(X, Type, Characteristics)"):
        print(f"Elemento: {element['X']} - Tipo: {element['Type']} - Características: {element['Characteristics']}")

    # Genera menús saludables
    for menu in prolog.query("generate_saludable(5, MenuSaludable)"):
        print("Menú Saludable:", list(menu['MenuSaludable']))

