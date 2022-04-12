while True:

    while True:
        x1 = input("Insira a abscissa do primeiro ponto: ")
        try:
            x1 = float(x1)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(x1) == float:
            print("")
            break
    
    while True:
        y1 = input("Insira a ordenada do primeiro ponto: ")
        try:
            y1 = float(y1)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(y1) == float:
            print("")
            break

    while True:
        x2 = input("Insira a abscissa do segundo ponto: ")
        try:
            x2 = float(x2)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(x2) == float:
            print("")
            break

    while True:
        y2 = input("Insira a ordenada do segundo ponto: ")
        try:
            y2 = float(y2)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(y2) == float:
            print("")
            break

    d = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    print(f"A distância entre os pontos é {d}.")

    print("\n\n", "-" * 20, "\n\n", sep="")