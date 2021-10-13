def main():
    valor = aux = int(input('Informe o valor do saque: R$ '))

    notas50 = aux//50
    aux = aux % 50

    notas30 = aux//30
    aux = aux % 30

    notas10 = aux//10
    aux = aux % 10

    notas1 = aux//1

    print('''O valor de R$ {} será entregue da seguinte forma: 
            
            {} notas de R$ 1
            {} notas de R$ 10
            {} notas de R$ 30
            {} notas de R$ 50'''.format(valor,notas1,notas10,notas30,notas50))
main()
