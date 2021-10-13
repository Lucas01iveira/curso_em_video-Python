from random import randrange
def main():
    print('{:=^30}'.format(' JOKENPO! '))
    print('''Jogadas possíveis: 
    [ 1 ] PEDRA 
    [ 2 ] PAPEL
    [ 3 ] TESOURA ''')
    jogador = int(input('Sua escolha: '))
    if jogador != 1 and jogador != 2 and jogador != 3:
        print('ERRO!')
    else:
        print('JO')
        print('KEN')
        print('PO!')
        computador = randrange(1,4)
        print('=-'*30)

        if jogador == 1:
            print('Jogador escolheu PEDRA')
            if computador == 1:
                print('Computador escolheu PEDRA')
                print('=-'*30)
                print('EMPATE!')
            elif computador == 2:
                print('Computador escolheu PAPEL')
                print('=-'*30)
                print('COMPUTADOR VENCE')
            elif computador == 3:
                print('Computador escolheu TESOURA')
                print('=-'*30)
                print('JOGADOR VENCE')

        elif jogador == 2:
            print('Jogador escolheu PAPEL')
            if computador == 1:
                print('Computador escolheu PEDRA')
                print('-='*30)
                print('JOGADOR VENCE')
            elif computador == 2:
                print('Computador escolheu PAPEL')
                print('=-'*30)
                print('EMPATE')
            elif computador == 3:
                print('Computador escolheu TESOURA')
                print('=-'*30)
                print('COMPUTADOR VENCE')

        elif jogador == 3:
            print('Jogador escolheu TESOURA')
            if computador == 1:
                print('Computador escolheu PEDRA')
                print('-=' * 30)
                print('COMPUTADOR VENCE')
            elif computador == 2:
                print('Computador escolheu PAPEL')
                print('=-' * 30)
                print('JOGADOR VENCE')
            elif computador == 3:
                print('Computador escolheu TESOURA')
                print('=-' * 30)
                print('EMPATE')
main()
