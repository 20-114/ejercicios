'''Fabrica de enlatados
Se necesita hacer el algoritmo de productos enlatados
Se debe consultar el peso del producto (en gramos) (solo valores positivos)
El porcentaje de sodio en el (solo valores entre 1 y 100)
y si se va a vender nacional o internacionalmente

Considerar los criterios en la siguiente tabla

menos de 500gr -> lata normal
más de 500 hasta 1500gr -> lata mediamás de 1500gr -> lata grande
si el Na es menos del 5% -> lata queda igual
si Na esta entre 5 y 8% -> lata especial
si tiene 9 o más -> lata acorazada
A las latas internacionales se les debe pegar un sticker de validación sanitaria

Ej: 800gr, 7%, 2(internacional) -> lata mediana especial con sticker sanitario
'''
try:
    peso_producto = int(input("Ingrese el peso en gramos: "))
    while peso_producto <0:
        if peso_producto < 0:
            print("Solo puede ingresar números positivos")
            peso_producto = int(input("Ingrese el peso: "))
except ValueError:
    print("Solo se pueden ingresar números")


metodo_de_venta = ""
try:
    venta = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
'''))
    while 1 > venta > 2:
        if venta < 1:
            print("Solo puede ingresar 1 o 2")
            venta = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
'''))
        elif venta > 2:
            print("Solo puede ingresar 1 o 2")
            venta = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
'''))
    match venta:
        case 1:
            metodo_de_venta = "Nacional"
        case 2:
            metodo_de_venta = "Internacional"
except TypeError:
    print("Solo puede ingresar números, 1 o 2")




