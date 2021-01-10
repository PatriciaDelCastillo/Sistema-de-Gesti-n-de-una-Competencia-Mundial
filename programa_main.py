import pickle
from menu import *
from paises import *
from confederacion import *
import os.path
import random


def vector_generado(FD):
    v = []
    if os.path.exists(FD):
        m = open(FD, 'rt')
        for linea in m:
            pais = csv_to_pais(linea)
            ordenar_vector(v, pais)
        m.close()
    return v


def ordenar_vector(v, pais):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].puntos == pais.puntos:
            pos = c
            break
        if pais.puntos > v[c].puntos:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [pais]


# ------------------------------------------------------------------------------------
#   opcion 1
def mostrar_vector_paises(v):
    print(get_titulos())
    print('=' * 110)
    for i in range(len(v)):
        print(to_string_paises(v[i]))


# ----------------------------------------------------------------------
# OPCION 2
def mayor_pais_campeonatos_ganados(v):
    mayor = v[0]
    n = len(v)
    for i in range(n):
        if v[i].cantidad > mayor.cantidad:
            mayor = v[i]
    return mayor


# -------------------------------------------------------------------------

# OPCION 3
def contador_por_confederacion(v):
    vc = [0] * 6
    for conf in v:
        if conf.cantidad > 0:
            vc[conf.confederacion] += 1
    return vc


# --------------------------------------------------------------------------
# OPCION 4
def generar_vector_confederacion(x, v, Fd):
    cont = 0
    m = open(Fd, 'wb')
    for conf in v:
        if conf.confederacion == x:
            pickle.dump(conf, m)
            cont += 1
    m.close()
    return cont


# --------------------------------------------------------------------------

# OPCION 5
def mostrar_archivo(Fd, v, x):
    if not os.path.exists(Fd):
        print('No existe!......se va generar ......')

        generar_vector_confederacion(x, v, Fd)

    archivo_conf = open(Fd, 'rb')
    tam = os.path.getsize(Fd)
    print('LISTA DE PAISES QUE PERTENECE A LA CONFEDERACION')
    print(get_titulos_confederacion())
    print('=' * 110)
    while archivo_conf.tell() < tam:
        una_conf = pickle.load(archivo_conf)
        print(to_string_confederacion(una_conf))
    archivo_conf.close()


# --------------------------------------------------------------------------
# OPCION 6
def buscar_nombre(v, nombres):
    p = None
    for pais in v:
        if pais.nombres == nombres:
            p = pais.nombres
            break
    return p


def generar_resto(v, m):
    vr = []
    vr2 = []
    for i in range(len(v)):
        y = v[i].nombres
        vr.append(y)

    for f in range(1):
        for c in range(8):
            vr.remove(m[f][c])

    for i in range(len(vr)):
        if i < 27:
            vr2.append(vr[i])
    return vr2


def generar_una_matriz(v):
    flag = False
    filas, columnas = 4, 8
    m = [[0] * columnas for i in range(filas)]
    nombres = input('Ingrese el nombre del pais Organizador:')
    p = buscar_nombre(v, nombres)

    m[0][0] = p
    for c in range(columnas):
        if c != 0:
            if not flag:
                m[0][c] = v[c - 1].nombres
                if m[0][c] == m[0][0]:
                    m[0][c] = v[c].nombres
                    flag = True
            else:
                m[0][c] = v[c].nombres
    vr = generar_resto(v, m)

    for f in range(1, filas):
        for c in range(columnas):
            m[f][c] = random.choice(vr)
            vr.remove(m[f][c])

    return m


def mostrar(m):
    celda = '\t\t|{:^10}|'
    print(' ' * 100, "FIXTURE DEL PROXIMO MUNDIAL\n")
    print("\t\t\t", get_titulos_grupos())
    print('\t\t', '=' * 185)
    for fila in m:
        for valor in fila:
            print("\t", celda.format(valor), end="")
        print()


# --------------------------------------------------------------------------
# OPCION 7
def buscar_un_pais(m, nom):
    res = False
    fil, col = None, None
    for f in range(len(m)):
        for c in range(len(m[0])):
            if m[f][c] == nom:
                res = True
                fil, col = f, c
                break
        if res:
            break
    return fil, col


def main():
    print(' \x1b[1;39m  ')
    FD = 'paises.csv'
    v = vector_generado(FD)
    m = ''
    cargar_matriz = True
    opcion = -1
    while opcion != 8:
        opcion = menu()
        if opcion == 1:
            mostrar_vector_paises(v)
            print('-' * 110)
        elif opcion == 2:
            mayor = mayor_pais_campeonatos_ganados(v)
            print('PAIS CON MAYOR CANTIDAD DE CAMPEONATOS GANADOS\n')
            print(get_titulos())
            print('=' * 110)
            print(to_string_paises(mayor))
            print('-' * 110)
        elif opcion == 3:
            vc = contador_por_confederacion(v)
            print('TOTAL DE PAISES QUE GANARON ALGUN CAMPEONATO\n')
            for i in range(len(vc)):
                if vc[i] != 0:
                    print('La Confederacion ', i, 'tiene', vc[i], 'países que ganaron un campeonato.')
                else:
                    print('La Confederacion', i, 'no tiene ninguno pais que haya ganado algun campeonato.')
        elif opcion == 4:
            x = validate('Ingrese un valor de la confederación entre 0 a 5(0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC): ',5, 0,)
            Fd = 'Clasificacion' + str(x) + '.dat'
            cont = generar_vector_confederacion(x, v, Fd)
            print('El nombre del archivo generado', Fd, 'y tiene ', cont, 'registros')
        elif opcion == 5:
            x = validate('Ingrese un valor de la confederación  a buscar  entre 0 a 5(0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC): ',5, 0,)
            Fd = 'Clasificacion' + str(x) + '.dat'
            mostrar_archivo(Fd, v, x)
        elif opcion == 6:
            m = generar_una_matriz(v)
            mostrar(m)
        elif opcion == 7:
            nom = input("Ingrese un nombre de un Pais a buscar: ")
            f, c = buscar_un_pais(m, nom)
            if (f != None and c != None):
                print("Se encontro el nombre ", m[f][c], "Se encontro en el Grupo: ", f)
            else:
                print("No se encontro el nombre del Pais")
        else:
            print('PROGRAMA FINALIZADO')


if __name__ == '__main__':
    main()
