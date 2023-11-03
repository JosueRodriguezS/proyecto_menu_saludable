import pytest
from modules.plato import Plato, ComboPlate, ComboPlateFactory
from modules.inventario import FoodElement 

# Pruebas para la clase ComboPlate
def test_combo_plate_creation() -> None:
    drink = FoodElement('Drink', 'Cafe', 20, ['sin azucar'], 10)
    protein = FoodElement('Protein', 'Pollo', 30, ['a la plancha'], 20)
    side_dish = FoodElement('Side Dish','ensalada', 10, ['verde'], 5)
    dessert = FoodElement('Dessert', 'Tres leches', 4, ['con chocolate'], 5)

    combo_plate = ComboPlateFactory.create_combo_plate(1, "Combo", 10, 1000, drink, protein, side_dish, dessert) 

    assert combo_plate.id is 1 and \
           combo_plate.name is 'Combo' and \
           combo_plate.price is 10 and \
           combo_plate.calories is 1000 and \
           combo_plate.drink is drink and \
           combo_plate.protein is protein and \
           combo_plate.side_dish is side_dish and \
           combo_plate.dessert is dessert
