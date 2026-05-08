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
def evaluacion_metodo_de_venta(venta): 
    while venta < 1 or venta > 2:
        print("Solo puede ingresar 1 o 2")
        venta = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
: '''))
    match venta:
        case 1:
            return "Nacional"
        case 2:
            return "Internacional"
def evaluacion_peso(peso_funcion):
    while peso_funcion < 0:
        print("Solo puede ingresar números positivos")
        peso_funcion = int(input("Ingrese el peso: "))
    return peso_funcion

while True:
    try:
        peso = int(input("Ingrese el peso en gramos: "))
        peso_producto = evaluacion_peso(peso)
        break
    except: 
        print("Solo se pueden ingresar números")
# print(peso_producto)

while True:
    try:
        metodo = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
: '''))
        metodo_de_venta = evaluacion_metodo_de_venta(metodo)
        break
    except:
        print("Solo pueden ingresar números, 1 o 2")
print(metodo_de_venta)

