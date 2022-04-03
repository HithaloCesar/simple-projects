# Pede um tempo Unix e informa o dia da semana daquele tempo.

# Repete o programa após o fim de uma execução.
while True:

    # Pede um tempo Unix e verifica se ela é um número inteiro. Caso não seja, pede novamente.
    while True:
        tempo_unix = input("Insira o tempo em Unix: ")
        try:
            tempo_unix = int(tempo_unix)
        except ValueError:
            print("Valor inválido. É necessário que ele seja um número inteiro.")
        if type(tempo_unix) == int:
            break

    # Sabendo que uma unidade de tempo Unix equivale a um segundo e que um dia tem 86400 segundos, calcula o número de dias que se passaram desde o tempo Unix 0.
    dias = tempo_unix / 86400
    
    # Sabendo que no tempo Unix 0, o dia da semana é quinta-feira, descobre e imprime o dia da semana.
    index_dia_semana = int((dias + 3) % 7)
    dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    print(f"Nesse tempo Unix, o dia da semana é uma {dias_da_semana[index_dia_semana]}.")