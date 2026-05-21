'''
Contexto: Eres la inteligencia artificial a cargo del muelle de 
abordaje de una estación minera espacial. Debes gestionar la 
asignación de la única bahía de carga disponible, verificar la 
legalidad de los cargamentos y cobrar los aranceles correspondientes.

Reglas de Funcionamiento:

Estado Operativo Constante: La terminal inicia con 200 unidades 
de energía de fusión y 1000 créditos estelares. El sistema debe 
operar continuamente procesando transacciones una a una. Si la 
energía llega a 0 o menos, el sistema se bloquea inmediatamente 
por seguridad.

Gestión de la Bahía de Carga: Solo hay espacio para una nave a la 
vez. Debes controlar si la bahía está ocupada o libre mediante el 
estado del sistema. No se puede recibir una nave si la bahía está 
llena, ni se puede despachar si está vacía.

Enrutador Estructural de Operaciones: En cada ciclo, la terminal 
solicita un código de comando numérico para activar uno de sus 4 módulos principales:

Módulo 1: Registro y Anclaje

    Solo ejecutable si la bahía está vacía. Genera un identificador 
    numérico aleatorio para el cargamento (entre 1000 y 9999) y solicita 
    al operario el peso estimado de la nave.

    Si el peso ingresado es menor o igual a cero, se considera una 
    lectura fantasma, consume 10 unidades de energía como penalización 
    y no ocupa la bahía. Si es válido, la bahía cambia a estado ocupado.

Módulo 2: Escaneo Biométrico y Criptográfico

    Solo ejecutable si la bahía está ocupada. Solicita una cadena de 
    texto que representa el "Manifiesto de Carga".

    Regla de Integridad: Si el largo total de la cadena de texto es 
    un número impar, el manifiesto es sospechoso.

    Regla de Contrabando: Si el residuo de dividir la longitud de la 
    cadena por 4 es exactamente cero, el cargamento contiene materiales 
    peligrosos. El sistema debe emitir una alarma visual y cobrar una multa
    automática de 200 créditos al propietario (restando o sumando al balance
    de la estación).

Módulo 3: Despacho y Liquidación de Aranceles

    Solo ejecutable si la bahía está ocupada. El sistema genera de forma aleatoria 
    el peso real verificado por la báscula de la estación (un número entre -20 y +20 
    en comparación con el peso estimado inicialmente).

    Calcula la distancia numérica sin signo (desviación absoluta) entre el peso estimado 
    y el peso real.

    Por cada unidad de desviación absoluta, la estación cobra 15 créditos de tarifa de 
    calibración. Tras mostrar el balance final del viaje, la bahía vuelve a quedar completamente libre.

Módulo 4: Diagnóstico y Recarga

    Muestra el estado actual de la energía, los créditos, si la bahía está ocupada y 
    cuántas naves ilegales se han detectado en el turno actual.

    Permite al usuario inyectar energía al sistema comprándola con créditos de la estación: 
    cada unidad de energía cuesta 5 créditos.

Seguridad de Datos de la Terminal: Si el operario introduce texto en los campos de peso, o 
comandos inexistentes en el menú, la terminal debe absorber el impacto del error, advertir 
sobre la "interferencia estelar", restar 5 unidades de energía debido al fallo de lectura 
y continuar con el siguiente ciclo.
'''

import random
import time

naves_ilegales = 0
multa_mod2 = 200
multa_mod3 = 15
multa_total = 0
energia = 200
creditos = 1000

bahia = 0

