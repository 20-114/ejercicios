'''
Contexto: Debes administrar el inventario de una biblioteca. 
Los datos se guardan en una lista general, donde cada libro 
es un diccionario independiente.

🎯 Instrucciones de Funcionamiento
Diseña un menú interactivo que permita al usuario realizar 
las siguientes acciones de forma continua hasta que decida salir:

Crear (Agregar Libro): Solicita el ISBN, título y autor.

    Condición: El ISBN debe ser estrictamente un número entero de 4 dígitos.

    Control de errores: Si el usuario ingresa letras o un número de 
    diferente longitud, debe mostrar un error y volver a pedir el ISBN.

    Validación: Si el ISBN ya existe en la biblioteca, rechaza el 
    registro. El estado prestado debe ser False por defecto.

Leer (Mostrar Inventario): Imprime una lista visualmente atractiva 
de todos los libros. Si el estado prestado es True, debe mostrar 
"(No Disponible)"; si es False, "(Disponible en sala)".

Actualizar (Prestar/Devolver): Pide el ISBN de un libro.

    Control de errores: Maneja el caso en que el usuario ingrese 
    texto en lugar de un número.

    Condición: Si el libro existe, invierte su estado (si estaba 
    prestado, ahora está devuelto, y viceversa). Si el ISBN no existe, 
    notifica al usuario.

Borrar (Dar de baja): Pide un ISBN para eliminar un libro del 
sistema de forma permanente.

    Condición Crítica: No puedes eliminar un libro que esté actualmente 
    prestado. Si el usuario intenta borrarlo, el sistema debe bloquear 
    la acción advirtiendo que el libro debe ser devuelto primero.
'''

biblioteca = [
    {"isbn": 1001, "titulo": "1984", "autor": "George Orwell", "prestado": False},
    {"isbn": 1002, "titulo": "Dune", "autor": "Frank Herbert", "prestado": True}
]

def agregarLibro():
    print("-"*50)
    activo = True
    while activo:
        try:
            isbn = int(input("Indique el ISBN del libro que desea ingresar al sistema \n--|"))
        except ValueError:
            print("El ISBN solo puede contener dígitos")
            continue
        if len(str(isbn)) != 4:
            print("El ISBN debe ser un número de cuatro dígitos")
            continue
        elif isbn <= 0:
            print("Solo puede ingresar números enteros mayores a cero")
            continue
        for codigo in biblioteca:
            if isbn == codigo['isbn']:
                print("El ISBN ya se encuentra registrado en la biblioteca")
                print("Ingreso Rechazado")
                activo = False
                break
        if not activo:
            break
        titulo = input("Ingrese el titulo del libro \n--|")
        autor = input("Ingrese el Autor del libro \n--| ")
        biblioteca.append({
                        "isbn": isbn,
                        "titulo": titulo,
                        "autor": autor,
                        "prestado": False
                        })
        print("°"*50)
        print(f"El libro {titulo} del autor {autor} con ISBN {isbn} fue ingresado en la biblioteca correctamente")
        break

def mostrarInventario():
    print("-"*50)
    prestado = ""
    for libro in biblioteca:
        if not libro['prestado']:
            prestado = "Disponible en sala"
        else:
            prestado = "No Disponible"
        print(f"ISBN: {libro['isbn']} -|- Titulo: {libro['titulo']} -|- Autor: {libro['autor']} -|- {prestado}")

# def mostrarInventario():
#     print(f"\n{'='*20} INVENTARIO ACTUAL {'='*20}")
#     for libro in biblioteca:
#         estado = "❌ No Disponible" if libro['prestado'] else "✅ Disponible"
#         print(f"[{libro['isbn']}] {libro['titulo']} | Autor: {libro['autor']} | Estado: {estado}")
#     print("-" * 60)

def actualizar():
    while True:
        mostrarInventario()
        try:
            isbn = int(input("Indica el ISBN del libro que se Prestara/Devolvera \n--|"))
        except ValueError:
            print("Solo puede ingresar números")
        if len(str(isbn)) != 4:
                print("El ISBN debe ser un número de cuatro dígitos")
                continue
        elif isbn <= 0:
            print("Solo puede ingresar números enteros mayores a cero")
            continue
        for codigo in biblioteca:
            if isbn == codigo['isbn']:
                if not codigo['prestado']:
                    codigo['prestado'] = True
                    break
                else:
                    codigo['prestado'] = False
                    break
            else:
                print("El ISBN ingresado no existe en la base de datos")
                continue
        break

def eliminarLibro():
    while True:
        mostrarInventario()
        try:
            isbn = int(input("Indica el ISBN del libro que desea aliminar de la base de datos \n--|"))
        except ValueError:
            print("Solo puede ingresar números")
        if len(str(isbn)) != 4:
                print("El ISBN debe ser un número de cuatro dígitos")
                continue
        elif isbn <= 0:
            print("Solo puede ingresar números enteros mayores a cero")
            continue
        for codigo in biblioteca:
            if isbn == codigo['isbn']:
                if not codigo['prestado']:
                    biblioteca.remove(codigo)
                    break
                else:
                    print("No se puede eliminar el libro porque esta prestado. Deven devolverlo primero")
                    break
            else:
                print("El ISBN ingresado no existe en la base de datos")
                continue
        break


def menu():
    while True:
        print("-"*50)   
        try:
            print('''
            BIBLIOTECA
        1. Agregar un libro
        2. Mostrar Inventario
        3. Prestar/Devolver
        4. Dar de baja
        5. Salir
    ''')
            op = input("    Seleccione una opción --|")
            match op:
                case "1":
                    agregarLibro()
                case "2":
                    mostrarInventario()
                case "3":
                    actualizar()
                case "4":
                    eliminarLibro()
                case "5":
                    print("Saliendo de la biblioteca")
                    break
                case _:
                    print("Ingreso Inválido")
        except KeyboardInterrupt:
            print(f"\n{"-"*20}|Sistema Bloqueado|{"-"*20}")
            break

menu()
