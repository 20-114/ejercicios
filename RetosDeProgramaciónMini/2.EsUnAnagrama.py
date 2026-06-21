
''' 
* Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
'''

palabra1 = "csaa"
palabra2 = "casa"

def evaluaAnagrama(palabra1, palabra2):
    if palabra1 == palabra2:
        return print(False)
    elif len(palabra1) == len(palabra2):
        for letra in palabra1:
            if letra in palabra2:
                continue
            else:
                print(letra)
                return print(False)
    else:
        return print(False)
    return print(True)
    
evaluaAnagrama(palabra1, palabra2)

