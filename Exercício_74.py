from random import randint
def main():
    maior = menor = a1 = randint(0,10)

    a2 = randint(0,10)
    if a2 >= maior:
        maior = a2
    elif a2 <= menor:
        menor = a2

    a3 = randint(0,10)
    if a3 >= maior:
        maior = a3
    elif a3 <= menor:
        menor = a3

    a4 = randint(0,10)
    if a4 >= maior:
        maior = a4
    elif a4 <= menor:
        menor = a4

    a5 = randint(0,10)
    if a5 >= maior:
        maior = a5
    elif a5 <= menor:
        menor = a5

    tupla = (a1, a2, a3, a4, a5)
    print('Foram sorteados os seguintes números: ', end= '')
    for i in range(len(tupla)):
        if i != len(tupla)-1:
            print(tupla[i], end=' ')
        else:
            print(tupla[i])
    print('O maior número sorteado foi {}.'.format(maior))
    print('O menor número sorteado foi {}.'.format(menor))


main()