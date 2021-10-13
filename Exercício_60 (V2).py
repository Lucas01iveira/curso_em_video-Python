def main():
    cont = num = int(input('Digite um número: '))
    fat = 1
    while cont > 0:
        fat = fat*cont
        cont -= 1
    print('{}! = {}'.format(num,fat))
main()