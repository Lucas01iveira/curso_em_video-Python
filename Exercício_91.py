from random import randint
from time import sleep


def main():
    #Faço esse codigo p evitar numeros repetidos (e consequentes empates)
    aux = list()
    while len(aux) != 4:
        k = randint(1,6)
        if k not in aux:
            aux.append(k)

    jogo = {'jogador 1': aux[0], 'jogador 2': aux[1], 'jogador 3': aux[2], 'jogador 4': aux[3]}

    # Apresento os sorteios:
    print('Valores sorteados: ')
    for c,i in jogo.items():
        print('     O {} tirou {}'.format(c,i))
        sleep(1)

    # Faço o ranqueamento dos jogadores:


main()
