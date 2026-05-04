import random

num_golpes = random.randint(50, 100)
print(num_golpes)

espada_daño = 0
espada_magia = 0
categoria = ""
for golpe in range(1, num_golpes + 1):
    if golpe % 4 == 0 and golpe % 7 == 0:
        espada_daño += 10
        espada_magia += 1
        print(f"Impacto {golpe}: Golpe Maestro (+10 Daño, +1 Magia)")
        print("-" * 50)
    elif golpe % 4 == 0:
        espada_daño += 5
        print(f"Impacto {golpe}: Golpe Pesado (+5 Daño)")
        print("-" * 50)
    elif golpe % 7 == 0:
        espada_daño += 2
        espada_magia += 1
        print(f"Impacto {golpe}: Golpe Rúnico (+2 Daño, +1 Magia)")
        print("-" * 50)
    else:
        espada_daño += 1
        print(f"Impacto {golpe}: Golpe Normal (+1 Daño)")
        print("-" * 50)
print("*" * 70)
if espada_daño >= 200:
    categoria = "Legendaria"
else:
    categoria = "Épica"
print(f'''
Reporte final:

Total de martillazos dados: {golpe}
Puntos de Daño totales: {espada_daño}
Puntos de Magia totales: {espada_magia}
Categoria de la espada: {categoria}
''')

