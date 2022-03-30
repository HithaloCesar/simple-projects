# Calcula a média aritmética de três números racionais

print("Os números inseridos devem ser racionais e o separador decimal, se presente, deve ser um ponto.\n")
while True:
    while True:
        x1 = input("Insira o primeiro número: ")
        print("")
        try:
            x1 = float(x1)
        except ValueError:
            print("O valor inserido é inválido!\n")
        if type(x1) == float:
            break
    while True:
        x2 = input("Insira o segundo número: ")
        print("")
        try:
            x2 = float(x2)
        except ValueError:
            print("O valor inserido é inválido!\n")
        if type(x2) == float:
            break
    while True:
        x3 = input("Insira o terceiro número: ")
        print("")
        try:
            x3 = float(x3)
        except ValueError:
            print("O valor inserido é inválitesdo!\n")
        if type(x3) == float:
            break
    M = round((x1 + x2 + x3) / 3, 2)
    print(f"A média aritmética de desses números é {M}.\n\n")