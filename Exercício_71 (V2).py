def main():
    valor = int(input('Informe o valor do saque: R$ '))

    #inicializo o valor da cedula com 50
    ced = 50
    totced = 0

    while True:
        #enquanto o valor do saque for maior que o valor da cedula, efetuo a diferenca
        if valor >= ced:
            valor -= ced
            totced += 1

        #no momento em que o valor deixar de ser maior do que a cedula, printo a relacao e atualizo a cedula
        else:
            #codigo do print na tela
            if totced > 0:
                if totced == 1:
                    palavra = 'cédula'
                else:
                    palavra = 'cédulas'
                print('{} {} de R$ {}'.format(totced,palavra,ced))

            #atualizacao do valor da cedula
            if ced == 50:
                ced = 30
            elif ced == 30:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if valor == 0:
                break
main()
