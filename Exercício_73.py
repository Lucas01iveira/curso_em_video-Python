def main():
    times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético - PR',
             'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
             'Bahia', 'Vasco', 'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará',
             'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
    print('='*40)
    print('{:^40}'.format('BRASILEIRÃO 2019'))
    print('='*40)

    print(' -> Os cinco primeiros colocados da tabela são: ', end='')
    for i in range(5):
        if i != 4:
            print(times[i], end=', ')
        else:
            print(times[i],'\n')

    print(' -> Os últimos 4 colocados da tabela são: ', end='')
    for i in range(len(times)-4,len(times)):
        if i != len(times)-1:
            print(times[i], end=', ')
        else:
            print(times[i],'\n')

    pos_chapecoense = times.index('Chapecoense')

    print(' -> Confira a lista, em ordem alfabética, dos times que participaram do campeonato: ')
    times = sorted(times)
    for i in range(len(times)):
        print('   {}'.format(times[i]))
    print()

    print(' -> O time da Chapecoense terminou o campeonato na posição {}'.format(pos_chapecoense+1))


main()