'''
Contexto: En un centro de datos es vital saber 
exactamente qué hardware está instalado en cada 
servidor para planificar actualizaciones.

Requisitos del programa:

Crea un diccionario donde las llaves sean los nombres 
de los servidores (por ejemplo: 'Rack_A1', 'Rack_B5') 
y los valores sean listas que almacenen los strings de 
los componentes instalados (ej. ['Intel_Xeon', 'RAM_64GB', 
'SSD_2TB']). Puedes iniciar el diccionario con algunos 
servidores preexistentes.

Diseña una función que permita registrar un componente 
nuevo en un servidor específico. La función debe validar 
defensivamente que el servidor exista y que el componente 
no esté duplicado en su lista.

Diseña otra función que permita dar de baja (eliminar) 
un componente viejo de un servidor, asegurándote de que 
el componente realmente exista antes de intentar borrarlo.

Implementa el bucle principal interactivo que le permita 
al operador elegir si quiere AGREGAR, ELIMINAR o ver el 
INVENTARIO completo. El programa debe cerrarse de forma 
segura cuando se escriba CERRAR.
'''




servidores = {
    'Rack_A1': ['Intel_Xeon', 'RAM_64GB', 'SSD_2TB'],
    'Rack_A2' : ['AMD_EPYC', 'RAM_128GB', 'SSD_4TB']
}

def registrar_componente(servidor, new_hardware):
    print("-"*50)
    if servidor in servidores.keys():
        if new_hardware not in servidores[servidor]:
            servidores[servidor].append(new_hardware)
            print(f"El componente {new_hardware} a sido registrado con exito")
        else:
            print("El componente ya existe en el servidor")
    else:
        print("El servidor ingresado no existe")
    mostrar_servidores()

def eliminar_componentes(servidor, del_hardware):
    print("-"*50)
    if servidor in servidores.keys():
        if del_hardware in servidores[servidor]:
            servidores[servidor].remove(del_hardware)
            print(f"El componente {del_hardware} a sido dado de baja")
        else:
            print("El componente NO existe en el servidor")
    else:
        print("El servidor ingresado no existe")
    mostrar_servidores()

def mostrar_servidores():
    print("-"*50)
    for serv, hard in servidores.items():
        print(f"Servidor: {serv} | Componentes: {hard}")

def cerrar_programa(ingreso):
    print("-"*50)
    ingreso = ingreso.upper()
    if ingreso == "CERRAR":
        print("Cerrando el programa...")
        return False
    else:
        return True

def menu():    
    activo = True
    while activo:
        print("-"*50)
        print("CENTRO DE DATOS")
        print("1.AGREGAR COMPONENTE \n2.ELIMINAR COMPONENTE \n3.VER INVENTARIO")
        print("Para cerrar el programa escribe CERRAR")
        op = (input("Indica que opercación quieres realizar \n : ")).upper()
        match op:
            case '1':
                servidor = input("Ingresa el nombre del servidor que quieres modificar: ")
                activo = cerrar_programa(servidor)
                if activo == False: break
                new_hardware = input("Ingresa el nombre del nuevo componente: ")
                activo = cerrar_programa(new_hardware)
                if activo == False: break
                registrar_componente(servidor, new_hardware)
            case '2':
                servidor = input("Ingresa el nombre del servidor que quieres modificar: ")
                activo = cerrar_programa(servidor)
                if activo == False: break
                del_hardware = input("Ingresa el nombre del componente a dar de baja: ")
                activo = cerrar_programa(del_hardware)
                if activo == False: break
                eliminar_componentes(servidor, del_hardware)
            case '3':
                mostrar_servidores()
            case "CERRAR":
                print("Cerrando el programa...")
                break
            case _:
                print("Opción Inválida")

menu()
