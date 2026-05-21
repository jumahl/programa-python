# Nombre del estudiante: Juan Manuel Hernandez Loaiza - 1006438861
# Grupo: 213022_225
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia
# Problema #1
'''
Una matriz almacena datos de sesiones de clientes con el formato:
[ID Cliente, Duracion (segundos), Eventos Clics].
Se necesita una herramienta para evaluar el nivel de compromiso de cada sesion.

Reglas de clasificacion:
- "Alto" si Duracion > 180s y Clics > 8.
- "Bajo" si Duracion < 60s o Clics < 3.
- "Medio" en los demas casos.
Salida: generar un informe con el ID del cliente y su clasificacion.

'''


def clasificar_compromiso(duracion_segundos, clics):

    if duracion_segundos > 180 and clics > 8:
        return "Alto"
    if duracion_segundos < 60 or clics < 3:
        return "Bajo"
    return "Medio"

sesiones = [
    ["C001", 240, 12],
    ["C002", 45, 2],
    ["C003", 90, 4],
    ["C004", 190, 5],
    ["C005", 30, 7],
]


print("=" * 38)
print(f"{'ID Cliente':>12} | Clasificación")
print("-" * 38)
for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    nivel = clasificar_compromiso(duracion, clics)
    print(f"{id_cliente:>12} | {nivel}")
print("=" * 38)
