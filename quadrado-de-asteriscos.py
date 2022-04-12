while True:

    while True:
        n = input("Insira o tamanho do quadrado a ser impresso: ")
        try:
            n = int(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser inteiro.")
        if type(n) == int:
            print("")
            break

    for i in range(n):
        print("* " * n)