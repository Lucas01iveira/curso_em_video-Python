def main():
    maior = 0
    menor = float(input('Massa corporal da primeira pessoa: '))
    for i in range(4):
        if i == 0:
            palavra = 'segunda'
        elif i == 1:
            palavra = 'terceira'
        elif i == 2:
            palavra = 'quarta'
        elif i == 3:
            palavra = 'quinta'
        peso = float(input('Massa corporal da {} pessoa: '.format(palavra)))
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    print('A maior massa corporal lida foi {}Kg'.format(maior))
    print('A menor massa corporal lida foi {}Kg'.format(menor))
main()