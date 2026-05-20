'''
Contexto: Debes programar la computadora de tiro de un tanque. 
El objetivo está oculto y debes guiar los disparos mediante coordenadas.

Reglas de Funcionamiento:

Configuración de Batalla: El usuario decide cuántas 
oportunidades de disparo tendrá (el máximo permitido son 10).

Dinámica de Tiro: Para cada oportunidad concedida:

    El sistema define una posición de objetivo oculta al azar (entre -50 y 50).

    El usuario ingresa su coordenada de disparo.

Cálculo de Precisión: El sistema debe determinar la distancia 
absoluta (sin valores negativos) entre el disparo y el objetivo.

Categorización del Impacto: Dependiendo de qué tan cerca cayó 
el proyectil, el sistema debe clasificar el resultado:

    Si la distancia es exactamente 0: "Impacto Crítico".

    Si la distancia está entre 1 y 5: "Daño Colateral".

    Si la distancia está entre 6 y 15: "Fallo Cercano".

Cualquier otra distancia: "Tiro Perdido".

Seguridad de Entrada: El programa debe validar que las coordenadas 
ingresadas sean números. Si el usuario ingresa algo inválido, esa oportunidad 
de disparo se pierde por "Falla de Calibración", pero el juego continúa con el siguiente turno.

Factor Ambiental: Si el número de turno actual es impar, el sistema 
debe informar que hay "Viento Lateral", lo que añade una capa de dificultad visual al mensaje.

Finalización: Al terminar todos los turnos, muestra el puntaje total 
acumulado según las categorías de impacto logradas.
'''
import random
objetivo_oculto = random.randint(-50 , 50)
print("Se identifico un objetivo oculto. Debemos destruirlo.")

while True:
    try:
        tiros = int(input("¿Cuantos disparos deseas realizar?. (MÁXIMO 10): "))
        if tiros <= 0 or tiros > 10:
            print("Solo puede ingresar números enteros positivos")
            continue
        break 
    except ValueError:
        print("Solo puede ingresar numeros")
d_critico = 5
d_colateral = 3
d_cercano =1
puntaje = 0
while tiros > 0:
    try:
        print("-"*25)
        print(f"Munición disponible: {tiros} cargas")
        if tiros % 2 != 0:
            print("[ALERTA: Viento Lateral Detectado]")
        else:
            print("CLIMA: Despejado")
        coordenada_disparo = int(input("Ingrese su coordenada de disparo: "))
        tiros -= 1
        distancia = abs(coordenada_disparo - objetivo_oculto)
    except ValueError:
        print("Falla de Calibración")
        tiros -= 1
        continue

    if distancia == 0:
        print("Impacto crítico")
        puntaje += d_critico
    elif 0 < distancia <=5 :
        print("Daño Colateral")
        puntaje += d_colateral
    elif 5 < distancia <=15:
        print("Fallo Cercano")
        puntaje += d_cercano
    else:
        print("Tiro Perdido")

print("-"*25)
print(f"Puntaje final: {puntaje}")

