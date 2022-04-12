while True:

    while True:
        print("Esse programa deve analisar os números de 0 até n, e dizer quais são primos.")
        n = input("Insira n: ")
        try:
            n = int(n)
        except ValueError:
            print("Erro: valor inválido. Ele deve ser inteiro.")
        if type(n) == int:
            print("")
            break
    
    is_prime = []
    for i in range(n + 1):
        is_prime.append(True)

    is_prime[0] = is_prime[1] = False

    q = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            q += 1
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    for i in range(n + 1):
        if is_prime[i]:
            print(i)

    print("")
    print(f"Há {q} números primos de 0 a {n}.")

    print("\n\n", "-" * 20, "\n\n", sep="")