import pytest
from modules.inventario import Inventory, FoodElement 

@pytest.fixture
def dummy_inventory() -> Inventory:
    inventory = Inventory()
    element1 = FoodElement(name="Papas", food_type="acompanamiento", calories=100, characteristics=["vegetariano", "carbohidrato"], price=1000)
    element2 = FoodElement(name="Pollo", food_type="proteina", calories=200, characteristics=["carne_blanca"], price=2000)
    inventory.add_food_element(food_element=element1)
    inventory.add_food_element(food_element=element2)
    return inventory


"""
Test para comprobar que invetario es respeta el patrón de diseño Singleton

Este test es simple, se crea una instancia de la clase Inventory y se comprueba que es la misma instancia que se crea en el fixture dummy_inventory
"""
def test_singleton(dummy_inventory) -> None:
    inventory = Inventory()
    assert inventory is dummy_inventory


"""
Test para el método add_food_element

El método add_food_element recibe como parámetro:
    - food_element: FoodElement
"""
def test_add_food_element(dummy_inventory) -> None:
    new_dummy_element = FoodElement(name="Ensalada", food_type="acompanamiento", calories=50, characteristics=["vegetariano", "frío"], price=500)
    dummy_inventory.add_food_element(food_element=new_dummy_element)
    assert "Ensalada" in dummy_inventory.food_elements

"""
Test para el método remove_food_element 

El método remove_food_element recibe como parámetro:
    - food_element_name: str
"""
def test_remove_food_element(dummy_inventory) -> None:
    new_dummy_element = FoodElement(name="Garbanzos", food_type="acompanamiento", calories=50, characteristics=["vegetariano", "legumbre"], price=500)
    dummy_inventory.add_food_element(food_element=new_dummy_element)
    dummy_inventory.remove_food_element(food_element_name="Garbanzos")
    assert "Garbanzos" not in dummy_inventory.food_elements


"""
Test para el método modify_food_element

El método modify_food_element recibe como parámetros:
    - food_element_name: str
    - modified_element: FoodElement
"""
def test_modify_food_element(dummy_inventory) -> None:
    new_dummy_element = FoodElement(name="Garbanzos", food_type="acompanamiento", calories=50, characteristics=["vegetariano", "legumbre"], price=500)
    dummy_inventory.add_food_element(food_element=new_dummy_element)
    modified_dummy_element = FoodElement(name="Garbanzos", food_type="acompanamiento", calories=50, characteristics=["vegetariano", "frío"], price=1000)
    dummy_inventory.modify_food_element(food_element_name="Garbanzos", modified_element=modified_dummy_element)
    assert dummy_inventory.food_elements["Garbanzos"].price is 1000 and "frío" in dummy_inventory.food_elements["Garbanzos"].characteristics

