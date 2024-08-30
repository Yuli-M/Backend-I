import numpy as np
#Algoritmo que busca la ruta con menos y mas costo para llegar del punto I al punto F

m = np.array ([[-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],
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
        [1,-3,1,0,1,2,3,1,-2,3,3,0,3]])

def ruta(filaI, columnaI, filaF, columnaF, matriz, menorCosto=True):
    recorrido = []
    sumaCostos = 0

    filaActual = filaI
    columnaActual = columnaI

    while (filaActual != filaF) or (columnaActual != columnaF):
        recorrido.append((filaActual, columnaActual))
        costoActual = matriz[filaActual, columnaActual]
        
        if isinstance(costoActual, (int, float)):
            sumaCostos += costoActual

        movimientosPosibles = []
        if filaActual != filaF:
            if filaActual + 1 < matriz.shape[0]:
                movimientosPosibles.append((filaActual + 1, columnaActual))
            if filaActual - 1 >= 0:
                movimientosPosibles.append((filaActual - 1, columnaActual))
        if columnaActual != columnaF:
            if columnaActual + 1 < matriz.shape[1]:
                movimientosPosibles.append((filaActual, columnaActual + 1))
            if columnaActual - 1 >= 0:
                movimientosPosibles.append((filaActual, columnaActual - 1))
        
        if not movimientosPosibles:
            break

        if menorCosto:
            salto = min(movimientosPosibles, key=lambda x: matriz[x[0], x[1]] if isinstance(matriz[x[0], x[1]], (int, float)) else float('inf'))
        else:
            salto = max(movimientosPosibles, key=lambda x: matriz[x[0], x[1]] if isinstance(matriz[x[0], x[1]], (int, float)) else float('-inf') )

        filaActual, columnaActual = salto

    recorrido.append((filaF, columnaF))
    costoTotal = matriz[filaF, columnaF]
    if isinstance(costoTotal, (int, float)):
        sumaCostos += costoTotal

    return recorrido, sumaCostos


inicio = 'I'
final = 'F'
posicionI = np.argwhere(m == inicio)
posicionF = np.argwhere(m == final)

if posicionI.size > 0 and posicionF.size > 0:
    filaI, columnaI = posicionI [0]
    filaF, columnaF = posicionF [0]
    columnas = 'ABCDEFGHIJKLM'
    name_columnaI = columnas[columnaI]
    name_filaI = filaI + 1
    name_columnaF = columnas[columnaF]
    name_filaF = filaF + 1

    print(f"El inicio esta en: [ {name_filaI}, {name_columnaI} ]")
    print(f"El final esta en : [ {name_filaF}, {name_columnaF} ]")

    recorridoMenor, costoTotalMenor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=True)
    print("\nRecorrido menor costo: ")
    for fila, columna in recorridoMenor:
        print(f"[ {fila + 1}, {columnas[columna]} ]")
    print(f"Costo menor: {costoTotalMenor}")

    recorridoMayor, costoTotalMayor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=False)
    print("\nRecorrido mayor costo: ")
    for fila, columna in recorridoMayor:
        print(f"[ {fila + 1}, {columnas[columna]} ]")
    print(f"Costo mayor: {costoTotalMayor}")



