'''
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
'''
poligonos = [
    {"cuadrado": [(-1,1),(-4,1),(-4,4),(-1,4)]},
    {"triangulo": [(1,1),(5,1),(3,5)]},
    {"rectangulo": [(-4,-2),(4,-2),(4,-5),(-4,-5)]}
]

def areaPoligono(polig):
    tipo_poligono = list(polig.keys())[0]
    vert = polig[tipo_poligono]
    if len(vert) == 3:
        x1, y1 = vert[0]
        x2, y2 = vert[1]
        x3, y3 = vert[2]
        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        return tipo_poligono, area
    elif len(vert) == 4:
        x1, y1 = vert[0]
        x2, y2 = vert[1]
        x3, y3 = vert[2]
        base = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        altura = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
        area = base * altura
        return tipo_poligono, area

for forma in poligonos:
    tipo, resultado_area = areaPoligono(forma)
    print(f"El area del {tipo} es de {resultado_area} unidades cuadradas")

# def areaPoligono(polig):
#     for forma, vert in polig.items():
#         if len(vert) == 3:
#             x1, y1 = vert[0]
#             x2, y2 = vert[1]
#             x3, y3 = vert[2]
#             area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
#             print(f"El area del triangulo es de {area} unidades cuadradas")
#         elif len(vert) == 4:
#             x1, y1 = vert[0]
#             x2, y2 = vert[1]
#             x3, y3 = vert[2]
#             base = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#             altura = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
#             area = base * altura
#             print(f"El area del {forma} es de {area} unidades cuadradas")

# area = map(lambda forma: areaPoligono(forma), poligonos)
# list(area)



# for forma in poligonos:
#     for vert in forma.values():
#         print(vert[0])
