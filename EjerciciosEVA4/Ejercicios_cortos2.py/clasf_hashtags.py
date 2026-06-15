'''
Contexto: Un sistema de marketing analiza las etiquetas (tags) 
de publicaciones para agruparlas. El sistema recibe una lista 
de textos crudos ingresados por los creadores de contenido y 
debe procesarlos para actualizar un diccionario global que cuenta 
la popularidad de cada etiqueta.

🎯 Instrucciones de Funcionamiento
El sistema debe procesar la lista de textos crudos uno por uno, 
aplicando filtros estrictos antes de afectar al diccionario de 
popularidad:

Filtro de Estructura: Para que un texto sea considerado un hashtag 
válido, debe iniciar obligatoriamente con el símbolo del numeral (#). 
Si no empieza con este símbolo, descarta el texto por completo.

Filtro de Espacios Internos: La etiqueta no puede tener espacios en 
blanco en su interior (entre palabras). Si el texto tiene espacios 
intermedios, se ignora (los espacios vacíos al inicio o al final del 
texto general sí deben ser ignorados y limpiados).

Conteo de Popularidad: Si el hashtag supera los filtros, remueve el 
símbolo # y transforma todo el texto a letras minúsculas (para que #Python 
y #python cuenten como lo mismo). Luego, busca esa palabra en el diccionario 
global: si ya existe, incrementa su contador en 1; si no existe, agrégala 
con un valor inicial de 1.
'''

list_tags = {}

while True:
    print("Escribe 'salir' para cerrar el programa")
    try:
        hashtag = input("Ingreso de Hashtags: ").strip()
        if hashtag.lower() == "salir":
            break
        if "#" in hashtag[0]:
            if " " in hashtag:
                print("Error de formato")
                print("Los Hashtags no pueden tener espacios intermedios")
                continue
        else:
            print("Error de formato")
            print("Los Hashtags deben comenzar con el simbolo '#'")
            continue  
        hashtag_tratado =hashtag.lstrip("#").lower()
        if hashtag_tratado in list_tags:
            list_tags[hashtag_tratado] += 1
        else:
            list_tags[hashtag_tratado] = 1
        for hashs, vistas in list_tags.items():
            print(f"{hashs} : {vistas} vistas")
    except KeyboardInterrupt:
        print("\nBloqueo del sistema")
    except:
        print("\nIngreso Inválido")
        continue



