'''
Contexto: Un software de trading financiero registra el portafolio 
de un usuario en un diccionario, donde la clave es el código (ticker) 
de la moneda y el valor es la cantidad de activos. Los códigos 
internacionales financieros son muy estrictos con su formato.

🎯 Instrucciones de Funcionamiento
Diseña un sistema que permita actualizar los activos del portafolio 
mediante dos entradas de texto: el código de la moneda y la cantidad 
de cambio (que puede ser positiva o negativa). El sistema debe operar 
bajo estas reglas:

Regla de Longitud: El código de la moneda debe tener estrictamente 
entre 3 y 5 caracteres de largo. Cualquier texto con menos de 3 o 
más de 5 caracteres se considera inválido.

Regla de Símbolos: El código solo puede estar compuesto por letras del 
abecedario. No se permiten espacios, números ni caracteres especiales 
(como guiones o puntos).

Normalización y Mutación: Si el código es válido, conviértelo completamente 
a mayúsculas para buscarlo en el diccionario.

Si la moneda ya existe, suma o resta la cantidad indicada a su valor actual.

Si la moneda no existe y la cantidad es positiva, agrégala como una nueva 
clave en el diccionario.

Si tras realizar una resta la cantidad de esa moneda llega a cero o menos, 
la clave debe ser completamente removida del portafolio.
'''

portafolio = {
    "BTC": 0.5,
    "ETH": 2.3
}


while True:
    clave = input("Indica que cripto quieres actualiazr: ")
    
    if len(clave) < 3 or len(clave) > 5:
        print("Codigo de la moneda inválido")
        continue
    if not clave.isalpha():
        print("El codigo solo puede contener letras")
        continue
    clave = clave.upper()
        
    if clave in portafolio:
        while True:
            try:
                cantidad = float(input(f"Indica que cantidad de {clave} quieres adicionar o restar \n : "))
            except ValueError:
                print("Ingreso Inválido")
                continue
            break
        portafolio[clave] += cantidad
        if portafolio[clave] <= 0:
            del portafolio[clave]
    else:
        while True:
            try:
                cantidad = float(input(f"Indica que cantidad de {clave} quieres adicionar o restar \n : "))
            except ValueError:
                print("Ingreso Inválido")
                continue
            if cantidad <= 0:
                print("Al ser una moneda no resgistrada, solo puedes ingresar montos positivos")
                continue
            portafolio[clave] = cantidad
            break

    break

for cripto, cantidad in portafolio.items():
    print(f"Cripto : {cripto} | Cantida : {cantidad}")

