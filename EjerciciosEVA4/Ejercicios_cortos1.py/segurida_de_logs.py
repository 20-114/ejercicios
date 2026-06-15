'''
Contexto: Tu servidor web está bajo un posible ataque de denegación de servicio (DDoS). 
Tienes una lista con los registros de las últimas peticiones entrantes y un diccionario 
de IPs sospechosas. Necesitas procesar la lista para automatizar el bloqueo.

Tu Misión
Contar e Identificar: Recorre la lista peticiones_entrantes. Si una IP ya está en el 
diccionario ips_bloqueadas, incrementa su contador de peticiones en 1 y elimínala 
de la lista de peticiones (usa comandos de remover).

Umbral de Bloqueo: Si una IP no está bloqueada pero aparece más de 3 veces en la 
lista, agrégala al diccionario de ips_bloqueadas con la razón 'Sospecha de Botnet' 
y un contador inicializado con sus peticiones correspondientes.

Limpieza en Sitio: Al finalizar, la lista peticiones_entrantes solo debe contener IPs 
limpias (que no hayan sido bloqueadas) y el diccionario debe reflejar el estado real 
de la seguridad.

'''

peticiones_entrantes = [
    "192.168.1.5", "10.0.0.1", "192.168.1.5", "185.220.101.5", 
    "10.0.0.1", "192.168.1.5", "185.220.101.5", "192.168.1.5"
]

ips_bloqueadas = {
    '185.220.101.5': {'razon': 'Tor Exit Node', 'peticiones': 0}
}


control_ips = {}
for ip_input in peticiones_entrantes[:]:
    if ip_input in ips_bloqueadas:
        peticiones_entrantes.remove(ip_input)
        ips_bloqueadas[ip_input]['peticiones'] += 1
        continue
    if ip_input not in control_ips:
        control_ips[ip_input] = 1
    else:
        control_ips[ip_input] += 1
    if control_ips[ip_input] > 3:
        ips_bloqueadas[ip_input] = {'razon' : 'Sospecha de Botnet', 'peticiones' : control_ips[ip_input]}
        for ip_borrar in peticiones_entrantes[:]:
            if ip_input == ip_borrar:
                peticiones_entrantes.remove(ip_input)

print(peticiones_entrantes) 
    


