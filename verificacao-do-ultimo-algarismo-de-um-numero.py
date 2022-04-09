# Dados um número inteiro e um algarismo, verifica se o algarismo é o último dígito do número.

while True:

    while True:
        num = input("Insira um número racional: ")
        try:
            num = float(num)
        except ValueError:
            print("Erro: valor inválido. O separador decimal, se presente, deve ser um ponto.\n")
        if type(num) == float:
            print("")
            if num % 1 == 0:
                num = int(num)
            break
    
    while True:
        alg = input("Insira um algarismo: ")
        try:
            alg = int(alg)
        except ValueError:
            print("Erro: valor inválido.\n") 
        if type(alg) == int:
            if alg > 9 or alg < 0:
                print("Erro: valor inválido.\n") 
            else:
                print("")
                break
    
    i = num
    while i - int(i) != 0:
        i = i * 10
    num_sem_decimais = i
    
    ultimo_alg = abs(num_sem_decimais) % 10

    if ultimo_alg == alg:
        print(f"{alg} é, de fato, o último algarismo de {num}.\n\n")
    else:
        print(f"{alg} não é o último algarismo de {num}.\n\n")
    
    print("-" * 20, "\n\n")