def maior_elemento(lista):
    xMaior = lista[0]
    for i in range(0, len(lista)):
       if lista[i] > xMaior: xMaior = lista[i]
    return xMaior
