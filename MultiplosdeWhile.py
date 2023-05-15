def MultiplosdeWhile():
    contador3 = 0
    contador7 = 0
    acumulador3 = 0
    acumulador7 = 0
    noMultiplos = 0
    i = 0
    while i < 100:
        i += 1
        if i % 3 == 0:
            print("Multiplos de 3", i)
            contador3 += 1
            acumulador3 += i
        elif i % 7 == 0:
            print("Multiplos de 7", i)
            contador7 += 1
            acumulador7 += i
        else:
            noMultiplos += 1
            print("No multiplos", noMultiplos)
    sumatotal = acumulador3 + acumulador7
    print("Multiplos de 3: " "Suma", acumulador3, "Cantidad", contador3)
    print("Multiplos de 7: " "Suma", acumulador7, "Cantidad", contador7)
    print("No multiplos", noMultiplos)
    print("Suma total", sumatotal)
MultiplosdeWhile()
