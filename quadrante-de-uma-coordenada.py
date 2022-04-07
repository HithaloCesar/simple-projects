# Dadas a abscissa e a ordenada de um ponto, imprime o quadrante ou o eixo desse ponto no plano cartesiano.

while True:

    while True:
        x = input("Insira o valor da abscissa (x): ")
        try:
            x = float(x)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(x) == float:
            print("")
            break

    while True:
        y = input("Insira o valor da ordenada (y): ")
        try:
            y = float(y)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
        if type(y) == float:
            print("")
            break

    if x > 0:
        if y > 0:
            print("O ponto está no 1º quadrante.")
        elif y < 0:
            print("O ponto está no 4º quadrante.")
        else:
            print("O ponto está na parte positiva do eixo das abscissas (x)")
    elif x < 0:
        if y > 0:
            print("O ponto está no 2º quadrante.")
        elif y < 0:
            print("O ponto está no 3º quadrante.")
        else:
            print("O ponto está na parte negativa do eixo das abscissas (x).")
    elif y > 0:
        print("O ponto está na parte positiva do eixo das ordenadas (y).")
    elif y < 0:
        print("O ponto está na parte negativa do eixo das ordenadas (y).")
    else:
        print("O ponto está na origem.")
    
    print("\n\n", "-" * 20, "\n\n", sep = "")