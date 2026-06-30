
''' 
* Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
'''

palabra1 = "aorm"
palabra2 = "amor"

# def evaluaAnagrama(palabra1, palabra2):
#     if palabra1 == palabra2:
#         return False
#     elif len(palabra1) == len(palabra2):
#         for letra in palabra1:
#             if letra in palabra2:
#                 continue
#             else:
#                 return False
#     else:
#         return False
#     return True
    
# resultado = evaluaAnagrama(palabra1, palabra2)
# print(resultado)




# def evaluaAnagrama(p1, p2):
#     if p1 == p2:
#         return False
#     return sorted(p1) == sorted(p2)
    
# resultado = evaluaAnagrama(palabra1, palabra2)
# print(resultado)


def evaluaAnagrama(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 == p2:
        return False
    if len(p1) != len(p2):
        return False
    letras_disponibles = list(p2)
    for letra in p1:
        if letra in letras_disponibles:
            letras_disponibles.remove(letra)
        else:
            return False
    return True

resultado = evaluaAnagrama(palabra1, palabra2)
print(resultado)


