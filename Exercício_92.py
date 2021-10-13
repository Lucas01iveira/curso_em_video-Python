def main():
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = 2020 - int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('Carteira de trabalho (digite 0 se não tem): '))
    if dados['ctps'] != 0:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: R$ '))
        dados['aposentadoria'] = (35 - (2020 - dados['contratação'])) + dados['idade']

    print('=-'*25)
    for k,v in dados.items():
        print('{} tem o valor {}'.format(k,v))


main()