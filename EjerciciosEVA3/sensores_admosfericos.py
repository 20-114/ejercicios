'''
El Desafío: Crear un recolector de datos climáticos 
que ignore lecturas corruptas de hardware y detecte 
picos térmicos peligrosos.

Comportamiento esperado:

El sistema debe solicitar al operador un total de 5 
lecturas exitosas de temperatura (números enteros).

Si el operador introduce texto, símbolos o deja el espacio 
vacío, el sistema debe mostrar un mensaje de error y volver 
a pedir la lectura actual. No puede avanzar a la siguiente 
lectura hasta que la actual sea un número válido.

A partir de la segunda lectura válida, el sistema debe 
comparar el valor actual con el inmediatamente anterior. Si 
la variación (ya sea que suba o baje) es estrictamente mayor 
a 15 grados, el sistema debe lanzar una alerta de cambio 
abrupto en pantalla antes de continuar.
'''



contador = 1 
lectura_anterior = 0
while contador <= 5:
    try:
        print("-"*25)
        lect = int(input("Ingrese la temperatura medida. \n : "))
        if contador > 1:
            variacion_tem = abs(lect - lectura_anterior)
            if variacion_tem > 15:
                print("¡¡¡ALERTA. Cambio abrupto en la temperatura!!!")
        lectura_anterior = lect
        contador += 1
    except ValueError:
        print("Error en ingreso de temperatura")
    except KeyboardInterrupt:
        print("Bloqueo de emergencia")
        break