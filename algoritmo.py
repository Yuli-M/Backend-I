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

def ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=True):
    recorrido = []
    movimientosRealizados = set()
    sumaCostos = 0

    filaActual = filaI
    columnaActual = columnaI
    movimientosRealizados.add((filaActual, columnaActual))
    columnas = 'ABCDEFGHIJKLM'

    while (filaActual, columnaActual) != (filaF, columnaF):
        #costoActual = m[filaActual, columnaActual]
        #if isinstance(costoActual, (int, float)):
            #sumaCostos += costoActual
            #recorrido.append((filaActual, columnaActual, costoActual, sumaCostos))
            #print(f"Celda: [{filaActual + 1}, {columnas[columnaActual]}] -- Costo: {costoActual} -- Costo acumulado: {sumaCostos}")

            #recorrido.append((filaActual, columnaActual))

        movimientosPosibles = []

        if filaActual != filaF:
            if filaActual + 1 < m.shape[0] and (filaActual + 1, columnaActual) not in movimientosRealizados:
                movimientosPosibles.append((filaActual + 1, columnaActual))
            if filaActual - 1 >= 0 and (filaActual - 1, columnaActual) not in movimientosRealizados:
                movimientosPosibles.append((filaActual - 1, columnaActual))
        if columnaActual != columnaF:
            if columnaActual + 1 < m.shape[1] and (filaActual, columnaActual + 1) not in movimientosRealizados:
                movimientosPosibles.append((filaActual, columnaActual + 1))
            if columnaActual - 1 >= 0 and (filaActual, columnaActual - 1) not in movimientosRealizados:
                movimientosPosibles.append((filaActual, columnaActual - 1))
        
        print(f"Movimientos posibles desde [{filaActual + 1}, {columnas[columnaActual]}]: {movimientosPosibles}")

        #solo para saber los costos antes
        for movimiento in movimientosPosibles:
            costo = m[movimiento[0], movimiento[1]]
            print(f"Moviemiento: {movimiento} -- Costo: {costo}")
            if isinstance(costo, (int, float)):
                sumaCostos += costo
                recorrido.append((filaActual, columnaActual, costo, sumaCostos))
                print(f"Celda: [{filaActual + 1}, {columnas[columnaActual]}] -- Costo: {costo} -- Costo acumulado: {sumaCostos}")
            else:
                print("valor no int");

        if not movimientosPosibles:
            break



        if menorCosto:
            salto = min(movimientosPosibles, key=lambda x: m[x[0], x[1]] if isinstance(m[x[0], x[1]], (int, float)) else float('inf'))
        else:
            salto = max(movimientosPosibles, key=lambda x: m[x[0], x[1]] if isinstance(m[x[0], x[1]], (int, float)) else float('-inf') )

        filaActual, columnaActual = salto
        movimientosRealizados.add((filaActual, columnaActual))

    #costoFinal = m[filaF, columnaF]
    #if isinstance(costoFinal, (int, float)):
        #sumaCostos += costoFinal

        print(f"Celda: [{filaF + 1}, {columnas[columnaF]}] -- Costo acumulado: {sumaCostos}")

    recorrido.append((filaF, columnaF))

    return recorrido, sumaCostos


inicio = 'I'
final = 'F'
posicionI = np.argwhere(m == inicio)
posicionF = np.argwhere(m == final)

filaI, columnaI = posicionI[0]
filaF, columnaF = posicionF[0]
columnas = 'ABCDEFGHIJKLM'

print(f"El inicio esta en: [ {filaI + 1}, {columnas[columnaI]} ]")
print(f"El final esta en : [ {filaF + 1}, {columnas[columnaF]} ]")

print("\nRecorrido menor costo: ")
recorridoMenor, costoTotalMenor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=True)

print("\nRecorrido mayor costo: ")
recorridoMayor, costoTotalMayor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=False)




