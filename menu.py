from validacion import *


# MENU
def menu():
    print("\033[1;35m" + " " * 200)
    print('\x1b[1;33m' + '¡BIENVENIDOS AL MENU DEL PROGRAMA!')

    print('\033[1;35m' + '1-Mostrar el listado completo de países. ')
    print('2-Informar cuál es el país con mayor cantidad de campeonatos ganados.')
    print('3-Determinar, para cada confederación, cuántos países ganaron algún campeonato.')
    print('4-Generar un nuevo vector conteniendo los países de una confederación X que se ingresa por teclado.')
    print('5-Ingresar una confederación por teclado y buscar su archivo de clasificación. ')
    print('6-Generar un Fixture del próximo mundial')
    print('7-Buscar un Pais en un Fixture.')
    print('8-Salida ')
    print(" " * 200)
    print('\x1b[1;33m')
    opcion = validate("Elija una opcion>>>>>>", 8, 1)
    print('\x1b[1;30m')
    return opcion

