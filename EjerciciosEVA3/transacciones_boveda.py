'''
El Desafío: Gestionar un flujo financiero continuo 
controlando saldos, previniendo sobregiros y 
filtrando operaciones nulas.

Comportamiento esperado:

La bóveda del servidor inicia con un saldo base 
de 150 créditos.

El sistema debe pedir transacciones una y otra vez 
de forma indefinida. Este ciclo solo se detiene si 
ocurre una de dos condiciones: el saldo llega a 0 
créditos o el usuario escribe la palabra exacta SALIR.

Al evaluar el monto introducido:

Si el usuario ingresa texto (que no sea la palabra 
de salida), el sistema debe reportarlo como monto 
inválido sin alterar el saldo ni cerrar el programa.

Si el monto es igual a 0, la operación se deniega 
por ser nula.

Si el monto es un valor negativo, representa un 
retiro. El sistema debe comprobar si hay fondos 
suficientes para cubrir esa cantidad exacta. Si 
hay saldo, se descuenta; si no, se rechaza por 
fondos insuficientes.

Si el monto es positivo, representa un depósito 
y se suma directamente al saldo actual.
'''

creditos = 150

while True:
    print(creditos)
    entrada = input("Ingrese los créditos de la transacción. \nIngrese SALIR si no desea realizar más operaciones. \n :  ").upper()

    if entrada == "SALIR":
        transaccion = "SALIR"
    else:
        try:
            transaccion = int(entrada)
        except ValueError:
            transaccion = entrada
    match transaccion:
        case "SALIR":
            break
        case int():
            if transaccion > 0:
                creditos += transaccion
                print(f"Deposito de {transaccion} créditos realizado")
            elif transaccion < 0:
                if creditos >= abs(transaccion):
                    creditos -= abs(transaccion)
                    print(f"Retiro de {transaccion} créditos realizado")
                else:
                    print("Operación rechazada por fondos insuficientes")
            else:
                print("Operación nula")
        case _: 
            print("Monto Inválido")
    if creditos <= 0:
        print("Tarjeta sobregirada")
        break
