# Dados um número inteiro e outro número inteiro diferente de zero, informa se o primeiro é divisível pelo segundo.

# Explica o conceito de divisibilidade e a terminologia utilizada pelo programa.
print("Um número (numerador) é divisível por outro (denominador) quando o resultado da divisão é um número inteiro e o resto é zero.")
print("Este programa verifica a divisibilidade de um número por outro.\n\n")
print("-" * 20, "\n\n")

# Repete o programa após o fim de uma execução.
while True:

    # Pede o valor do numerador e verifica se ele é um número racional. Caso não seja, pede novamente.
    while True:
        n = input("Insira o numerador: ")
        try:
            n = float(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.\n")
        if type(n) == float:
            print("")
            break

    # Pede o valor do numerador e verifica se ele é um número racional diferente de zero. Caso não seja, pede novamente.
    while True:
        d = input("Insira o denominador: ")
        try:
            d = float(d)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional diferente de zero e o separador decimal, se presente, deve ser um ponto.\n")
        if type(d) == float:
            if d == 0:
                print("Erro: valor inválido. Ele deve ser um número racional diferente de zero e o separador decimal, se presente, deve ser um ponto.\n")
            else:
                print("")
                break

    # Verifica se o numerador é divisível pelo denominador e imprime o resultado.
    if n % d == 0:
        print(f"{n} é divisível por {d}.\n")
    else:
        print(f"{n} não é divisível por {d}.\n\n")

    # Insere uma linha de 20 hífens e pula duas linhas, para explicitar a reinicialização do programa.
    print("-" * 20, "\n\n")