def main():
    lista = []
    tot = 0
    while True:
        num = int(input('Digite um número: '))
        tot += 1
        lista.append(num)
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if resp not in 'SN':
            while resp not in 'SN':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: ')).strip().upper()
        if resp == 'N':
            break

    print('=-'*30)
    print('Você digitou {} números no total'.format(tot))
    print('Em ordem decrescente, os números ficam dispostos da seguinte forma: ', end='')
    # faco a organizacao da lista em ordem decrescente
    lista = sorted(lista, reverse=True)
    for c,i in enumerate(lista):
        if c != len(lista)-1:
            print(i, end=', ')
        else:
            print(i)

    if 5 in lista:
        print('O valor 5 foi encontrado na posição {} da lista'.format(lista.index(5)+1))
    else:
        print('O valor 5 nao foi encontrado na lista')


main()