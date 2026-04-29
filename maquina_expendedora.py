import time

chocman = 500 #pylint: disable=invalid-name
triton = 600 #pylint: disable=invalid-name
cocacola_500ml = 1500 #pylint: disable=invalid-name
jumex = 1400 #pylint: disable=invalid-name

cont_500 = 0
cont_100 = 0
cont_50 = 0
cont_10 = 0

def pagar_producto(nuevo_producto):
    '''pago de produtco'''
    nuevo_total = nuevo_producto
    print(f"Su total a pagar es {nuevo_total}. \nIngrese el dinero: ")
    dinero_ingresado = 0
    while dinero_ingresado < nuevo_total:
        moneda = int(input("1) 500 \n2) 100 \n3) 50 \n4) 10 \n "))
        match moneda:
            case 1:
                dinero_ingresado += 500
            case 2:
                dinero_ingresado += 100
            case 3:
                dinero_ingresado += 50
            case 4:
                dinero_ingresado += 10
        print(f"Pagado: ${dinero_ingresado} pesos")
    return dinero_ingresado

print("Maquina Expendedora")
producto = int(input(f'''1) Chocman $ {chocman} \n2) Triton $ {triton} \n3) Coca cola $ {cocacola_500ml} \n4) Jumex $ {jumex} \n '''))

match producto:
    case 1:
        total_pagado = pagar_producto(chocman)
        producto_especifico = chocman        
    case 2:
        total_pagado = pagar_producto(triton)        
        producto_especifico = triton        
    case 3:
        total_pagado = pagar_producto(cocacola_500ml)        
        producto_especifico = cocacola_500ml        
    case 4:
        total_pagado = pagar_producto(jumex)
        producto_especifico = jumex        

print("Procesando pago...")
# time.sleep(2)

if total_pagado > producto_especifico:
    vuelto = total_pagado - producto_especifico
    vuelto_impreso = vuelto
    while vuelto != 0:
        if vuelto >= 500:
            vuelto -= 500
            cont_500 += 1
        elif vuelto >= 100:
            vuelto -= 100
            cont_100 += 1
        elif vuelto >= 50:
            vuelto -= 50
            cont_50 += 1
        elif vuelto >= 10:
            vuelto -= 10
            cont_10 += 1
print(f'''Su vuelto es de {vuelto_impreso}: 
      {cont_500} monedas de 500
      {cont_100} monedas de 100
      {cont_50} monedas de 50
      {cont_10} monedas de 10''')
        


