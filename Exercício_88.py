from random import randint
from time import sleep
def main():
    print('-'*50)
    print('{:^50}'.format('JOGA NA MEGA SENA AE'))
    print('-'*50)

    tot = int(input('Quantos voce quer que eu sorteie meu consagrado? '))
    print('{:=^40}'.format(' Sorteando {} jogos '.format(tot)))

    lista = []
    for i in range(tot):
        aux = []
        while len(aux) != 6:
            num = randint(1,60)
            if num not in aux:
                aux.append(num)
        lista.append(aux)

    for c,i in enumerate(lista):
        print('Jogo {} : {} '.format(c+1,i))
        sleep(0.75)

    print('-='*6, ' < Boa Sorte! >', '-='*6)


main()