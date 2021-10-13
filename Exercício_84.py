def main():
    dados = []
    pessoas = []
    tot = 0

    # Efetuo a leitura do primeiro dado inserido pelo usuário
    nome = str(input('Nome: '))
    maior = menor = peso = int(input('Peso (kg): '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    tot += 1
    resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    if resp not in 'sn':
        while resp not in 'sn':
            resp = str(input('Comando desconhecido, por favor, digite novamente: '))

    while resp == 's':
        # Cadastro a pessoa
        print()
        nome = str(input('Nome: '))
        peso = int(input('Peso (kg): '))
        dados.append(nome)
        dados.append(peso)
        tot += 1
        pessoas.append(dados)
        dados = []

        # Verifico seu peso:
        if peso >= maior:
            maior = peso
        elif peso <= menor:
            menor = peso

        # Tratamento da resposta:
        resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
        if resp != 's' and resp != 'n':
            while resp != 's' and resp != 'n':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: '))

    # Apresento os resultados
    print('=-'*30)
    print(f'Você cadastrou {tot} pessoas.')

    # Maior peso
    print('O maior peso cadastrado foi {} kg. Peso de : '.format(maior), end='')
    for i in pessoas:
        if i[1] == maior:
            print('[{}] '.format(i[0]), end='')
    print()

    # Menor peso
    print('O menor peso cadastrado foi {} kg. Peso de : '.format(menor), end='')
    for i in pessoas:
        if i[1] == menor:
            print('[{}] '.format(i[0]), end='')
    print()


main()