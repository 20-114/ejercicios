import random

produccion_del_dia = random.randint(30, 60)
print(produccion_del_dia)

muestras_doradas = 0
control_calidad = 0
prueba_estres = 0
aprobado_regular = 0


for chip in range(1, produccion_del_dia +1):
    print(f"Evaluando chip número {chip}")
    if chip % 3 == 0 and chip % 5 == 0:
        print(f"Pieza {chip}: Muestra Dorada")
        muestras_doradas += 1
        print("-" * 50)
    elif chip % 3 == 0 and chip % 5 != 0:
        print(f"Pieza {chip}: Control de Calidad")
        control_calidad += 1
        print("-" * 50)
    elif chip % 5 == 0 and chip % 3 != 0:
        print(f"Pieza {chip}: Prueba de Estrés")
        prueba_estres += 1
        print("-" * 50)
    elif chip % 3 != 0 and chip % 5 != 0:
        print(f"Pieza {chip}: Aprobado Regular")
        aprobado_regular += 1
        print("-" * 50)

print(f"Total ed piezas fabricadas {chip}. \nMuestras Doradas recolectadas: {muestras_doradas}")




