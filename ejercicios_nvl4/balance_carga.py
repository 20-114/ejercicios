'''
El Desafío: Administrar la carga de trabajo de un 
grupo de nodos de procesamiento, distribuyendo tareas 
y manejando caídas imprevistas de los servidores.

Comportamiento esperado:

El sistema maneja un inventario de nodos. Inicialmente 
hay 3 nodos activos, identificados como 1, 2 y 3. Cada 
nodo tiene asignada una lista de tareas representadas 
por su peso de procesamiento (números enteros). Todos 
empiezan con sus listas vacías.

El programa pide de forma continua que se ingrese el 
peso de una nueva tarea (un número entero). El ciclo 
termina si el usuario escribe APAGAR.

Al ingresar una tarea:

Si la entrada no es un número entero válido (o es menor 
o igual a cero), el sistema lo reporta como "Tarea corrupta" 
y pide la entrada de nuevo.

Si la tarea es válida, el sistema debe asignarla al nodo 
que el usuario elija (pidiendo el número de nodo 1, 2 o 3).

Si el usuario elige un nodo que no existe o introduce 
letras en la selección del nodo, el sistema debe atrapar 
el error, advertir que el nodo no responde y redirigir 
automáticamente esa tarea a una lista especial de "Tareas en Espera".

Simulación de caída: Justo después de asignar la tarea, 
el sistema genera un número aleatorio entre 1 y 10. Si el 
número es exactamente divisible entre 5, significa que el 
nodo seleccionado sufrió una sobrecarga: el sistema vacía por 
completo la lista de tareas de ese nodo (se pierden) y muestra 
un mensaje de "⚠️ Nodo colapsado. Memoria liberada".
'''

# import random

# nodos = {
#     '1' : [],
#     '2' : [],
#     '3' : [],
#     'espera' : []
# }


# while True:
#     try:
#         try:
#             tamano_tarea = input("- Ingresa el tamaño de la tarea \n- Ingresa APAGAR para salir del sistema \n : ").upper()

#             if tamano_tarea == "APAGAR":
#                 print("Informe de nodos:")
#                 for clave, valor in nodos.items():
#                     print(f"{clave} : {valor}")
#                 print("Saliendo del sistema")
#                 break
#             else:
#                 tamano_tarea = int(tamano_tarea)

#             if tamano_tarea <= 0:
#                 print("Tarea corrupta")
#                 print("Intenta de nuevo")
#                 continue

#         except ValueError:
#             print("Tarea corrupta")
#             print("Intenta de nuevo")
#             continue

#         try:
#             nodo_procesamiento = int(input("Indica el nodo que desea para procesar la información (1, 2 o 3): "))
#         except ValueError:
#             print("El nodo no responde...")
#             nodos['espera'].append(tamano_tarea) #agrega archivos a lista de espera en caso de ingreso de palabras de parte del usuario 
#             continue

#         num = random.randint(1, 10) #evalua posible fallo del nodo por sobecarga

#         if nodo_procesamiento > len(nodos)-1 or nodo_procesamiento < 1:  #evalua si agrega archivo a la lista de espera segpun la selección de nodo
#             print("El nodo no responde...")
#             nodos['espera'].append(tamano_tarea)
#         else:
#             nodo_procesamiento = str(nodo_procesamiento) #transforma la variable "nodo_procesamiento" a string para modificar los valores de cada doiccionario
#             nodos[nodo_procesamiento].append(tamano_tarea)

#             if num % 5 == 0: #evalua posible fallo del nodo por sobecarga
#                 print(num)
#                 nodos[nodo_procesamiento].clear()
#                 print("⚠️ Nodo colapsado. Memoria liberada")

#     except KeyboardInterrupt:
#         print("Bloqueo de Emergencia")
#         print("Informe de nodos:")
#         for clave, valor in nodos.items():
#             print(f"{clave} : {valor}")
#         break
    

# Ahora con funciones


import random

# --- CONFIGURACIÓN GLOBAL (El patio principal) ---
nodos = {
    '1' : [],
    '2' : [],
    '3' : [],
    'espera' : []
}

# --- FUNCIONES DEL SISTEMA ---

def mostrar_informe():
    """Imprime en consola el estado actual de almacenamiento de todos los nodos."""
    print("Informe de nodos:")
    for clave, valor in nodos.items():
        print(f"{clave} : {valor}")

def despachar_tarea(nodo_elegido, peso_tarea):
    """
    Se encarga de enrutar la tarea al nodo correspondiente, aplicando 
    las reglas de desconexión y la simulación de colapso por sobrecarga.
    """
    # Mantenemos tu validación exacta basada en el tamaño del diccionario
    if nodo_elegido > len(nodos) - 1 or nodo_elegido < 1:  
        print("El nodo no responde...")
        nodos['espera'].append(peso_tarea)
    else:
        nodo_str = str(nodo_elegido) 
        
        # 1. Asignamos la tarea al nodo apuntado
        nodos[nodo_str].append(peso_tarea)
        
        # 2. Simulación aleatoria de sobrecarga inmediata
        num = random.randint(1, 10) 
        if num % 5 == 0: 
            nodos[nodo_str].clear()
            print("⚠️ Nodo colapsado. Memoria liberada")


# --- FLUJO PRINCIPAL DEL CLÚSTER (Bucle de Control) ---
while True:
    try:
        # Fase 1: Captura y validación del tamaño de la tarea
        try:
            tamano_tarea = input("- Ingresa el tamaño de la tarea \n- Ingresa APAGAR para salir del sistema \n : ").upper()
            if tamano_tarea == "APAGAR":
                mostrar_informe()  # Reutilización de función
                print("Saliendo del sistema")
                break
            else:
                tamano_tarea = int(tamano_tarea)
            if tamano_tarea <= 0:
                print("Tarea corrupta\nIntenta de nuevo")
                continue
        except ValueError:
            print("Tarea corrupta\nIntenta de nuevo")
            continue
            
        # Fase 2: Captura y validación del nodo de destino
        try:
            nodo_procesamiento = int(input("Indica el nodo que desea para procesar la información (1, 2 o 3): "))
        except ValueError:
            print("El nodo no responde...")
            nodos['espera'].append(tamano_tarea) 
            continue
            
        # Fase 3: Procesamiento y Despacho (Invocación de la función)
        despachar_tarea(nodo_procesamiento, tamano_tarea)
                
    except KeyboardInterrupt:
        print("\n🛑 Bloqueo de Emergencia Detectado")
        print("Informe de nodos en el último estado conocido:")
        mostrar_informe()  # Reutilización de función
        break


