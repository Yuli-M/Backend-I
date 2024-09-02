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

def obtener_costo(valor):
    if isinstance(valor, (int, float)):
        return valor
    else:
        return float('inf')

def ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=True):
    recorrido = []
    movimientosRealizados = set()
    sumaCostos = 0

    filaActual = filaI
    columnaActual = columnaI
    movimientosRealizados.add((filaActual, columnaActual))
    columnas = 'ABCDEFGHIJKLM'

    while (filaActual, columnaActual) != (filaF, columnaF):
        costoActual = obtener_costo(m[filaActual] [columnaActual])
        #costoActual = m[filaActual, columnaActual]
        #if isinstance(costoActual, (int, float)):
            #sumaCostos += costoActual
            #recorrido.append((filaActual, columnaActual, costoActual, sumaCostos))
            #print(f"Celda: [{filaActual + 1}, {columnas[columnaActual]}] -- Costo: {costoActual} -- Costo acumulado: {sumaCostos}")
            #recorrido.append((filaActual, columnaActual))

        sumaCostos += costoActual
        recorrido.append((filaActual, columnaActual, costoActual, sumaCostos))
        print(f"Celda: [{filaActual + 1}, {columnas[columnaActual]}] -- Costo: {costoActual} -- Costo acumulado: {sumaCostos}")

        #movimientosRealizados.add((filaActual, columnaActual))#inicio


        movimientosPosibles = []

        if filaActual != filaF:
            if filaActual + 1 < len(m) and (filaActual + 1, columnaActual) not in movimientosRealizados:
                movimientosPosibles.append((filaActual + 1, columnaActual))
            if filaActual - 1 >= 0 and (filaActual - 1, columnaActual) not in movimientosRealizados:
                movimientosPosibles.append((filaActual - 1, columnaActual))
        if columnaActual != columnaF:
            if columnaActual + 1 < len(m[0]) and (filaActual, columnaActual + 1) not in movimientosRealizados:
                movimientosPosibles.append((filaActual, columnaActual + 1))
            if columnaActual - 1 >= 0 and (filaActual, columnaActual - 1) not in movimientosRealizados:
                movimientosPosibles.append((filaActual, columnaActual - 1))
        
        print(f"Movimientos posibles desde [{filaActual + 1}, {columnas[columnaActual]}]: {movimientosPosibles}")

        if movimientosPosibles:
            if menorCosto:
                movimiento = min(movimientosPosibles, key=lambda x: obtener_costo(m[x[0]][x[1]]))
            else:
                #si menorCosto es False
                movimiento = max(movimientosPosibles, key=lambda x: obtener_costo(m[x[0]][x[1]]))
            filaActual, columnaActual = movimiento
        else:
            break

        #filaActual, columnaActual = salto
        #movimientosRealizados.add((filaActual, columnaActual))

    #costoFinal = m[filaF, columnaF]
    #if isinstance(costoFinal, (int, float)):
        #sumaCostos += costoFinal

        print("Recorrido final:")
        for fila, columna, costo, acumulado in recorrido:
            print(f"Celda: [{fila + 1}, {columnas[columna]}] -- Costo: {costo} -- Costo acumulado: {acumulado}")
    #recorrido.append((filaF, columnaF))
        return recorrido, sumaCostos


inicio = 'I'
final = 'F'
filaI, columnaI = buscar_posicion(m, inicio)
filaF, columnaF = buscar_posicion(m, final)

columnas = 'ABCDEFGHIJKLM'

print(f"El inicio esta en: [ {filaI + 1}, {columnas[columnaI]} ]")
print(f"El final esta en : [ {filaF + 1}, {columnas[columnaF]} ]")

print("\nRecorrido menor costo: ")
recorridoMenor, costoTotalMenor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=True)

print("\nRecorrido mayor costo: ")
recorridoMayor, costoTotalMayor = ruta(filaI, columnaI, filaF, columnaF, m, menorCosto=False)




