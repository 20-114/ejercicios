'''
Contexto: Un departamento de finanzas necesita 
calcular rápidamente el dinero neto que se 
transferirá a una lista de empleados al final del mes.

Los Datos Base: 
    Una lista estática con los salarios brutos actuales de 
    los trabajadores: [1200, 850, 3100, 950, 1800].

El Comportamiento Esperado: 
    El programa debe tomar esa lista y generar una nueva 
    lista con los salarios netos finales. El cálculo para 
    cada salario individual debe realizarse en un único paso 
    lógico: primero se le suma un bono fijo del 15% por 
    productividad y, al resultado de esa suma, se le descuenta 
    un 12% por retenciones legales.

El Resultado: 
    Al ejecutar el programa, debes obtener la lista con los montos 
    finales exactos listos para la transferencia bancaria.

'''


sal_bruto = [1200, 850, 3100, 950, 1800]

bono = 1.15
retencion = 0.88

neto = map(lambda bruto: (bruto * bono)*retencion, sal_bruto)

print(list(neto))