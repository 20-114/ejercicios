'''
El Desafío: Simular un sistema de detección de intrusos (IDS) 
que registre qué puertos de red intenta tocar cada dirección 
IP y dispare alertas si el comportamiento se vuelve hostil.

Comportamiento esperado:

El programa debe ejecutar un ciclo de exactamente 5 rondas. 
En cada ronda, la máquina simula un intento de conexión generando 
de forma imprevista y aleatoria un número de puerto entre 1 y 100.

En cada ronda, el sistema le pide al operador que ingrese la 
dirección IP (un texto) que originó esa conexión.

El sistema debe almacenar cada IP como un identificador único, 
y asociarle una lista con todos los puertos que ha intentado 
tocar durante el simulacro.

Control de seguridad: * Si el operador deja el campo de la IP 
vacío o presiona espacio, el sistema debe reportar una anomalía 
de origen, ignorar el puerto generado y saltar a la siguiente ronda.

Si la IP es válida, se registra el puerto en su historial.

Al finalizar las 5 rondas, el programa inspecciona los registros: 
si alguna IP atacó un número total de puertos que sea un número par, 
el sistema imprime una alerta de "Sospecha de escaneo de red". Si el 
total de puertos atacados por esa IP es impar, muestra "Tráfico bajo 
análisis". Al final, muestra el reporte completo de qué puertos tocó 
cada IP.
'''


