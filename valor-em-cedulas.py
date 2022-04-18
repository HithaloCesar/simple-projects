cedulas = [2, 5, 10, 20, 50, 100, 200]
moedas = [0.01, 0.05, 0.10, 0.25, 0.50, 1]

while True:

    while True:
        n = input("Insira o valor monetário: ")
        try:
            n = float(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional positivo, e o separador decimal, se presente, deve ser um ponto.\n")
        if type(n) == float:
            if n <= 0:
                print("Erro: valor inválido. Ele deve ser um número racional positivo, e o separador decimal, se presente, deve ser um ponto.\n")
            else:
                print("")
                break
            
    cedulas_moedas = []
    cedulas_moedas.extend(cedulas)
    cedulas_moedas.extend(moedas)
    cedulas_moedas.sort(reverse=True)
    qtd_cada_cedula_moeda = []
    for i in range(len(cedulas_moedas)):
        qtd_cada_cedula_moeda.append(int((n * 100) // (cedulas_moedas[i] * 100)))
        n %= cedulas_moedas[i]
        n = round(n, 2)
        if cedulas_moedas[i] in cedulas:
            if qtd_cada_cedula_moeda[i] > 1:
                cedula_moeda_sing_plur = "cédulas"
            else:
                cedula_moeda_sing_plur = "cédula"
        else:
            if qtd_cada_cedula_moeda[i] > 1:
                cedula_moeda_sing_plur = "moedas"
            else:
                cedula_moeda_sing_plur = "moeda"
        if qtd_cada_cedula_moeda[i] != 0:
            if cedulas_moedas[i] > 1:
                print(qtd_cada_cedula_moeda[i], " ", cedula_moeda_sing_plur, " de ", cedulas_moedas[i], " reais.", sep="")
            elif cedulas_moedas[i] == 1:
                print(qtd_cada_cedula_moeda[i], " ", cedula_moeda_sing_plur, " de ", cedulas_moedas[i], " real.", sep="")
            elif cedulas_moedas[i] < 1 and cedulas_moedas[i] > 0.01:
                print(qtd_cada_cedula_moeda[i], " ", cedula_moeda_sing_plur, " de ", int(cedulas_moedas[i] * 100), " centavos.", sep="")
            else:
                print(qtd_cada_cedula_moeda[i], " ", cedula_moeda_sing_plur, " de ", int(cedulas_moedas[i] * 100), " centavo.", sep="")

    print("\n\n", "-" * 20, "\n\n", sep="")