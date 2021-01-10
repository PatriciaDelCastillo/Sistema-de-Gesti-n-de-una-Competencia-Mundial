# VALIDACION DEL TAMAÑO
def validate(msg, limite_superior, limite_inferior=0):
    x = int(input(msg))
    while x < limite_inferior or x > limite_superior:
        print('El valor deber estar entre', limite_inferior, \
              'y', limite_superior)
        x = int(input(msg))
    return x
