
chocman = 500 #pylint: disable=invalid-name
triton = 600 #pylint: disable=invalid-name
cocacola_500 = 1500 #pylint: disable=invalid-name
jumex = 1400 #pylint: disable=invalid-name

def pagar_producto(nuevo_producto):
    '''pago de produtco'''
    nuevo_total = nuevo_producto
    pago = input(f"Su total a pagar es {nuevo_total}. \nIngrese el dinero: ")
    return nuevo_total

print("Maquina Expendedora")
producto = int(input(f'''1) Chocman $ {chocman} \n2) Triton $ {triton} \n3) Coca cola $ {cocacola_500} \n4) Jumex $ {jumex} \n '''))

match producto:
    case 1:
        total = pagar_producto(chocman)
        
    # case 2:
    # case 3:
    # case 4:


