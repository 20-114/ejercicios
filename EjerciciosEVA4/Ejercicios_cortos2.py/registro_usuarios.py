'''
Contexto: Estás programando el módulo de registro para una plataforma médica. 
El sistema almacena los datos en una lista que contiene diccionarios (cada 
diccionario es un perfil de usuario). Debido a restricciones de la base de 
datos, los nombres de usuario deben ser extremadamente limpios.

🎯 Instrucciones de Funcionamiento
Crea un flujo que solicite un nuevo nombre de usuario y evalúe las siguientes 
reglas antes de guardarlo:

Validación de Espacios: El nombre de usuario no puede contener ningún espacio 
en blanco (ni al principio, ni al final, ni entre medio). Si se detecta un 
solo espacio, el registro se cancela inmediatamente avisando del error.

Validación de Contenido: El texto debe contener obligatoriamente una combinación 
de letras y números. No se permiten nombres de usuario que consistan únicamente 
en números.

Validación de Existencia: Si el texto pasa las reglas anteriores, revisa la lista. 
Si el nombre de usuario ya existe (sin importar si lo escribieron en mayúsculas o 
minúsculas), rechaza el registro por duplicado.

Inserción: Si es completamente válido, añade un nuevo diccionario al final de la 
lista con el nombre de usuario en minúsculas y el rol asignado por defecto 
como "invitado".
'''

usuarios_registrados = [
    {"username": "ana_gomez4", "rol": "medico"},
    {"username": "carlos99", "rol": "paciente"}
]


while True:
    tiene_numero = False
    tiene_letras = False
    numeros = "0123456789"
    letras = "abcdefghijklmnñopqrstuvwxyz"
    print("-"*30)
    new_user = input("Nombra a tu nuevo ususario \n : ")
    if " " in new_user:
        print("El nombre de usuario no puede contener espacios")
        print("Registro cancelado")
        continue
    # if any(char.isdigit() for char in new_user) and any(char.isalpha() for char in new_user ):
    #     print("hola")
    # else:
    #     print("El nombre debe contener letras y números")
    print("-"*30)
    for num in numeros:
        if num in new_user:
            tiene_numero = True
            break
    for letra in letras:
        if letra in new_user.lower():
            tiene_letras = True
            break
    if tiene_letras and tiene_numero:
        print("Evaluando existencia en los registros")
    else:
        print("El nombre debe contener letras y números")
        continue
    print("-"*30)
    existe = False
    for user_exist in usuarios_registrados:
        if new_user.lower() == user_exist['username'].lower():
            print("El usuario ya existe en los registros")
            print("Registro rechazado por duplicado")
            existe = True
            break
    if existe:
        continue 
    else:
        print("Registrando usuario...")
    print("-"*30)
    usuarios_registrados.append({"username": new_user.lower(), "rol": "invitado"})
    print(f"{new_user.lower()} fue registrado como invitado")
    print("-"*30)
    for usuarios in usuarios_registrados:
        print(f"{usuarios['username']} : {usuarios['rol']}")
    break

    
        
    

