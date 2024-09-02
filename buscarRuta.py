 #Algoritmo que busca la ruta con menos y mas costo para llegar del punto I al punto F
m = [
        [-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],
        [2,3,'I',-1,-1,3,2,0,-3,-3,2,2,1],
        [1,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
        [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],
        [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
        [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
        [0,3,2,0,1,1,2,3,-1,-3,0,0,-2],
        [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
        [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
        [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
        [-3,-3,-3,3,-3,0,-2,-3,1,0,1,-1,-2],
        [-1,0,1,2,1,0,'F',0,-3,3,3,-2,-1],
        [1,-3,1,0,1,2,3,1,-2,3,3,0,3]
    ]

def buscar_posicion(m, valor):
    for i, fila in enumerate(m):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return i, j
    return None, None

def buscar_rutas (filaI, columnaI, filaF, columnaF, rutaActual, rutas, rutaRealizada, m, costoActual):
    print(f"Entrar a buscar rutas: ({filaI}, {columnaI}), Costo actual:{costoActual} ")
    print(f"Ruta actual: {rutaActual}")
    print(f"ruta realizada: {rutaRealizada}")
    if (filaI, columnaI) == (filaF, columnaF):
        rutas.append((list(rutaActual), costoActual))
        print(f"Ruta encontrada: {rutaActual} con costo {costoActual}")
        return

    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for movimiento in movimientos:
        nuevaFila = filaI + movimiento[0]
        nuevaColumna = columnaI + movimiento[1]

        if (0 <= nuevaFila < len(m)) and (0 <= nuevaColumna < len(m[0])) and (nuevaFila, nuevaColumna) not in rutaRealizada:
            print(f"Moviendo a: ({nuevaFila, nuevaColumna})")
            rutaRealizada.add((nuevaFila, nuevaColumna))
            rutaActual.append((nuevaFila, nuevaColumna))

            costo = m[nuevaFila][nuevaColumna]
            if isinstance(costo, (int, float)):
                nuevoCosto = costoActual + costo
             #else:
                 #continue
                print(f"Costo de la celda: {costo}, costo acumulado: {nuevoCosto}")
                buscar_rutas(nuevaFila, nuevaColumna, filaF, columnaF, rutaActual, rutas, rutaRealizada, m, nuevoCosto)

            rutaActual.pop()
            rutaRealizada.remove((nuevaFila, nuevaColumna))
            print(f"Regresando de: ({nuevaFila}, {nuevaColumna})")
            print(f"Ruta actual despues de regresar: {rutaActual}")
            print(f"Ruta realizada despues de regresar: {rutaRealizada}")

    print(f"Saliendo de buscar rutas: ({filaI}, {columnaI})...")

'''def buscar_posicion(m, valor):
    for fila in range(len(m[fila])):
        if m[fila][col] == valor:
            return (fila, col)
    return None'''

def buscar_min_max_costo(rutas):
    if not rutas:
        return None, None, None, None

    minCosto = float('inf')
    maxCosto = float('-inf')
    rutaMin = None#
    rutaMax = None#

    for ruta, costo in rutas:
        if costo < minCosto:
            minCosto = costo
            rutaMin = ruta #
        if costo > maxCosto:
            maxCosto = costo
            rutaMax = ruta #

    return rutaMin, minCosto, rutaMax, maxCosto

inicio = 'I'
final = 'F'
filaI, columnaI = buscar_posicion(m, inicio)
filaF, columnaF = buscar_posicion(m, final)

columnas = 'ABCDEFGHIJKLM'

print(f"El inicio esta en: [ {filaI + 1}, {columnas[columnaI]} ]")
print(f"El final esta en : [ {filaF + 1}, {columnas[columnaF]} ]")

rutas = []
rutaRealizada = set()
rutaActual = [(filaI, columnaI)]
costoActual = 0 #para que el costo inicial sea 0

rutaRealizada.add((filaI, columnaI))
buscar_rutas(filaI, columnaI, filaF, columnaF, rutaActual, rutas, rutaRealizada, m, costoActual)

rutaMin, minCosto, rutaMax, maxCosto = buscar_min_max_costo(rutas)

print(f"Ruta con el costo minimo ({minCosto}) : {rutaMin} ")
print(f"Ruta con el costo maximo ({maxCosto}) : {rutaMax}")





