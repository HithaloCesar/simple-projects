# Paridade de um número inteiro

while True:
    while True:
        n = input("Insira um número inteiro: ")
        try:
            n = int(n)
        except ValueError:
            print("O valor inserido não é válido!\n")
        if type(n) == int:
            break

    if n % 2 == 0:
        print(n, "é par.\n")
    else:
        print(n, "é ímpar.\n")