def main():
    lista = [[],[]]
    for i in range(7):
        num = int(input('Digite o {}º valor: '.format(i+1)))
        if num % 2 == 0:
            lista[0].append(num)
        else:
            lista[1].append(num)

    # Apresento os resultados
    print('=-'*30)
    print('Os valores pares digitados foram: {}'.format(sorted(lista[0])))
    print('Os valores ímpares digitados foram: {}'.format(sorted(lista[1])))


main()