def main():
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite outro numero inteiro: '))
    if a > b:
        print('O primeiro valor eh maior que o segundo')
    elif a < b:
        print('O segundo valor eh maior que o primeiro')
    else:
        print('Nao existe valor maior, ambos sao iguais')
main()