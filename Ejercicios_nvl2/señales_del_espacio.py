'''
Contexto: Has recibido una cadena de texto que contiene una transmisión de 
una civilización lejana. Tu trabajo es extraer los datos numéricos ocultos en el ruido.

Reglas de Funcionamiento:

Recepción de Señal: Solicita al usuario una cadena de texto. 
Si la longitud de la cadena es inferior a 12 caracteres, el sistema 
debe rechazarla por ser "ruido insuficiente" y pedir una nueva hasta que cumpla el requisito.

Procesamiento Secuencial: El sistema debe analizar cada elemento 
de la cadena, uno por uno, de principio a fin.

Extracción Selectiva: * El comportamiento del análisis cambia según 
la posición del carácter:
* En posiciones pares, el sistema debe intentar tratar ese carácter como 
un número. Si lo logra, debe sumarlo a un acumulador de "Energía de Señal".
* En posiciones impares, el sistema debe simplemente identificar si el 
carácter es una vocal o no.

Gestión de Errores Internos: Dado que la cadena contiene texto y números 
mezclados, el sistema debe ser capaz de intentar la conversión numérica sin detenerse 
ni mostrar errores técnicos si encuentra una letra donde esperaba un número. Simplemente 
debe saltar ese elemento y continuar.

Resultado del Análisis: Al finalizar el recorrido, debe mostrar la suma total 
obtenida y el promedio de valor por cada carácter de la cadena original.
'''
import random

while True:
    try:
        codigo_señal = input("Ingresa la señal: ")
        print("-"*25)
        if len(codigo_señal) < 12:
            print("Ruido insuficiente")
        else:
            break
    except ValueError:
        print("Ingreso Invalido")

energia_de_señal = 0.0
for i in codigo_señal:
    if codigo_señal.index(i) % 2 == 0:
        if i in "1234567890": # == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            print(i)
            energia_de_señal += float(i)
    elif codigo_señal.index(i) % 2 != 0:
        if i in "aeiou": #== "a"or i == "e"or i == "i"or i == "o"or i == "u":
            print(f"{i} es vocal")
        elif i in "bcdfghjklmnñpqrstvwxyz":
            print(f"{i} NO es vocal")

promedio_valor_caracteres = energia_de_señal / len(codigo_señal)
print(f"Suma total obtenida: {energia_de_señal}")
print(f"Promedio de los valores: {promedio_valor_caracteres}")


# =============================================================================
# VERSIÓN CORREGIDA POR GEMINI CODE ASSIST (Para comparación)
# =============================================================================
'''
DIFERENCIAS CLAVE:
1. Uso de enumerate(): Fundamental para obtener el índice real de cada carácter, 
   especialmente cuando hay caracteres repetidos.
2. Bloque Try-Except: Implementa la "Gestión de Errores Internos" de forma 
   profesional, intentando convertir a número y saltando si falla.
3. Soporte de Mayúsculas: Se añadieron vocales en mayúsculas para mayor robustez.
4. Limpieza de Lógica: Se reemplaza el 'elif' redundante por un 'else' simple.
'''

# def version_corregida():
#     while True:
#         # Validación de longitud (Recepción de Señal)
#         señal = input("\n[Nueva Entrada] Ingrese la señal: ")
#         if len(señal) < 12:
#             print("Ruido insuficiente (mínimo 12 caracteres).")
#             continue
#         break
#
#     energia_total = 0.0
#     vocales = "aeiouAEIOU"
#
#     print("\n--- Iniciando Procesamiento Secuencial ---")
#     for indice, caracter in enumerate(señal):
#         # En posiciones pares (0, 2, 4...)
#         if indice % 2 == 0:
#             try:
#                 # Intento de extracción numérica (Gestión de Errores Internos)
#                 valor = float(caracter)
#                 energia_total += valor
#                 print(f"Índice {indice}: '{caracter}' sumado a Energía.")
#             except ValueError:
#                 # Salto silencioso si no es un número
#                 pass
#         # En posiciones impares (1, 3, 5...)
#         else:
#             if caracter in vocales:
#                 print(f"Índice {indice}: '{caracter}' es una vocal.")
#
#     # Resultado del Análisis
#     promedio = energia_total / len(señal)
#     print(f"\nSuma total de Energía: {energia_total}")
#     print(f"Promedio por carácter original: {promedio:.2f}")



#  Explicación de Gemini
# ¿Por qué mi versión es más robusta?
# El error de .index(): Si tu señal fuera 10101010101010, tu código original 
# siempre diría que el segundo 1 está en la posición 0 (par), porque .index() busca 
# desde el inicio de la cadena. Al usar enumerate(codigo_señal), garantizamos que 
# cada carácter se procese con su posición real.
# 
# Conversión de Datos: En lugar de verificar si el carácter está en la cadena 
# "1234567890", utilizo float(caracter) dentro de un try-except. Esto es más 
# eficiente y sigue mejor la regla de "intentar la conversión sin detenerse".
# 
# Promedio Preciso: He formateado el promedio a dos decimales (:.2f) para 
# que la salida sea más legible, algo común en sistemas de monitoreo.








