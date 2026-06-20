'''
Contexto: Un restaurante organiza su menú en un diccionario principal 
donde las llaves son las categorías ("entradas", "fondos", etc.), y 
el valor de cada categoría es una lista de diccionarios (los platos).

🎯 Instrucciones de Funcionamiento
Crea el sistema de gestión con las siguientes reglas:

    Crear (Añadir Plato): Solicita la categoría, el nombre del plato y el precio.

        Condición: Si la categoría ya existe, añade el plato a su lista. Si la 
        categoría no existe, créala automáticamente y luego añade el plato.

        Control de errores: El precio debe ser obligatoriamente un número decimal 
        positivo. Si ingresan letras o números negativos, bloquea el registro y 
        vuelve a solicitar el precio.

Leer (Imprimir Carta): Muestra el menú agrupado por categorías. Si el menú 
está completamente vacío, muestra un aviso indicándolo.

Actualizar (Cambio de Precio): Pide el nombre de un plato y el nuevo precio.

    Condición: Debes buscar el plato en todas las categorías. Si lo encuentras, 
    actualiza su precio. Si terminas de revisar todo el menú y no existe, avisa al usuario.

    Control de errores: Aplica la misma protección numérica para el nuevo precio.

Borrar (Retirar Plato): Solicita el nombre de un plato para eliminarlo.

    Condición Crítica: Si al eliminar el plato, su categoría se queda completamente 
    vacía (sin más platos), debes eliminar también la categoría completa del 
    diccionario principal.
'''

menu = {
    "bebidas": [{"nombre": "agua", "precio": 2.0}, {"nombre": "jugo", "precio": 3.5}],
    "postres": [{"nombre": "flan", "precio": 4.0}]
}
def imprimirMenu():
    print("-"*50) 
    if not menu:
        print("El menú esta vacio")
        return
    for categoria, platos in menu.items():
        print(f"----{categoria}----")
        for plato in platos:
            print(f"{plato['nombre']} = {plato['precio']}")
def mostrarPlato():
    print("-"*50) 
    for categoria, platos in menu.items():
        print(f"----{categoria}----")
        for plato in platos:
            print(plato)

def añadirPlato():
    activo = True
    while activo:
        # mostrarPlato()
        print("-"*50) 
        categoria = input("Indica la categoria del plato a agregar \n--|")
        nombre = input("Indica el nombre del plato a agregar \n--|")
        try:
            precio = float(input("Indica precio del plato a agregar \n--|"))
        except ValueError:
            print("Solo se permiten números en este campo")
            print("Registro bloqueado, vuelve a intentarlo")
            continue
        if precio < 0:
            print("Solo puede ingresar números positivos")
            print("Registro bloqueado, vuelve a intentarlo")
            continue
        if categoria in menu:
            menu[categoria].append({'nombre': nombre, 'precio' : precio})
            break
        else:
            menu[categoria] = [{'nombre': nombre, 'precio' : precio}]
            break
def gestionMenu():
    while True:
        print("-"*50)   
        try:
            print('''
            BIBLIOTECA
        1. Añadir plato
        2. Imprimir carta
        3. Cambio de precio
        4. Retirar plato
        5. Salir
    ''')
            op = input("    Seleccione una opción --|")
            match op:
                case "1":
                    añadirPlato()
                case "2":
                    imprimirMenu()
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    print("Saliendo de la biblioteca")
                    break
                case _:
                    print("Ingreso Inválido")
        except KeyboardInterrupt:
            print(f"\n{"-"*20}|Sistema Bloqueado|{"-"*20}")
            break

gestionMenu()




