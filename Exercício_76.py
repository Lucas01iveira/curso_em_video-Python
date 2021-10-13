def main():
    # Alterar os dados da tupla caso desejar ver outros produtos na listagem
    lista = ('Calculadora', 30.00, 'Lápis', 8.00, 'Notebook', 2600, 'Estojo', 23.50, 'Borracha', 1.50, 'Apontador', 3.50, 'Caneta', 2.30)
    print('-'*40)
    print('{:^40}'.format('LISTAGEM DE PREÇOS'))
    print('-'*40)
    for i in range(0,len(lista)-1,2):
        print('{:.<30}'.format(lista[i]),'R$ {:.2f}'.format(lista[i+1]))
    print('-'*40)


main()