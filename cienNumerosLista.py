def CienNumerosLista():
    multiplosDeTres = []
    multiplosDeSiete = []
    noMultiplos = []
    
    for i in range(1,101):
        if i % 3 == 0:
            multiplosDeTres.append(i)
        elif i % 7 == 0:
            multiplosDeSiete.append(i)
        else:
            noMultiplos.append(i)
    
    sumatotal = multiplosDeTres + multiplosDeSiete
    print("Multiplos de 3: " "Suma", sum(multiplosDeTres), "Cantidad",len(multiplosDeTres))
    print("Multiplos de 7: " "Suma", sum(multiplosDeSiete), "Cantidad",len(multiplosDeSiete))
    print("No multiplos", len(noMultiplos))
    
CienNumerosLista()
    
