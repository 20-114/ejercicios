'''
Contexto: En un juego RPG, el jugador tiene un inventario 
(diccionario) y quiere fabricar (craftear) una espada usando 
recetas. Este ejercicio requiere modificar cantidades, verificar 
existencias y añadir nuevos ítems.

🎯 Tu Misión
Diseña la función craftear_item(nombre_item):

Validación de Receta: Verifica si el ítem solicitado existe 
en el diccionario recetas. Si no existe, avisa al jugador que 
no tiene los planos de ese objeto.

Validación de Recursos: Comprueba si el jugador tiene todos los 
ingredientes necesarios en su inventario y en las cantidades 
suficientes. Por ejemplo, para la espada_oro se necesitan 2 de oro, 
pero el inventario inicial solo tiene 1. El sistema debe detenerse 
y avisar qué material falta.

Mutación Cruzada: Si tiene los materiales, resta los ingredientes 
del inventario del jugador. Si la cantidad de algún material llega 
a 0, elimina la llave de ese material del inventario para mantenerlo 
limpio. Finalmente, añade el nuevo ítem (ej. 'espada_hierro') al 
inventario con cantidad 1 (o súmale 1 si ya tenía una).
'''
recetas = {
    'espada basica' : {'madera' : 1, 'hierro' : 2},
    'escudo' : {'madera' : 1,'hierro' : 3, 'cuero' : 1}
    }
inventario = {'madera' : 5,'hierro' : 2,'cuero' : 2, 'espada basica' : 1}


def craftear_item(inventario, item):
    copia_inventario = inventario.copy()
    mat_faltante = []
    if item in recetas: #busca si existen los planos del item que se quiere construir
        for mat_primas in recetas[item]: #busca los ingredientes necesarios en el invetario según la receta
            prima_cantidad = recetas[item][mat_primas]
            try:
                if copia_inventario[mat_primas] >= prima_cantidad: #valida que existan las cantidades minimas de los ingredientes en el inventarios para craftear el objeto
                    copia_inventario[mat_primas] -= prima_cantidad #resta los ingredientes consumidos del inventario
                    if copia_inventario[mat_primas] == 0:
                        del copia_inventario[mat_primas]
                else:
                    mat_faltante.append(mat_primas)
            except KeyError:
                mat_faltante.append(mat_primas)
        if mat_faltante:
            print(f"Te faltan materiales: {mat_faltante}")
            return
        if item in copia_inventario:
            copia_inventario[item] += 1
        else:
            copia_inventario[item] = 1
        inventario.clear()
        inventario.update(copia_inventario)
    else:
        print("No existen los planos del objeto")

item = input("¿Que quieres crear?: ")
craftear_item(inventario, item)

print(inventario)