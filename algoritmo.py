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