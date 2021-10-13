from time import sleep
from random import randint
def main():
    jogador = 0
    while True:
        op_jogador = str(input('Voce escolhe par ou impar? ')).strip().lower()
        if op_jogador != 'par' and op_jogador != 'impar':
            while op_jogador != 'par' and op_jogador != 'impar':
                op_jogador = str(input('Dado inválido. Por favor, digite novamente. Par ou impar? ')).strip().lower()

        if op_jogador == 'par':
            print('Muito bem. Ficarei com impar.')
            num_computador = randint(0, 10)
            print('-'*30)
            sleep(1)
            print('{:^30}'.format('PAR'))
            sleep(1)
            print('{:^30}'.format('OU'))
            sleep(1)
            print('{:^30}'.format('IMPAR'))
            sleep(1)
            print('-'*30)
            num_jogador = int(input('Qual número você escolheu? '))
            print('Eu escolhi o número {}'.format(num_computador))
            sleep(0.5)
            soma = num_computador+num_jogador
            if soma%2 == 0:
                print('{} + {} = {} que é par! Voce venceu!'.format(num_jogador, num_computador, soma))
                jogador += 1
            else:
                print('{} + {} = {} que é impar! Eu venci!'.format(num_computador, num_jogador, soma))
                break

        elif op_jogador == 'impar':
            # mesmo codigo se repete, apenas com algumas alteracoes nos prints
            print('Muito bem. Ficarei com par.')
            num_computador = randint(0, 10)
            print('-' * 30)
            sleep(1)
            print('{:^30}'.format('PAR'))
            sleep(1)
            print('{:^30}'.format('OU'))
            sleep(1)
            print('{:^30}'.format('IMPAR'))
            sleep(1)
            print('-' * 30)
            num_jogador = int(input('Qual número você escolheu? '))
            print('Eu escolhi o número {}'.format(num_computador))
            sleep(0.5)
            soma = num_computador + num_jogador
            if soma % 2 != 0:
                print('{} + {} = {} que é impar! Voce venceu!'.format(num_jogador, num_computador, soma))
                jogador += 1
            else:
                print('{} + {} = {} que é par! Eu venci!'.format(num_jogador, num_computador, soma))
                break
        print('='*30)
    print('='*30)
    if jogador == 0:
        print('Fim de jogo! Você não venceu nenhuma vez.')
    elif jogador == 1:
        print('Fim de jogo! Você venceu 1 vez.')
    else:
        print('Fim de jogo! Você venceu {} vezes consecutivas!'.format(jogador))
main()