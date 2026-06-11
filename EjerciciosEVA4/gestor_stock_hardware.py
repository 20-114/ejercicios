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

def registrar_servidor():
    servidor = input("Ingresa el nombre del servidor que quieres modificar: ")
    if servidor in servidores.keys():
        new_hardware = input("Ingresa el nombre del nuevo componente: ")
        if new_hardware not in servidores[servidor]:
            servidores[servidor].append(new_hardware)
            print(servidores[servidor])
        else:
            print("El componente ya existe en el servidor")
    else:
        print("El servidor ingresado no existe")
    mostrar_servidores()

def mostrar_servidores():
    for serv, hard in servidores.items():
        print(f"Servidor: {serv} | Componentes: {hard}")


registrar_servidor()

while True:
    print("CENTRO DE DATOS")
    print("1.AGREGAR COMPONENTE \n2.ELIMINAR COMPONENTE \n3.VER INVENTARIO")
    op = int(input("Indica que opercación quieres realizar \n : "))


