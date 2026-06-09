'''
Contexto: En ciberseguridad, el Control de Acceso Basado 
en Roles (RBAC) define qué puede hacer cada usuario en 
el sistema.

Requisitos del programa:

Define un diccionario llamado usuarios_sistema donde las 
llaves sean nombres de usuarios ('admin', 'operador', 'invitado') 
y sus valores sean listas de strings con sus permisos actuales (por 
ejemplo: ['leer', 'escribir', 'borrar']).

Diseña una función llamada modificar_permiso(usuario, accion, 
permiso) que reciba tres parámetros:

usuario (string): El nombre del usuario a modificar.

accion (string): Puede ser 'AGREGAR' o 'REMOVER'.

permiso (string): El nombre del permiso (ej. 'ejecutar').

La función debe validar:

Si el usuario existe en el diccionario. Si no existe, debe advertirlo.

Si la acción es 'AGREGAR', debe sumar el permiso a la lista de ese 
usuario (¡pero evita que se duplique si ya lo tiene!).

Si la acción es 'REMOVER', debe quitar el permiso de la lista (valida 
primero que el permiso realmente exista en su lista para que no rompa 
el programa).

Crea un flujo principal interactivo donde se soliciten estos tres 
datos al operador de forma continua hasta que decida salir escribiendo 
SALIR. Al finalizar, muestra el estado del diccionario.
'''

usuarios_sistema = {
    'admin' : [],
    'operador' : [],
    'invitado' : []
}
def salir(ingreso):
    'cambia el valor de la bandera "activo" a FALSE para interrumpir el bucle cuando el usuario escriba SALIR'
    ingreso = ingreso.upper()
    if ingreso == "SALIR":
        print("Saliendo del sistema")
        mostrar_usuarios()
        return False
    else:
        return True

def mostrar_usuarios():
    'imprime los usuarios y sus permisos actualmente existentes'
    print("-"*50)
    for usuario, permisos in usuarios_sistema.items():
        print(f"Usuario {usuario} | Permisos : {permisos}")

def modificar_permiso(usuario, accion, permiso):
    'Modifica los permisos de los usuarios. Debe ejecutarse solo si el usuario existe en el sistema'
    print("-"*50)
    match accion:
        case "AGREGAR": 
            if permiso in usuarios_sistema[usuario]:
                print("El usuario seleccionado ya tiene el permiso solicitodo")
            else:              
                usuarios_sistema[usuario].append(permiso)
        case "REMOVER":
            if permiso not in usuarios_sistema[usuario]:
                print("El usuario no cuenta con este permiso para ser eliminado")
            else:
                usuarios_sistema[usuario].remove(permiso)
        case _:
            print("Acción Inválida")

activo = True
while activo:
    try:
        mostrar_usuarios()
        print("Ingresa SALIR para finalizar el programa")
        print("-"*50)
        usr = input("Ingresa el usuario a modificar \n : ").lower()
        activo = salir(usr)
        if activo == False:
            break
        if usr in usuarios_sistema:
            print("Ususario encontrado")
            accion = input("Indica que acción de permisos quieres realizar (AGREGAR | REMOVER) \n : ").upper()
            activo = salir(accion)
            if activo == False:
                break
            permiso = input("Indica que permiso quieres gestionar \n : ")
            activo = salir(permiso)
            if activo == False:
                break
            modificar_permiso(usr, accion, permiso)
        else: 
            print("El ususario no existe en los registros")
        print(usuarios_sistema)
    except KeyboardInterrupt:
        print("Sistema Bloqueado")
        mostrar_usuarios()
        break

