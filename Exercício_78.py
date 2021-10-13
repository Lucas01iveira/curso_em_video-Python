def main():
    lista = []
    for i in range(5):
        num = int(input('Digite um número: '))
        if i == 0:
            maior = menor = num
            pos_maior = pos_menor = 0
        lista.append(num)

    for c,i in enumerate(lista):
        if i >= maior:
            maior = i
            pos_maior = c
        elif i <= menor:
            menor = i
            pos_menor = c

    print('Segue a lista dos valores inseridos: ', end='')
    for i in range(len(lista)):
        if i != len(lista)-1:
            print(i, end=', ')
        else:
            print(i)
    print(f'O maior número digitado foi {maior}, na posição {pos_maior}.')
    print('O menor número digitado foi {}, na posição {}'.format(menor,pos_menor))


main()