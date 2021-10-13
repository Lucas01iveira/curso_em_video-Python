def main():
    print('{:=^40}'.format(' GERADOR DE PA '))
    n1 = int(input('Informe o 1o termo: '))
    r = int(input('Informe a razão da PA: '))
    tot = 10
    quant = 0
    while tot != 0:
        cont = 1
        while cont <= tot:
            if cont != tot:
                print('{} -> '.format(n1), end = '')
            else:
                print('{} -> PAUSA'.format(n1))
            n1 += r
            cont += 1
            quant += 1
        tot = int(input('Quantos elementos a mais voce deseja verificar? '))
    print('Progressão finalizada com {} termos mostrados.'.format(quant))
main()