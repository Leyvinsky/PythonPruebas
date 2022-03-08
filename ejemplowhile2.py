contadorexterno = 0
contadorinterno = 0
while contadorexterno <= 9:
    while contadorinterno <= 9:
        print(contadorexterno, contadorinterno)
        contadorinterno += 1

        if contadorinterno > 6:
            break

    contadorexterno += 1
    contadorinterno = 0
