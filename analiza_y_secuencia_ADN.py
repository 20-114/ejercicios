
adn_ingresado = input('''Ingrese una cadena de ADN.
Considere que la bases nitrogenadas de una cadena normal son;
- Adenina  (A)
- Timina   (T)
- Citosina (C)
- Guanina  (G)
- Cualuier ingreso distinto de las bases se considera un amutación
ADN: ''')

adn_ingresado_upper = adn_ingresado.upper()

contA = 0
contT = 0
contC = 0
contG = 0
cont_mutacion = 0

cadena_complementaria = ""

for base in adn_ingresado_upper:
    if base == "A":
        contA += 1
        cadena_complementaria += "T"
    elif base == "T":
        contT += 1
        cadena_complementaria += "A"
    elif base == "C":
        contC += 1
        cadena_complementaria += "G"
    elif base == "G":
        contG += 1
        cadena_complementaria += "C"
    else:
        if cont_mutacion == 0: 
            print("\n¡Alerta: Anomalía detectada!")
        cont_mutacion += 1
        cadena_complementaria += "X"

total_bases_mutaciones = len(adn_ingresado_upper)
contenido_GC = contG + contC

if total_bases_mutaciones > 0:
    porcentaje_GC = (contenido_GC * 100) / total_bases_mutaciones
else:
    porcentaje_GC = 0

print(f'''
Conteo de bases:
Adenina = {contA}
Timina = {contT}
Citosina = {contC}
Guanina = {contG}
Mutaciones = {cont_mutacion}

Porcentaje de GC = {porcentaje_GC}%

ADN ingresado        =  {adn_ingresado_upper}
Hebra complementaria =  {cadena_complementaria}''')
