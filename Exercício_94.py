def main():
    pessoas = []
    while True:
        pessoa = dict()
        pessoa['nome'] = str(input('Nome: ')).strip()
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip()
        if pessoa['sexo'] not in 'MmFf':
            while pessoa['sexo'] not in 'MmFf':
                pessoa['sexo'] = str(input('Comando desconhecido. Por favor, digite novamente: '))
        pessoa['idade'] = int(input('Idade: '))
        pessoas.append(pessoa)

        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()
        if resp not in 'sn':
            while resp not in 'sn':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: '))
        if resp == 'n':
            break

    print('=-'*30)
    print('- O grupo tem {} pessoas'.format(len(pessoas)))

    # Calculo a média de idade:
    aux = 0
    for i in pessoas:
        aux += i['idade']
    m = aux/len(pessoas)
    print('- A média de idade é de {:.2f} anos'.format(m))

    # Apresento as mulheres cadastradas
    print('- As mulheres cadastradas foram: ', end='')
    for i in pessoas:
        if i['sexo'] in 'Ff':
            print('[{}] '.format(i['nome']), end='')
    print()

    # Apresento a lista de pessoas que estão acima da média de idade:
    print('- As pessoas que estão acima da média de idade são: ')
    for i in pessoas:
        if i['idade'] >= m:
            for k,v in i.items():
                print('     {}: {}'.format(k,v), end='; ')
            print()
    print('{:=^50}'.format(' ENCERRADO '))



main()