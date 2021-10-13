def main():
    a1 = int(input('Digite um número: '))
    a2 = int(input('Digite outro número: '))
    a3 = int(input('Digite mais um número: '))
    a4 = int(input('Digite o último número: '))
    tupla = (a1, a2, a3, a4)
    print('='*30)

    if tupla.count(9) == 0:
        print('Você não digitou o número 9.')
    else:
        if tupla.count(9) == 1:
            palavra = 'vez'
        else:
            palavra = 'vezes'
        print('O valor 9 apareceu {} {}'.format(tupla.count(9),palavra))

    if 3 not in tupla:
        print('Você não digitou o número 3.')
    else:
        print('O número 3 foi o seu {}o número digitado'.format(tupla.index(3)+1))

    print('Entre os números digitados, os seguintes são pares: ', end='')
    for i in range(len(tupla)):
        if tupla[i] % 2 == 0:
            if i != len(tupla) - 1:
                print(tupla[i], end=' ')
            else:
                print(tupla[i])



main()