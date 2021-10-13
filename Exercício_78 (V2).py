# INCORRETO !!!!

def main():
    lista = []
    for i in range(5):
        num = int(input('Digite um número para a posição {}: '.format(i+1)))
        lista.append(num)

    maior = menor = lista[0]
    pos_maior = []
    pos_menor = []

    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
            pos_maior.append(i)

        elif lista[i] <= menor:
            menor = lista[i]
            pos_menor.append(i)

    #tratamento da lista de posições do menor para que ela contenha apenas as posições do menor valor
    for i in pos_menor:
        if lista[i] != menor:
            pos_menor.remove(i)

    #tratamento da lista de posições do maior para que ela contenha apenas as posições do maior valor
    for i in pos_maior:
        if lista[i] != maior:
            pos_maior.remove(i)

    '''outra maneira de fazer essa parte seria:
    for c,i in enumerate(lista):
        if i >= maior:
            maior = i
            pos_maior = c
        elif i <= menor:
            menor = i
            pos_menor = c'''

    print('=' * 50)
    print('Você digitou os valores: ', end='')
    for i in range(len(lista)):
        if i != len(lista)-1:
            print(lista[i], end=', ')
        else:
            print(lista[i])

    #tratamento de str
    if len(pos_menor) == 1:
        palavra_menor = 'na posição'
    else:
        palavra_menor = 'nas posições'

    if len(pos_maior) == 1:
        palavra_maior = 'na posição'
    else:
        palavra_maior = 'nas posições'

    #apresentação na tela
    print('O maior número digitado foi {}; {} '.format(maior,palavra_maior), end='')
    if len(pos_maior) == 1:
        print(pos_maior[0])
    else:
        for i in range(len(pos_maior)):
            if i != len(pos_maior) - 1:
                print(pos_maior[i]+1, end=', ')
            else:
                print(pos_maior[i]+1)

    print('O menor número digitado foi {}; {} '.format(menor,palavra_menor), end='')
    if len(pos_menor) == 1:
        print(pos_menor[0])
    else:
        for i in range(len(pos_menor)):
            if i != len(pos_menor) - 1:
                print(pos_menor[i]+1, end=', ')
            else:
                print(pos_menor[i]+1)


main()