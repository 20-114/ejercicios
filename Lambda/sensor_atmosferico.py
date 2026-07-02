'''
Contexto: Un dispositivo ecológico mide cada hora las partículas 
por millón (PPM) de contaminación en el aire y necesita aislar 
los momentos de crisis ambiental.

Los Datos Base: 
    Una lista de lecturas numéricas tomadas durante el día:
    [45, 120, 165, 80, 210, 148, 190, 30].

El Comportamiento Esperado: 
    El sistema debe analizar el conjunto completo de lecturas y 
    extraer únicamente aquellos registros que representen un peligro 
    inminente para la salud, definidos estrictamente como valores que 
    superen las 150 PPM. Todas las lecturas que estén por debajo de ese 
    límite deben ser ignoradas y descartadas del resultado final en un 
    solo paso de evaluación.

El Resultado: 
    Una lista limpia que actúe como bitácora que contenga solo los picos 
    de contaminación detectados.

'''

ppm = [45, 120, 165, 80, 210, 148, 190, 30]

peligro = filter(lambda ppms: ppms > 150, ppm)

print(list(peligro))
