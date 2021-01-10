class Paises:
    def __init__(self, confederacion, nombres, puntos, cantidad):
        self.confederacion = confederacion
        self.nombres = nombres
        self.puntos = puntos
        self.cantidad = cantidad


def to_string_paises(paises):
    list = " "
    list += '{:^25} |'.format(str(to_string_confederacion(paises.confederacion)))
    list += '{:^30} |'.format(str(paises.nombres))
    list += '{:^15} |'.format(str(paises.puntos))
    list += '{:^22} |'.format(str(paises.cantidad))
    return list


def get_titulos():
    renglon = '\n'
    renglon += '{:^22}'.format("Confederacion")
    renglon += ' '
    renglon += '{:^30}'.format("Nombre")
    renglon += '  '
    renglon += '{:^17}'.format("Puntos")
    renglon += '  '
    renglon += '{:^20}'.format("Cantidad de Campeonatos Ganados")

    return renglon


def get_titulos_confederacion():
    renglon = '\n'
    renglon += '{:<30}'.format("Nombre")
    renglon += ' '
    renglon += '{:<25}'.format("Puntos")
    renglon += '  '
    renglon += '{:^17}'.format("Cantidad de Campeonatos Ganados")
    return renglon


def get_titulos_grupos():
    renglon = ''
    renglon += '{:<24}'.format("GRUPO 1")
    renglon += ' '
    renglon += '{:<22}'.format("GRUPO 2")
    renglon += '  '
    renglon += '{:<22}'.format("GRUPO 3")
    renglon += '  '
    renglon += '{:<22}'.format("GRUPO 4")
    renglon += '  '
    renglon += '{:<22}'.format("GRUPO 5")
    renglon += '  '
    renglon += '{:<22}'.format("GRUPO 6")
    renglon += '  '
    renglon += '{:<22}'.format("GRUPO 7")
    renglon += '  '
    renglon += '{:<20}'.format("GRUPO 8")
    return renglon


def csv_to_pais(linea):
    token = linea.split(',')
    confederacion = int(token[0])
    nombres = token[1]
    puntos = int(token[2])
    cantidad = int(token[3])
    paises = Paises(confederacion, nombres, puntos, cantidad)
    return paises


def to_string_confederacion(confederacion):
    descripcion = ('UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC')
    return descripcion[confederacion]
