'''
Contexto: Los carritos de compras no son diccionarios planos; 
suelen ser una lista que contiene diccionarios, donde cada 
diccionario representa un artículo con propiedades mutables.

🎯 Tu Misión
Crea un sistema con 3 funciones rápidas:

agregar_o_actualizar(id_prod, nombre, precio): Si el id_prod 
ya existe en el carrito, incrementa su cantidad en 1. Si no 
existe, crea el diccionario del nuevo producto con cantidad 
inicial 1 y agrégalo al final de la lista.

modificar_cantidad(id_prod, nueva_cantidad): Busca el producto 
por su ID. Actualiza su cantidad. Defensa: Si la nueva cantidad 
ingresada es 0 o menor, el producto debe ser eliminado por completo 
de la lista del carrito usando su índice.

calcular_total(): Devuelve el precio total acumulado (multiplicando 
precio por cantidad de cada artículo). Tip pro: Si te animas, ¡intenta 
usar una función lambda aquí!
'''


carrito = [
    {'id': 101, 'nombre': 'Teclado Mecánico', 'precio': 45.0, 'cantidad': 1},
    {'id': 102, 'nombre': 'Mouse Gamer', 'precio': 25.0, 'cantidad': 2}
]

def agregar_o_actualizar(id_prod, nombre, precio):
    print("°"*15)
    if carrito:
        for producto in carrito:
            if id_prod == producto['id']:
                producto['cantidad'] += 1
                break
        else:
            carrito.append({'id' : id_prod, 'nombre' : nombre, 'precio' : precio, 'cantidad' : 1 })
    else:
        print("Carrito vacio")
    mostrar_carrrito()

def modificar_cantidad(id_prod, nueva_cantidad):
    print("°"*15)
    for producto in carrito:
        if id_prod == producto['id']:
            if nueva_cantidad > 0:
                producto['cantidad'] = nueva_cantidad
                
            else:
                carrito.remove(producto)
            break
    else:
        print("El producto no existe en el carrito de compras")
    mostrar_carrrito()

            

def calcular_total():
    total_bruto = 0
    iva = 1.19
    print("-"*16,"BOLETA", "-"*16)
    for producto in carrito:
        precio = producto['precio']
        cantidad = producto['cantidad']
        total_producto = precio * cantidad
        total_bruto += total_producto
        print(f"{producto['nombre']} | {producto['cantidad']} unidades | precio: {total_producto}")
    total_neto = total_bruto * iva
    print(f"Total sin iva: {total_bruto}")
    print(f"Total a pagar: {total_neto}")

def mostrar_carrrito():
    for producto in carrito:
        print(f"{producto['id']} | {producto['nombre']} | ${producto['precio']} | {producto['cantidad']} unidades")

def  menu():
    while True:
        print("Carrito de compras")
        print("1. Agregar un producto \n2. Modificar cantidad de un producto \n3. Total a pagar")
        try:
            op = input(" : ")
            match op:
                case "1":
                    print("-"*40)
                    mostrar_carrrito()
                    while True:
                        try:
                            id_producto = int(input("Ingresa el id del producto para agregarlo al carrito\n : "))
                        except ValueError:
                            print("Solo puede ingresar números enteros positivos")
                            continue
                        nombre_producto = input("Ingresa el nombre del producto\n : ")
                        break
                    while True:
                        try:
                            precio_producto = float(input("Ingresa el precio del producto\n : "))
                        except ValueError:
                            print("Solo puede ingresar números positivos")
                            continue
                        agregar_o_actualizar(id_producto, nombre_producto, precio_producto)
                        break
                case "2":
                    mostrar_carrrito()
                    print("-"*40)
                    while True:
                        try:
                            id_producto = int(input("Ingresa el id del producto al que desea cambiar la cantidad\n : "))
                            nueva_cantidad = int(input("Indica cuantos productos quieres agregar\n : "))
                        except ValueError:
                            print("Solo puede ingresar números enteros positivos")
                            continue
                        modificar_cantidad(id_producto, nueva_cantidad)
                        break
                case "3":
                    print("-"*40)
                    calcular_total()
                    break
                case _:
                    print("Opción Inválida")
        except KeyboardInterrupt:
            print("Carrito Bloqueado")
            break
menu()
