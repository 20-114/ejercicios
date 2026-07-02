'''
Contexto: Un bot de marketing recopila etiquetas introducidas 
por usuarios, pero estas vienen con errores de formato (espacios 
en blanco innecesarios y mezcla caótica de mayúsculas y minúsculas).

Los Datos Base: 
Una lista de cadenas de texto sucias: 
["  #PythonMola   ", " #ia ", "  #PROGRAMACION ", " #code    ", " #tech "].

El Comportamiento Esperado: El programa debe limpiar el flujo 
de texto aplicando dos reglas en cadena:

    Estandarizar las cadenas removiendo todos los espacios en blanco 
    de los extremos y convirtiendo todo el texto a letras minúsculas.

    Analizar la longitud del texto ya limpio y descartar cualquier 
    etiqueta que tenga una longitud total menor a 6 caracteres 
    (contando el símbolo #).

El Resultado: Una lista purgada con los hashtags óptimos, 
homogéneos y listos para el motor de búsqueda.

'''

hashs = ["  #PythonMola   ", " #ia ", "  #PROGRAMACION ", " #code    ", " #tech "]

estandar = map(lambda hash: hash.lower().strip(), hashs)

optimos = filter(lambda hash: len(hash) >= 6, estandar)

print(list(optimos))

