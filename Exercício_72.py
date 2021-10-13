def main():
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    a = int(input('Digite um número entre 0 e 20: '))
    if a > 20 or a < 0:
        while a > 20 or a < 0:
            a = int(input('Número inválido. Por favor, digite novamente: '))
    print('Você digitou o número {}.'.format(numeros[a]))


main()