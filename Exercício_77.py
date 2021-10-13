def main():
    lista = ('Rotacional', 'Divergente', 'Gradiente', 'Nabla', 'Eletrodinamica')
    for i in range(len(lista)):
        print('A palavra {} contém as vogais: '.format(lista[i].upper()), end='')
        for j in range(len(lista[i])):
            if lista[i][j].lower() in 'aeiou':
                if j == len(lista[i]):
                    print('{}'.format(lista[i][j]))
                else:
                    print('{}'.format(lista[i][j]), end=' ')
        print()


main()