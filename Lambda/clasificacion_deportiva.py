'''
Contexto: El comité de un torneo de videojuegos quiere 
determinar qué jugadores avanzan a la gran final tras aplicar 
un factor de dificultad a sus puntajes base.

Los Datos Base: Una lista con los puntajes crudos de los participantes: 
[40, 55, 30, 70, 51, 85].

El Comportamiento Esperado: El programa debe realizar dos 
operaciones consecutivas sobre la colección de datos de manera fluida:

    Modificar todos los puntajes de la lista 
    multiplicándolos por un factor de dificultad de 1.5.

    Evaluar esos nuevos puntajes calculados y 
    conservar exclusivamente a los atletas que 
    logren superar la marca mínima de 75 puntos 
    para clasificar.

El Resultado: Una lista final que muestre los puntajes ajustados 
de los únicos competidores que lograron el pase a la final.
'''

puntajes = [40, 55, 30, 70, 51, 85]
dificultad = 1.5

con_dificultad = map(lambda puntaje: puntaje * dificultad, puntajes)

pase_final = filter(lambda puntaje: puntaje > 75, con_dificultad)
print(list(pase_final))

