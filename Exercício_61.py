def main():
    print('{:^40}'.format(' GERADOR DE PA '))
    print('-='*20)
    n1 = int(input('Insira o primeiro termo: '))
    r = int(input('Insira a razão dessa PA: '))
    tot = int(input('Quantos termos voce deseja visualizar? '))
    cont = 1
    while cont <= tot:
        if cont == tot:
            controle = ''
        else:
            controle = '->'
        print('{} {} '.format(n1,controle), end= '')
        n1 = n1 + r
        cont = cont +1
main()
