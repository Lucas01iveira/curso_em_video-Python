def main():
    classe = []
    while True:
        aluno = []
        nome = str(input('Nome: '))
        aluno.append(nome)
        notas = []
        for i in range(2):
            a = float(input('Nota {}: '.format(i+1)))
            notas.append(a)
        aluno.append(notas)

        classe.append(aluno)

        resp = str(input('Deseja inserir mais algum aluno(a)? [s/n]: ')).strip().lower()
        if resp not in 'sn':
            while resp not in 'sn':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: ')).strip().lower()
        if resp == 'n':
            break

    # print(classe)
    # Apresentação dos dados inseridos
    print('-='*30)
    print('No.   ', 'Nome         ', 'MÉDIA')
    # Uma outra forma de fazer esse print (sem precisar ficar acertando a formatação no olho) seria:
    # print('{:<4}'.format('No.'), '{:<10}'.format('Nome'), '{:>8}'.format('Média))
    print('-'*30)

    for i in range(len(classe)):
        print('{:<}'.format(i),'   {:^10}'.format(classe[i][0]), '     {:.2f}'.format((classe[i][1][0] + classe[i][1][1])/2))
    print('-'*30)

    num = 0
    while num != 999:
        num = int(input('Deseja verificar as notas de qual aluno? (999 para parar): '))
        if num > len(classe) and num != 999:
            while num > len(classe) and num != 999:
                num = int(input('Número não encontrado. Por favor, digite novamente: '))
        if num == 999:
            break
        print('Nota 1: {}'.format(classe[num][1][0]))
        print('Nota 2: {}'.format(classe[num][1][1]))
        print('-'*30)
    print('{:=^30}'.format(' Programa encerrado '))


main()