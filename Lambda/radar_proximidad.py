'''
Contexto: El sistema de navegación de un dron recibe las coordenadas 
de varios objetivos en un plano cartesiano y debe identificar cuáles 
están dentro de su rango de acción.

Los Datos Base: Una lista de tuplas que representan coordenadas (x, y) 
de diferentes puntos en el espacio respecto al dron ubicado en el 
centro (0, 0): 
[(3, 4), (10, 12), (1, 1), (6, 8), (15, 2)].

El Comportamiento Esperado: 
    El programa debe calcular la distancia en línea recta desde el dron hacia 
    cada punto utilizando la fórmula matemática de la distancia al origen:

    raíz{x^2 + y^2}

Una vez calculadas las distancias de todos los puntos, el sistema debe filtrar 
los resultados para conservar únicamente las distancias de aquellos objetivos 
que se encuentren dentro de un radio de cobertura seguro menor o igual a 10 unidades.

El Resultado: Una lista con los valores numéricos de las distancias de los cuerpos 
que están efectivamente dentro del rango del radar.

Con estos ejercicios vas a notar cómo el código se vuelve mucho más declarativo 
(le dices al programa qué hacer con los datos, en lugar de guiarlo paso a paso en 
el cómo recorrerlos). ¡Quedo atento a ver cómo planteas las soluciones!
'''

coordenadas = [(3, 4), (10, 12), (1, 1), (6, 8), (15, 2)]

distancia = map(lambda par: ((par[0]*par[0]) + (par[1]*par[1]))**(1/2), coordenadas)

radio_seguro = filter(lambda dist: dist <= 10, distancia)

print(list(radio_seguro))