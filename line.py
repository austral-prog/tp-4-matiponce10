import math

def line():
    # coeficiente_a = 2.3
    # coeficiente_b = -4.0
    # coeficiente_x1 = 50
    # coeficiente_x2 = -32.9
    coeficiente_a = float(input("Ingrese el coeficiente A:\n"))
    coeficiente_b = float(input("Ingrese el coeficiente B:\n"))
    coeficiente_x1 = float(input("Ingrese el coeficiente X1:\n"))
    coeficiente_x2 = float(input("Ingrese el coeficiente X2:\n"))

    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_x2}")
    print("")
    coeficiente_y1 = coeficiente_a * coeficiente_x1 + coeficiente_b
    coeficiente_y2 = coeficiente_a * coeficiente_x2 + coeficiente_b

    print(f"Para la siguiente ecuación:")
    print(f"\tY = {coeficiente_a}X + {coeficiente_b}")
    print("")
    print(f"Dados los siguientes puntos:")
    print(f"\tP1 ({coeficiente_x1}, {coeficiente_y1})")
    print(f"\tP2 ({coeficiente_x2}, {coeficiente_y2})")
    print("")
    distancia_entre_dos_puntos =  math.sqrt( ( math.pow(coeficiente_x2 - coeficiente_x1, 2) ) + ( math.pow(coeficiente_y2 - coeficiente_y1, 2) ) )
    print(f"La distancia entre ellos es: {distancia_entre_dos_puntos}")
