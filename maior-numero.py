# Dados n números racionais, informa qual é o maior.

while True:

    while True:
        n = input("Insira a quantidade de números a serem comparados: ")
        try:
            n = int(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser um número inteiro positivo.")
        if type(n) == int:
            print("")
            break
    
    for i in range (n):
        while True:
            num = input(f"Insira o {i+1}º número: ")
            try:
                num = float(num)
            except ValueError:
                print("Erro: valor inválido. Ele deve ser um número racional e o separador decimal, se presente, deve ser um ponto.")
            if type(num) == float:
                print("")
                break
        if i == 0:
            num_maior = num
        elif num > num_maior:
            num_maior = num
        num_anterior = num

    if num_maior % 1 == 0:
        num_maior = int(num_maior)

    print("O maior número inserido foi ", num_maior, ".", sep = "")

    print("\n\n", "-" * 20, "\n\n", sep = "")