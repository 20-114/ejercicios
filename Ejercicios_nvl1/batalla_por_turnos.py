import random
import time

heroe = "Giorno" # pylint: disable=invalid-name
monstruo = "Cangurin" # pylint: disable=invalid-name
hp_heroe = 100 # pylint: disable=invalid-name
hp_monstuo = 100 # pylint: disable=invalid-name


def attack(vida_monstruo):
    "el heroe atacara al mounstruo"
    attack_her = random.randint(10,20)
    vida_monstruo -= attack_her
    print(f"Atacaste con {attack_her} de daño")
    time.sleep(1)
    return vida_monstruo
def curar(vida_heroe):
    "el heroe se curara"
    vida_heroe += random.randint(15, 20)
    if vida_heroe > 100:
        vida_heroe = 100
    print("Te has curado")
    time.sleep(1)
    return vida_heroe
def attack_special(vida_monstruo):
    ''''el heroe atacara con critico al mounstruo'''
    probabilidad_critico = random.randint(1, 10)   
    if probabilidad_critico <= 3:
        vida_monstruo -= 40
        print("Ataque crítico")
    else:
        print("fallaste")
    time.sleep(1)
    return vida_monstruo
def attack_mons(vida_heroe):
    ''''el mounstruo atacara al heroe'''
    attack_monstruo = random.randint(5, 25)
    vida_heroe -= attack_monstruo
    print(f"El monstruo te hizo {attack_monstruo} de daño")
    time.sleep(1)
    return vida_heroe
def barra_vida_heroe(nombre_heroe, barra):
    "bara de vida del heroe"
    vida = "-"
    print(f"{nombre_heroe}: {barra*vida}")
def barra_vida_monstruo(nombre_monstruo, barra):
    "bara de vida del heroe"
    vida = "-"
    print(f"{nombre_monstruo}: {barra*vida}")

while hp_heroe > 0 and hp_monstuo > 0:
    barra_vida_heroe(heroe, hp_heroe)
    barra_vida_monstruo(monstruo, hp_monstuo)
    time.sleep(1)
    boton = int(input("Elige una acción: \n1) Atacar \n2) Curarte \n3) Ataque especial \n4) Rendirte \n "))
    match boton:
        case 1:
            hp_monstuo = attack(hp_monstuo)
        case 2:
            hp_heroe = curar(hp_heroe)
        case 3:
            hp_monstuo = attack_special(hp_monstuo)
        case 4:
            hp_heroe = 0 
            print("Eres una verguenza")
            break
    if hp_monstuo > 0:
        hp_heroe = attack_mons(hp_heroe)
if hp_heroe > hp_monstuo:
    print("!VICTORIA¡")
else:
    print("DERROTTA")
     