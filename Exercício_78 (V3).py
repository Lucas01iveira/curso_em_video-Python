def main():
    lista = []
    maior = menor = 0
    for i in range(5):
        lista.append(int(input('Digite um número para a posição {}: '.format(i))))
        if i == 0:
            maior = menor = lista[i]
        else:
            if lista[i] >= maior:
                maior = lista[i]
            elif lista[i] <= menor:
                menor = lista[i]

    print('='*30)
    print('O maior valor digitado foi {} nas posições '.format(maior), end='')
    for c,i in enumerate(lista):
        if i == maior:
            print(c, end='... ')
    print()

    print('O menor valor digitado foi {} nas posições '.format(menor), end='')
    for c,i in enumerate(lista):
        if i == menor:
            print(c, end='... ')


main()