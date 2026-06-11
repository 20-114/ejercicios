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
            del_hardware = input("Ingresa el nombre del nuevo componente: ")
            activo = cerrar_programa(del_hardware)
            eliminar_componentes(servidor, del_hardware)
        case '3':
            mostrar_servidores()
        case "CERRAR":
            print("Cerrando el programa...")
            break
        case _:
            print("Opción Inválida")
