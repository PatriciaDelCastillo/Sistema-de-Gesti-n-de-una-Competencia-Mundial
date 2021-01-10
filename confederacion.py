class Confederacion:
    def __init__(self, nombres, puntos, cantidad):
        self.nombres = nombres
        self.puntos = puntos
        self.cantidad = cantidad


def to_string_confederacion(confederacion):
    list = ''
    list += '{:<32}'.format(confederacion.nombres)
    list += '{:<30}'.format(confederacion.puntos)
    list += '{:<22}'.format(confederacion.cantidad)
    return list


def get_titulos_confederacion():
    renglon = '\n'
    renglon += '{:<20}'.format("Nombre")
    renglon += '  '
    renglon += '{:<30}'.format("Puntos")
    renglon += '  '
    renglon += '{:<20}'.format("Cantidad de Campeonatos Ganados")
    return renglon


