:- use_module(library(random)).
:- use_module(library(lists)).

:- use_module(library(lists)).

% Definir hechos para los elementos del inventario (bebidas, proteínas, acompañamientos y postres).
element(bebida1, 'bebida', [azucarada, no_alcoholica, baja_caloria]).
element(bebida2, 'bebida', [azucarada, alcoholica]).
element(proteina1, 'proteina', [pollo, baja_grasa]).
element(proteina2, 'proteina', [pescado, alta_proteina]).
element(acompanamiento1, 'acompanamiento', [papas, fritas]).
element(acompanamiento2, 'acompanamiento', [ensalada, frutas]).
element(postre1, 'postre', [helado, frutas]).
element(postre2, 'postre', [galletas, chocolate]).

% Regla para generar todos los menús saludables posibles que cumplan con las características deseadas.
generate_saludables(DrinkCharacteristic, ProteinCharacteristic, SideDishCharacteristic, DessertCharacteristic, MenuSaludables) :-
    findall([Bebida, Proteina, Acompanamiento, Postre],
            (element(Bebida, 'bebida', Characteristics1),
             element(Proteina, 'proteina', Characteristics2),
             element(Acompanamiento, 'acompanamiento', Characteristics3),
             element(Postre, 'postre', Characteristics4),
             member(DrinkCharacteristic, Characteristics1),
             member(ProteinCharacteristic, Characteristics2),
             member(SideDishCharacteristic, Characteristics3),
             member(DessertCharacteristic, Characteristics4)),
            MenuSaludables).

