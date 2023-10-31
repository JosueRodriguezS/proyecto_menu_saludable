-- SQLBook: Code
-- restaurante.sql
DROP TABLE IF EXISTS FoodElements;
DROP TABLE IF EXISTS Platos;
DROP TABLE IF EXISTS ComboPlates;
DROP TABLE IF EXISTS MenuSaludable;

CREATE TABLE IF NOT EXISTS FoodElements (
    name TEXT PRIMARY KEY,
    food_type TEXT,
    calories INTEGER,
    characteristics TEXT,
    price INTEGER
);

CREATE TABLE IF NOT EXISTS Platos (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    calories INTEGER
);

CREATE TABLE IF NOT EXISTS ComboPlates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    calories INTEGER,
    drink_name TEXT,
    protein_name TEXT,
    side_dish_name TEXT,
    dessert_name TEXT
);

CREATE TABLE IF NOT EXISTS MenuSaludable (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    calories INTEGER,
    drink_name TEXT,
    protein_name TEXT,
    side_dish_name TEXT,
    dessert_name TEXT
);
-- Inserción de datos en la tabla FoodElements

INSERT INTO FoodElements (name, food_type, calories, characteristics, price) VALUES
    ('cafe', 'bebida', 10, 'caliente, cafeina', 2000),
    ('leche', 'bebida', 20, 'frio, lacteo', 2500),
    ('jugo', 'bebida', 30, 'frio, fruta', 3000),
    ('soda', 'bebida', 30, 'frio, gas', 3000),
    ('te', 'bebida', 5, 'caliente, hierba', 1000),
    ('agua', 'bebida', 0, 'frio, incoloro', 500),
    ('refresco', 'bebida', 50, 'frio, gas, azucar', 1500),
    ('cerveza', 'bebida', 100, 'frio, gas, alcohol', 3000),
    ('vino', 'bebida', 150, 'frio, alcohol', 4000),
    ('leche_chocolate', 'bebida', 100, 'frio, lacteo, azucar, chocolate', 2500),
    ('leche_cafe', 'bebida', 50, 'frio, lacteo, cafeina', 2000),
    ('leche_chocolate_cafe', 'bebida', 150, 'frio, lacteo, cafeina, azucar, chocolate', 3000),
    ('huevo', 'proteina', 100, 'animal, proteina', 2500),
    ('jamon', 'proteina', 150, 'animal, proteina', 3500),
    ('chorizo', 'proteina', 200, 'animal, proteina', 4500),
    ('salchicha', 'proteina', 200, 'animal, proteina', 4500),
    ('pollo', 'proteina', 200, 'animal, proteina', 4500),
    ('pescado', 'proteina', 200, 'animal, proteina', 4500),
    ('carne', 'proteina', 200, 'animal, proteina', 4500),
    ('tocino', 'proteina', 200, 'animal, proteina', 4500),
    ('tofu', 'proteina', 200, 'vegetal, proteina', 2500),
    ('lentejas', 'proteina', 200, 'vegetal, proteina', 2500),
    ('frijoles', 'proteina', 200, 'vegetal, proteina', 2500),
    ('garbanzos', 'proteina', 200, 'vegetal, proteina', 2500),
    ('nuez', 'proteina', 200, 'vegetal, proteina', 2500),
    ('soya', 'proteina', 200, 'vegetal, proteina', 2500),
    ('pan', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('tortilla', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('papa', 'acompanamiento', 100, 'tuberculo', 1500),
    ('arroz', 'acompanamiento', 100, 'cereal', 1500),
    ('lechuga', 'acompanamiento', 100, 'verdura', 1500),
    ('espinaca', 'acompanamiento', 100, 'verdura', 1500),
    ('aguacate', 'acompanamiento', 100, 'fruta', 1500),
    ('tomate', 'acompanamiento', 100, 'fruta', 1500),
    ('cebolla', 'acompanamiento', 100, 'verdura', 1500),
    ('zanahoria', 'acompanamiento', 100, 'verdura', 1500),
    ('pepino', 'acompanamiento', 100, 'verdura', 1500),
    ('chile', 'acompanamiento', 100, 'verdura', 1500),
    ('manzana', 'acompanamiento', 100, 'fruta', 1500),
    ('naranja', 'acompanamiento', 100, 'fruta', 1500),
    ('platano', 'acompanamiento', 100, 'fruta', 1500),
    ('melon', 'acompanamiento', 100, 'fruta', 1500),
    ('sandia', 'acompanamiento', 100, 'fruta', 1500),
    ('pasta', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('pizza', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('hotdog', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('hamburguesa', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('papas_fritas', 'acompanamiento', 100, 'tuberculo', 1500),
    ('quesadilla', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('tacos', 'acompanamiento', 100, 'harina, cereal', 1500),
    ('yuca_frita', 'acompanamiento', 100, 'tuberculo', 1500),
    ('queso', 'acompanamiento', 100, 'lacteo', 1500),
    ('crema', 'acompanamiento', 100, 'lacteo', 1500),
    ('mantequilla', 'acompanamiento', 100, 'lacteo', 1500),
    ('mayonesa', 'acompanamiento', 100, 'lacteo', 1500),
    ('helado', 'postre', 100, 'frio, azucar, lacteo', 2000),
    ('pastel', 'postre', 100, 'azucar, harina, lacteo', 2500),
    ('gelatina', 'postre', 100, 'frio, azucar', 1500),
    ('galletas', 'postre', 100, 'azucar, harina', 1000),
    ('donut', 'postre', 100, 'azucar, harina, lacteo', 1500),
    ('pie', 'postre', 100, 'azucar, harina, lacteo', 1500),
    ('pastelillo', 'postre', 100, 'azucar, harina, lacteo', 1500),
    ('ensalada', 'postre', 100, 'fruta', 1500),
    ('pan_dulce', 'postre', 100, 'azucar, harina, lacteo', 1500),
    ('flan', 'postre', 100, 'azucar, lacteo', 1500);

-- Insercion de 25 platos en la tabla Platos
INSERT INTO Platos (name, price, calories) VALUES
    ('Plato 1', 30000, 750),
    ('Plato 2', 28000, 700),
    ('Plato 3', 25000, 800),
    ('Plato 4', 32000, 900),
    ('Plato 5', 35000, 850),
    ('Plato 6', 29000, 720),
    ('Plato 7', 27500, 780),
    ('Plato 8', 31000, 920),
    ('Plato 9', 26500, 740),
    ('Plato 10', 29000, 710),
    ('Plato 11', 27000, 800),
    ('Plato 12', 33000, 920),
    ('Plato 13', 29500, 780),
    ('Plato 14', 30500, 750),
    ('Plato 15', 28000, 770),
    ('Plato 16', 32500, 880),
    ('Plato 17', 31000, 720),
    ('Plato 18', 29500, 790),
    ('Plato 19', 28500, 750),
    ('Plato 20', 31500, 820),
    ('Plato 21', 27500, 730),
    ('Plato 22', 27000, 700),
    ('Plato 23', 29500, 760),
    ('Plato 24', 32000, 880),
    ('Plato 25', 29500, 770);

-- Insercion de 15 combo en la tabla ComboPlates
INSERT INTO ComboPlates (name, price, calories, drink_name, protein_name, side_dish_name, dessert_name) VALUES
    ('Combo 1', 15, 12000, 'soda', 'pollo', 'papas_fritas', 'pastel'),
    ('Combo 2', 14, 10050, 'jugo', 'carne', 'arroz', 'helado'),
    ('Combo 3', 16, 12000, 'te', 'tofu', 'ensalada', 'galletas'),
    ('Combo 4', 15, 11000, 'cerveza', 'pescado', 'papas_fritas', 'pastelillo'),
    ('Combo 5', 14, 10500, 'agua', 'hamburguesa', 'papas_fritas', 'flan'),
    ('Combo 6', 16, 12000, 'leche', 'jamon', 'tortilla', 'donut'),
    ('Combo 7', 15, 11000, 'vino', 'hotdog', 'papa', 'pie'),
    ('Combo 8', 14, 10500, 'leche', 'lentejas', 'lechuga', 'pan_dulce'),
    ('Combo 9', 16, 12000, 'te', 'tocino', 'tomate', 'gelatina'),
    ('Combo 10', 15, 11000, 'cerveza', 'huevo', 'zanahoria', 'helado');



-- Inserción de datos en la tabla MenuSaludable
INSERT INTO MenuSaludable (name, price, calories, drink_name, protein_name, side_dish_name, dessert_name) VALUES
    ('Menu Saludable 1', 12, 15000, 'Agua', 'Pechuga de Pollo a la Parrilla', 'Ensalada de Espinaca', 'Fruta Fresca'),
    ('Menu Saludable 2', 14, 10550, 'Jugo de Naranja Natural', 'Salmon a la Parrilla', 'Brocoli al Vapor', 'Yogur Bajo en Grasa'),
    ('Menu Saludable 3', 13, 13480, 'Te Verde', 'Tofu a la Parrilla', 'Ensalada de Quinua', 'Compota de Manzana Sin Azucar'),
    ('Menu Saludable 4', 12, 15490, 'Agua de Coco', 'Pechuga de Pavo a la Parrilla', 'Zanahorias Baby', 'Fruta Mixta'),
    ('Menu Saludable 5', 15, 18550, 'Jugo de Zanahoria Fresco', 'Pechuga de Pollo a la Parrilla', 'Esparragos al Vapor', 'Gelatina Sin Azucar'),
    ('Menu Saludable 6', 13, 14520, 'Te de Hierbas', 'Salmon al Horno', 'Brocoli al Vapor', 'Compota de Pera Sin Azucar'),
    ('Menu Saludable 7', 14, 12530, 'Agua con Limon', 'Tofu Salteado con Verduras', 'Ensalada de Lentejas', 'Yogur Natural'),
    ('Menu Saludable 8', 15, 11600, 'Jugo de Manzana Natural', 'Pechuga de Pollo a la Parrilla', 'Espinacas Salteadas', 'Fruta Fresca'),
    ('Menu Saludable 9', 12, 15470, 'Te de Menta', 'Salmon a la Parrilla', 'Col Rizada al Vapor', 'Yogur Griego Bajo en Grasa'),
    ('Menu Saludable 10', 14, 16520, 'Agua Mineral', 'Tofu a la Parrilla con Salsa de Soja', 'Ensalada de Garbanzos', 'Compota de Ciruela Sin Azucar');

