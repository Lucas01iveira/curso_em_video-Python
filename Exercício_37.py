def main():
    num = int(input('Digite um numero na base decimal: '))
    print('''Voce deseja converte-lo para qual base de numeracao? 
                    [ 1 ] Binaria
                    [ 2 ] Octal 
                    [ 3 ] Hexadecimal''')
    resp = int(input('Sua escolha: '))

    if resp == 1:
        print('O numero {} (base decimal) eh igual a {} (base binaria)'.format(num,bin(num)[2:]))
    else:
        if resp == 2:
            print('O numero {} (base decimal) eh igual a {} (base octal)'.format(num,oct(num)[2:]))
        else:
            if resp == 3:
                print('O numero {} (base decimal) eh igual a {} (base hexadecimal)'.format(num,hex(num)[2:]))
            else:
                print('Comando desconhecido, tente novamente.')
main()