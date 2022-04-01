# Dados n números racionais, informa sua soma e sua média aritmética.

S = 0
while True:
    while True:
        n = input("Insira a quantidade de números cuja soma e média aritmética devem ser calculadas: ")
        print("")
        try:
            n = int(n)
        except ValueError:
            print("Valor inválido! É necessário que seja um número natural positivo.\n")
        if n == 0:
            print("Valor inválido! É necessário que seja um número natural positivo.\n")
        elif type(n) == int:
            break
    for i in range (1, n + 1, 1):
        while True:
            x = input(f"Insira o {i}ᵒ número: ")
            print("")
            try:
                x = float(x)
            except ValueError:
                print("Valor inválido! É necessário que seja um número racional e que o separador decimal, se presente, seja um ponto")
            if type(x) == float:
                break
        S = S + x
    M = round(S/n, 2)
    S = round(S, 2)
    print(f"A soma desses números é {S}.\n")
    print(f"A média aritmética desses números é {M}.")
    print("\n" * 3)