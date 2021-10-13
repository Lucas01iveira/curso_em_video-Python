def main():
    print('='*29)
    print('{:^30}'.format('ALISTAMENTO MILITAR'))
    print('='*29)
    ano = int(input('Ano de nascimento: '))
    if 2020 - ano < 18:
        if (18 - (2020 - ano)) > 1:
            palavra = 'anos'
        elif (18 - (2020 - ano)) == 1:
            palavra = 'ano'
        print('Esse jovem deve se alistar daqui {} {}.'.format(18 - (2020-ano),palavra))
    elif 2020 - ano > 18:
        if (2020 - ano) - 18 > 1:
            palavra = 'anos'
        elif (2020 - ano) - 18 == 1:
            palavra = 'ano'
        print('Esse jovem passou do período de alistamento há {} {}.'.format((2020 - ano)-18,palavra))
        print('O alistemando d')
    else:
        print('Esse jovem deve se alisar ainda este ano.')
main()