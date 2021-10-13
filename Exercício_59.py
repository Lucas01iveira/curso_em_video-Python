from time import sleep

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    #Inicializo a variável resp com valor 0 apenas para iniciar o loop
    # (poderia também ser feita uma primeira rotação antes do início do loop sem nenhum problema; o programa apenas ficaria mais longo)
    resp = 0

    while resp != 5:
        print('-=' * 30)
        print('{:^30}'.format('MENU DE OPÇÕES'))
        print('  [ 1 ] Soma')
        print('  [ 2 ] Multiplcação')
        print('  [ 3 ] Comparação')
        print('  [ 4 ] Novos valores')
        print('  [ 5 ] Sair do programa')
        resp = int(input('Sua escolha: '))

        if resp == 1:
            soma = n1+n2
            print('A soma {} + {} é igual a {}'.format(n1,n2,soma))

        elif resp == 2:
            mult = n1*n2
            print('A multiplicação {} x {} é igual a {}'.format(n1,n2,mult))

        elif resp == 3:
            if n1 > n2:
                print('O número {} é maior que {}'.format(n1,n2))
            elif n1 < n2:
                print('O número {} é maior que {}'.format(n2,n1))
            elif n1 == n2:
                print('O número {} é igual a {}'.format(n1,n2))

        elif resp == 4:
            n1 = int(input('Insira um novo valor: '))
            n2 = int(input('Insira outro novo valor: '))

        else:
            print('Comando desconhecido. Por favor, tente novamente!')

        sleep(1)

    print('Programa Encerrado!')
main()
