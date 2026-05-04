import random
import time

bitacora = ""
nave_energia = 100
exploracion = "TOS" #A)Encontrar Titanio "T" / B)Encontrar Oro "O" / C)Tormenta sola. No encuentra nada. La nave pierde 20 puntos (S)
creditos = 0
while nave_energia > 0:
    print(f"Energía de la nave: {nave_energia}")
    accion = int(input(f"Elija una acción \n1) Explorar Planetas (consume 15 de energía) \n2) Analizar Bitacora \n3) Recargar Energía \n4) Retornar a la Tierra \n "))
    match accion:
        case 1: #Exploración
            nave_energia -= 15
            lugar_explorado = random.choice(exploracion)
            print("Viajando por el hiprespacio")
            time.sleep(2)
            if lugar_explorado == "T":
                print("Encontraste Titanio")
                bitacora += lugar_explorado
            elif lugar_explorado == "O":
                print("Encontraste Oro")
                bitacora += lugar_explorado
            else:
                print("Interceptaste una tormenta solar. \nPerdiste 20 de energía")
                nave_energia -= 20  
            print("-" * 40) 
        case 2: #Análisis de bitácora
            if creditos > 0:
                creditos = 0
            for elemento_de_bitacora in bitacora:
                if elemento_de_bitacora == "T":
                    creditos += 50
                elif elemento_de_bitacora == "O":
                    creditos += 100
            print(f"Total de créditos: {creditos}")
            print("-" * 40) 
        case 3: #Recarga de energía
            recarga_energia = random.randint(1, 2)
            if recarga_energia == 1:
                nave_energia += 30
                print("Recarga de energía exitosa (+30)")
            else:
                print("Fallo al intetar recargar energía")
            if nave_energia > 100:
                print("Energía de la nave al maximo")
                nave_energia = 100
            print("-" * 40)
        case 4: #Vuelta a la Tierra
            print("Misión exitosa \nRetornando a la Tierra...")
            nave_energia = 0
            print("-" * 40)
    creditos_finales = creditos
    if accion != 4 and nave_energia <= 20 and nave_energia > 0:
        print("¡Peligro: Energía Crítica")
    elif accion != 4 and nave_energia <= 0:
        print("Nave perdida en el espacio...")
        nave_energia = 0
    

puntaje_final = len(bitacora)
print(f"Puntaje total: {puntaje_final} \nCréditos recolectados: {creditos_finales}")
