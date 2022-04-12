while True:

    while True:
        n = input("Insira o valor em reais: ")
        try:
            n = float(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número racional, e o separador decimal, se presente, deve ser um ponto.")
        if type(n) == float:
            print("")
            break

    qtd200 = n // 200
    n %= 200

    qtd100 = n // 100
    n %= 100
    
    qtd50 = n // 50
    n %= 50
    
    qtd20 = n // 20
    n %= 20
    
    qtd10 = n // 10
    n %= 10

    qtd5 = n // 5
    n %= 5
    
    qtd2 = n // 2
    n %= 2

    qtd1 = n // 1
    n %= 1

    qtd_50 = n // 0.5
    n %= 0.5

    qtd_25 = n // 0.25
    n %= 0.25

    qtd_10 = n // 0.1
    n %= 0.1

    qtd_05 = n // 0.05
    n %= 0.05

    qtd_01 = n // 0.01
    n %= 0.01
    
    print(qtd200, "nota(s) de 200 reais.")
    print(qtd100, "nota(s) de 100 reais.")
    print(qtd50, "nota(s) de 50 reais.")
    print(qtd20, "nota(s) de 20 reais.")
    print(qtd10, "nota(s) de 10 reais.")
    print(qtd5, "nota(s) de 5 reais.")
    print(qtd2, "nota(s) de 2 reais.")
    print(qtd1, "moeda(s) de 1 real.")
    print(qtd_50, "moeda(s) de 50 centavos.")
    print(qtd_25, "moeda(s) de 25 centavos.")
    print(qtd_10, "moeda(s) de 10 centavos.")
    print(qtd_05, "moeda(s) de 5 centavos.")
    print(qtd_01, "moeda(s) de 1 centavo.")