def main():
    resp = 's'
    lista = []
    while resp == 's':
        num = int(input('Digite um número: '))
        lista.append(num)
        resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
        if resp != 's' and resp != 'n':
            while resp != 's' and resp != 'n':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: ')).strip().lower()

    lista_pares = []
    lista_impares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)

    print('=-'*30)
    print('A lista completa dos valores digitados é: {}'.format(lista))
    print('A lista dos valores pares digitados é: {}'.format(lista_pares))
    print('A lista dos valores impares digitados é: {}'.format(lista_impares))


main()