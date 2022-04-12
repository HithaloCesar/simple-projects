from numpy import True_


while True:

    cedulas = []

    faltam_cedulas = True

    start = input("Digite \"br\" para carregar os valores de cédulas e de moedas brasileiras, ou aperte enter para inserir valores customizados: ")
    if start != "br" and start != "":
        print("Erro: resposta inválida.")
    elif start == "br":
        cedulas = [0.01, 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 25, 50, 100, 200]
        print ("")
    else:
        print("")
        while faltam_cedulas:
            while True:
                cedula_atual = (input("Insira um valor de cédula ou de moeda para adicionar, ou aperte enter para finalizar: "))
                if cedula_atual == "":
                    if cedulas == []:
                        print("\nErro: o programa exige pelo menos um valor de cédula ou de moeda.\n")
                    else:
                        faltam_cedulas = False
                        print("")
                        break
                else:
                    try:
                        cedula_atual = float(cedula_atual)
                    except ValueError:
                        print("\nErro: valor inválido. Ele deve ser um número racional positivo, e o separador decimal, se presente, deve ser um ponto.\n")
                    if type(cedula_atual) == float:
                        if cedula_atual <= 0:
                            print("\nErro: valor inválido. Ele deve ser um número racional positivo, e o separador decimal, se presente, deve ser um ponto.\n")
                        elif cedula_atual in cedulas:
                            print("\nErro: valor já inserido.\n")
                        else:
                            if cedula_atual % 1 == 0:
                                cedula_atual = int(cedula_atual)
                            cedulas.append(cedula_atual)
                            cedulas.sort()
                            print("")
                            print("Valores de cédulas inseridos: ", end="")
                            for i in range(len(cedulas)):
                                if i != len(cedulas) - 1:
                                    print (cedulas[i], " | ", sep="", end="")
                                else:
                                    print (cedulas[i])
                                    print("")
                            break
    
    while True:
        n = input("Insira o valor monetário: ")
        try:
            n = float(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional, e o separador decimal, se presente, deve ser um ponto.")
        if type(n) == float:
            print("")
            break

    cedulas.sort(reverse=True)
    qtd_cada_cedula = []
    for i in range(len(cedulas)):
        qtd_cada_cedula.append(n // cedulas[i])
        n %= cedulas[i]
        if qtd_cada_cedula[i] != 0:
            if cedulas[i] > 1:
                print(qtd_cada_cedula[i], " nota(s) ou moeda(s) de ", cedulas[i], " reais.", sep="")
            elif cedulas[i] == 1:
                print(qtd_cada_cedula[i], " nota(s) ou moeda(s) de ", cedulas[i], " real.", sep="")
            elif cedulas[i] < 1 and cedulas[i] > 0.01:
                print(qtd_cada_cedula[i], " nota(s) ou moeda(s) de ", cedulas[i] * 100, " centavo(s).", sep="")
            else:
                print(qtd_cada_cedula[i], " nota(s) ou moeda(s) de ", cedulas[i] * 100, " centavo.", sep="")
    
    print("\n\n", "-" * 20, "\n\n", sep="")