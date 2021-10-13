from random import randrange
def main():
    num = randrange(1,11)
    print('Sou seu computador...')
    print('Acabei de pensar em número entre 0 e 10. Será que voce consegue advinhá-lo?')
    tent = int(input('Qual é o seu palpite? '))
    num_tent = 1
    while tent != num:
        if tent > num:
            tent = int(input('Menos... Tente mais uma vez: '))
            num_tent += 1
        elif tent < num:
            tent = int(input(('Mais... Tente mais uma vez: ')))
            num_tent += 1
    print('Acertou com {} tentativas. Parabéns!'.format(num_tent))
main()