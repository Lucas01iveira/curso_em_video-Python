def main():
    cont = num = int(input('Digite um número: '))
    print('{}! = '.format(num), end='')
    fat = 1
    while cont != 0:
        fat = fat*cont
        if cont == 1:
            controle = '='
        else:
            controle = 'x'
        print('{} {} '.format(cont,controle), end = '')
        cont -= 1
    print('{}'.format(fat))
main()