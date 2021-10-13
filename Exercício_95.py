def main():
    craques = []
    while True:
        jogador = dict()
        jogador['nome'] = str(input('Nome do jogador: '))
        partidas = int(input('Quantas partidas ele jogou? '))

        aux = list()
        for i in range(partidas):
            a = int(input('Quantas gols marcou na {}ª partida? '.format(i+1)))
            aux.append(a)
        jogador['gols'] = aux

        total = 0
        for i in jogador['gols']:
            total += i
        jogador['total'] = total

        craques.append(jogador)

        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()
        if resp == 'n':
            break

    print('-'*40)
    print('{:<3}'.format('cod'), '{:<5}'.format('nome'), '{:^20}'.format('gols'), '{:>5}'.format('total'))
    print('-'*40)
    for c,i in enumerate(craques):
        #print(' {}'.format(c), ' {}'.format(i['nome']), '       {}'.format(i['gols']), '      {}'.format(i['total']))
        print('{:<3}'.format(c), '{:<11}'.format(i['nome']), '{}'.format(i['gols']), '{:>10}'.format(i['total']))

    while True:
        print('-'*40)
        cod = int(input('Deseja verificar os dados de qual jogador? '))
        if cod == 999:
            break

        elif cod > len(craques):
            while cod > len(craques):
                cod = int(input('Erro! Código não encontrado. Digite novamente: '))
                for c, i in enumerate(craques):
                    if c == cod:
                        print('Levantamento do jogador {}: '.format(i['nome']))
                        for k, j in enumerate(i['gols']):
                            print('     Na partida {} fez {} gols'.format(k + 1, j))

        else:
            for c,i in enumerate(craques):
                if c == cod:
                    print('Levantamento do jogador {}: '.format(i['nome']))
                    for k,j in enumerate(i['gols']):
                        print('     Na partida {} fez {} gols'.format(k+1,j))

    print()
    print('{:^40}'.format(' Programa Encerrado '))


main()