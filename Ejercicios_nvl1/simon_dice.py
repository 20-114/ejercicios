import random 
import time

# col1 = "R"
# col2 = "V"
# col3 = "A"
# col4 = "M"
colores = "RVAM"
secuencia = ""
cadena_correcta = ""
continuidad = True

while continuidad  == True:
    # color_azar = random.randint(1, 4)
    # if color_azar == 1:
    #     secuencia += col1
    # elif color_azar == 2:
    #     secuencia += col2
    # elif color_azar == 3:
    #     secuencia += col3
    # elif color_azar == 4:
    #     secuencia += col4
    secuencia += random.choice(colores)
    print(f"Ronda {len(secuencia)} / Secuencia: {secuencia}")
    time.sleep(3)
    print("\n" * 50)
    respuesta = input("Ingrese la secuencia anterior de corrido: ")

    if respuesta == secuencia:
        print("Felicidades")
        cadena_correcta = secuencia
    else:
        print("Game Over")
        continuidad = False

print(f"Puntaje {len(cadena_correcta)}")


