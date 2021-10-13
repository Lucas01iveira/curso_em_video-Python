def main ():
    n = int(input('Quantos números voce deseja informar? '))
    maior = 0
    menor = int(input('Digite o 1o número: '))
    for i in range(1,n):
        num = int(input('Digite o {}o número: '.format(i+1)))
        if num > maior:
            maior = num
        else:
            if num < menor:
                menor = num
    print ('O maior número digitado foi {}, e o menor foi {}.'.format(maior,menor))
main()