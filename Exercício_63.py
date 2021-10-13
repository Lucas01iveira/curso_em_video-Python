def main():
    print('='*45)
    print('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
    print('='*45)
    tot = int(input('Quantos elementos voce deseja visualizar? '))
    a1 = 0
    a2 = 1
    print('{} -> {} -> '.format(a1,a2),end= '')
    cont = 3
    while cont <= tot:
        atual = a1+a2
        if cont == tot:
            print('{} -> FIM'.format(atual))
        else:
            print('{} '.format(atual),end= '-> ')
        a1 = a2
        a2 = atual
        cont += 1
main()