import random

# Opciones posibles
opciones = ['piedra', 'papel', 'tijera']

# Solicitar elegir una opción al usuario y convertirla a minúsculas
eleccion_usuario = input("Introduce piedra, papel o tijera: ").lower()

# Validar la elección del usuario
if eleccion_usuario not in opciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
else:
    # Simular la elección del computador usando random.choice()
    eleccion_computador = random.choice(opciones)

    # Mostrar resultados
    print("Tu jugaste", eleccion_usuario)
    print("Computador jugó", eleccion_computador)

    # Determinar el resultado
    if eleccion_usuario == eleccion_computador:
        print("Empate!")
    elif (eleccion_usuario == 'piedra' and eleccion_computador == 'tijera') or \
         (eleccion_usuario == 'tijera' and eleccion_computador == 'papel') or \
         (eleccion_usuario == 'papel' and eleccion_computador == 'piedra'):
        print("Ganaste!!")
    else:
        print("Perdiste!")