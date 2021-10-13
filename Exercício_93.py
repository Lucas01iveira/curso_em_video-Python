def main():
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

    # Apresento os resultados:
    print('=-'*30)
    for k,v in jogador.items():
        print('O campo {} tem valor {}'.format(k,v))

    print('=-'*30)
    print('O jogador {} jogou {} partidas'.format(jogador['nome'],partidas))
    for c,i in enumerate(aux):
        print('     => Na {}ª partida fez {} gols'.format(c+1,i))
    print('Foi um total de {} gols'.format(total))


main()