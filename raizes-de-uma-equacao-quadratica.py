# Dadas as constantes a, b e c de um equação quadrática, calcula as raízes dessa equação.

# Repete o programa após o fim de uma execução.
while True:

    print("Seja ax²+bx+c a fórmula da equação quadrática, siga as instruções a seguir para obter suas raízes.")

    # Pede o valor da constante a e verifica se ela é um número racional diferente de zero. Caso não seja, pede novamente.
    while True:
        a = input("Insira o valor de a: ")
        try:
            a = float(a)
        except ValueError:
            print("Valor inválido! Ele deve ser um número racional diferente de zero.\n")
        if a == 0:
            print("Valor invalido! Ele deve ser um número racional diferente de zero.\n")
        if type(a) == float and a != 0:
            print ("")
            break

    # Pede o valor da constante b e verifica se ela é um número racional. Caso não seja, pede novamente.
    while True:
        b = input("Insira o valor de b: ")
        try:
            b = float(b)
        except ValueError:
            print("Valor inválido! Ele deve ser um número racional.\n")
        if type(b) == float:
            print ("")
            break

    # Pede o valor da constante c e verifica se ela é um número racional. Caso não seja, pede novamente.
    while True:
        c = input("Insira o valor de c: ")
        try:
            c = float(c)
        except ValueError:
            print("Valor inválido! Ele deve ser um número racional.\n")
        if type(c) == float:
            print ("")
            break

    # Calcula e imprime a solução da equação quadrática, se houver.
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Não há solução no conjunto dos números reais.\n\n")
    elif d == 0:
        x = -b / (2 * a)
        print(f"A raíz dessa equação é {x}.\n\n")
    else:
        d = d ** 0.5
        x1 = round((-b + d) / (2 * a), 2)
        x2 = round((-b - d) / (2 * a), 2)
        print(f"As raízes dessa equação são {x1} e {x2}.\n\n")
    
    # Insere uma linha de 20 hífens e pula duas linhas, para explicitar a reinicialização do programa.
    print("-" * 20, "\n\n")