while energia > 0:
    try:
        print("[Módulos Disponibles]")
        if bahia == 0: #bahia vacia
            print("1) [Registro y Anclaje]")
        elif bahia == 1: #bahia ocupada
            print("2) [Escaneo Biométrico y Criptográfico]")
            print("3) [Despacho y Liquidación de Aranceles]")
        print("4) [Diagnóstico y Recarga]")
        mod = int(input("[Selecciona el módulo que deseas ejecutar] \n----| "))          
        match mod:
            case 1:
                print("-"*25)
                if bahia == 1:
                    print("--Módulo deshabilitado por bahia llena--")
                    time.sleep(1)
                    continue
                else:
                    id_cargamento = random.randint(1000, 9999)
                    peso_nave = int(input("Operador, ingrese el peso de su nave \n----| "))
                    if peso_nave <= 0:
                        print("[Lectura fantasma]")
                        energia -= 10                
                    else:
                        print(f"[Nave con id {id_cargamento}, con peso de {peso_nave}kg]")
                        bahia = 1 #espacio utilizado               
            case 2:
                print("-"*25)
                if bahia == 0:
                    print("--Módulo deshabilitado por bahia vacia--")
                    time.sleep(1)
                    continue
                else:
                    manifiesto_carga = input("Ingrese el manifiesto de la carga: \n| ")
                    if len(manifiesto_carga) % 2 != 0:
                        time.sleep(0.5)
                        print("Manifiesto Sospechoso")
                    elif len(manifiesto_carga) % 4 == 0:
                        time.sleep(0.5)
                        naves_ilegales += 1
                        print("[Identificados materiales peligrosos dentro del cargamento]")
                        time.sleep(0.5)
                        print("[Se le cobra una multa automatica de 200 creditos por su falta]")
                        multa_total += multa_mod2
                        time.sleep(0.5)
                    else:
                        time.sleep(0.5)
                        print("[Escaneo realiazdo sin inconvenientes]")
            case 3:
                print("-"*25)
                if bahia == 0:
                    print("--Módulo deshabilitado por bahia vacia--")
                    time.sleep(1)
                    continue
                else:
                    peso_real_nave = random.randint(peso_nave-20, peso_nave+20)
                    print("[Sistema identificando el peso real de la nave...]")
                    time.sleep(2)
                    print(f"[El peso real de la nave es de {peso_real_nave}kg]")
                    dif_peso = peso_nave - peso_real_nave
                    abs_dif_peso = abs(dif_peso)
                    creditos_por_peso = 0
                    if abs_dif_peso > 0:
                        creditos_por_peso = abs_dif_peso * multa_mod3
                        print(f"[Existe una diferencia de {abs_dif_peso}kg con el peso declarado]")
                        time.sleep(0.5)
                        print("[Se le cobrarn 15 creditos por cada unidad de diferencia]")
                        time.sleep(0.5)
                        print(f"Creditos por diferencia a cobrar: {creditos_por_peso}")
                        multa_total += creditos_por_peso
                    time.sleep(0.5)
                    print(f"Total a pagar: {multa_total}")
                    creditos += multa_total
                    bahia = 0
                    multa_total = 0
            case 4:
                print("-"*25)
                print("[Analizando el estado de la Terminal...]")
                time.sleep(1)
                print(f"Energía: {energia} | Creditos: {creditos}")
                print(f"Naves ilegales iedntificadas: {naves_ilegales}")
                if bahia == 0:
                    print("Bahia vacia")
                elif bahia == 1:
                    print("Bahia ocupada")
                time.sleep(1)
                while True:
                    try:
                        print("[¿Inyectar energía al sistema? 5 creditos por u/energía]")
                        compra = int(input("1) Si \n2) No \n----| "))
                        match compra:
                            case 1:
                                uni_a_comprar = int(input("¿Cuantas unidads de energía desea comprar? ---| "))
                                print(f"[{uni_a_comprar} unidades de energía por {uni_a_comprar*5} creditos]")
                                energia += uni_a_comprar
                                creditos -= (uni_a_comprar*5)
                                break
                            case 2:
                                break
                            case _:
                                print("Opción de compra invalida")
                    except ValueError:
                        print("Ingreso de datos invalidos")
            case _:
                print("¡Interferencia estelar detectada!")
                energia -= 5
    except:
        print("¡Interferencia estelar detectada!")
        energia -= 5




