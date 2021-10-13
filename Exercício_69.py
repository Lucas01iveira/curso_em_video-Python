def main():
    resp = 'sim'
    mais18 = homens = menos20 = pessoas = 0
    while resp != 'nao':
        pessoas += 1
        print('='*30)
        print('{:^30}'.format('CADASTRE UMA PESSOA'))
        print('='*30)
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        if sexo != 'M' and sexo != 'F':
            while sexo != 'M' and sexo != 'F':
                sexo = str(input('Dado inválido. Por favor, digite novamente. [M/F]: ')).strip().upper()[0]
        idade = int(input('Informe a idade: '))

        #Verifico se a pessoa (independentemente de ser m ou f) tem mais de 18 anos
        if idade > 18:
            mais18 += 1

        #Verifico o sexo
        if sexo == 'M':
            homens += 1
        elif sexo == 'F':
            if idade < 20:
                menos20 += 1

        resp = str(input('Deseja cadastrar mais dados? [sim/nao]: ')).strip().lower()
        if resp != 'sim' and resp != 'nao':
            while resp != 'sim' and resp != 'nao':
                resp = str(input('Dado inválido. Por favor, digite novamente. Deseja cadastrar mais dados? [sim/nao]: ')).strip().lower()
        print('-='*40)
    print('Voce cadastrou os dados de {} pessoas'.format(pessoas))
    print('Entre elas, {} são homens, {} tem mais de 18 anos e {} são mulheres com menos de 20 anos'.format(homens, mais18,  menos20))


main()