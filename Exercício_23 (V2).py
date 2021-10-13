def main ():
    n = int(input('Digite um número inteiro entre 0 e 9999: '))
    aux = n
    lista = []
    while aux != 0:
        m = aux%10
        lista.append(m)
        aux = aux//10

    if len (lista) == 1:
        print ('Unidade: {}'.format(lista[0]))
        print ('Dezena: 0')
        print ('Centena: 0')
        print ('Milhar: 0')

    if len (lista) == 2:
        print ('Unidade: {}'.format(lista[0]))
        print ('Dezena: {}'.formaT(lista[1]))
        print ('Centena: 0')
        print ('Milhar: 0')

    if len(lista) == 3:
        print ('Unidade: {}'.format(lista[0]))
        print ('Dezena: {}'.format(lista[1]))
        print ('Centena: {}'.format(lista[2]))
        print ('Milhar: 0')

    if len(lista) == 4:
        print ('Unidade: {}'.format(lista[0]))
        print ('Dezena: {}'.format(lista[1]))
        print ('Centena: {}'.format(lista[2]))
        print ('Milhar: {}'.format(lista[3]))
main()