'''Fabrica de enlatados
Se necesita hacer el algoritmo de productos enlatados
Se debe consultar el peso del producto (en gramos) (solo valores positivos)
El porcentaje de sodio en el (solo valores entre 1 y 100)
y si se va a vender nacional o internacionalmente

Considerar los criterios en la siguiente tabla

menos de 500gr -> lata normal
más de 500 hasta 1500gr -> lata mediana
más de 1500gr -> lata grande
si el Na es menos del 5% -> lata queda igual
si Na esta entre 5 y 8% -> lata especial
si tiene 9 o más -> lata acorazada
A las latas internacionales se les debe pegar un sticker de validación sanitaria

Ej: 800gr, 7%, 2(internacional) -> lata mediana especial con sticker sanitario
'''
def evaluacion_peso(peso_funcion):
    while peso_funcion < 0:
        print("Solo puede ingresar números positivos")
        peso_funcion = float(input("Ingrese el peso: "))
    return peso_funcion
def evaluación_Na(sodio):
    while sodio < 0 or sodio > 100:
        if sodio < 0:
            print("Solo se pueden ingresar números positivos")
            sodio = float(input("Ingrese el porcentaje de sodio: "))
        if sodio > 100:
            print("El valor máximo es 100")
            sodio = float(input("Ingrese el porcentaje de sodio: "))
    return sodio
def evaluacion_metodo_de_venta(metodo_funcion): 
    while metodo_funcion < 1 or metodo_funcion > 2:
        print("Solo puede ingresar 1 o 2")
        metodo_funcion = int(input('''
Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
: '''))
    match metodo_funcion:
        case 1:
            return ""
        case 2:
            return "con sticker sanitario"


while True:     #control de errores de peso de la lata
    try:
        peso = int(input("Ingrese el peso en gramos: "))
        peso_producto = evaluacion_peso(peso)
        break
    except: 
        print("Solo se pueden ingresar números")
# print(peso_producto)
while True:     #control de errores del porcentaje de sodio
    try:
        porcentaje_Na = float(input("Ingrese el porcentaje de sodio: "))
        porcentaje_sodio = evaluación_Na(porcentaje_Na)
        break
    except:
        print("Solo se pueden ingresar números")
# print(f"{porcentaje_sodio}%")
while True:     #control de errores metodo de venta
    try:
        metodo = int(input('''Indica si el producto se vendera de manera nacional o internacional:
1. Nacional
2. Internacional
: '''))
        metodo_de_venta = evaluacion_metodo_de_venta(metodo)
        break
    except:
        print("Solo pueden ingresar números, 1 o 2")
# print(metodo_de_venta)

tamaño = ""
tipo = ""
# venta_publico = ""
if peso_producto < 500: #tamaño de lata
    tamaño = "normal"
elif peso_producto <= 1500:
    tamaño = "mediano"
else:
    tamaño = "grande"

if porcentaje_sodio < 5: #tipo de lata
    tipo = ""
elif porcentaje_sodio <= 8:
    tipo = "especial "
else:
    tipo = "acorazada "

formato_final = f"{tipo}de tamaño {tamaño} {metodo_de_venta}"
print(f"Lata {formato_final}")
