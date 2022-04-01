# Dados o capital, a taxa de juros compostos ao ano e o tempo, informa qual será o montante do investimento.

while True:
    while True:
        c = input("Insira o capital a ser investido, em reais: ")
        try:
            c = float(c)
        except ValueError:
            print("• O valor inserido não é válido!")
            print("• É necessário que ele seja um número racional e que o separador decimal, se presente, seja um ponto.\n")
        if type(c) == float:
            break
    print("")
    while True:
        i = input("Insira a taxa de juros compostos ao ano, em porcentagem: ")
        try:
            i = float(i)
        except ValueError:
            print("• O valor inserido não é válido!")
            print("• Considere que o símbolo de porcentagem está implícito e que o separador decimal, se presente, deve ser um ponto.\n")
        if type(i) == float:
            break
    print("")
    while True:
        t = input("Insira o tempo, em meses: ")
        try:
            t = int(t)
        except ValueError:
            print("• O valor inserido não é válido!")
            print("• É necessário que ele seja um número natural.\n")
        if type(t) == int:
            break
    print("")
    i = i / 100
    t = t / 12
    M = round(c * (1 + i) ** t, 2)
    print(f"O montante desse investimento será R$ {M}.\n\n")
    print(("-" * 40), "\n\n")