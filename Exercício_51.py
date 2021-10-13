def main():
    print('-='*20)
    print('{:^40}'.format('PROGRESSÃO ARITMÉTICA'))
    print('-='*20)
    elemento = int(input('Insira o primeiro elemento da P.A.: '))
    r = int(input('Insira a razao da P.A.: '))
    tot = int(input('Quantos elementos dessa progressão você deseja verificar? '))
    for i in range(tot):
        print('{:^40}'.format(elemento))
        elemento += r
main()