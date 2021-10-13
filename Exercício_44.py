def main():
    print('{:=^40}'.format(' LOJAS GUANABARA '))
    preco = int(input('Preço das compras: R$ '))
    print('Como deseja efetuar o pagamento? ')
    print('''    [ 1 ] À vista em dinheiro/cheque (10% off)
    [ 2 ] À vista no cartão (5% off)
    [ 3 ] 2x no cartão (sem juros)
    [ 4 ] 3x (ou mais) no cartão (20% juros)''')
    opcao = int(input('''Resposta: '''))

    if opcao == 1:
        print('Na opção escolhida você recebe 10% de desconto!')
        print('TOTAL A PAGAR: R$ {}'.format(preco - (preco * 0.1)))
        print('Obrigado pela compra. Agradecemos a preferência!')

    elif opcao == 2:
        print('Nessa opcao você recebe 5% de desconto.')
        print('TOTAL A PAGAR: R$ {}'.format(preco - (preco * 0.05)))
        print('Obrigado pela compra. Agradecemos a preferência!')

    elif opcao == 3:
        print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(preco/2))
        print('Obrigado pela compra. Agradecemos a preferência!')

    elif opcao == 4:
        print('CONFIRMAÇÃO DE PARCELAMENTO 3x NO CARTÃO')
        print('     [ 1 ] Sim')
        print('     [ 2 ] Não')
        resp = int(input('Opção: '))
        if resp == 1:
            print('TOTAL A PAGAR: R$ {}'.format(preco + 0.2 * preco))
            print('Sua compra será parcelada em 3x de R$ {:.2f}'.format((preco + preco*0.2)/3))
            print('Obrigado pela compra. Agradecemos a preferência!')
        else:
            quant = int(input('Em quantas vezes deseja parcelar a dívida? '))
            print('TOTAL A PAGAR: R$ {}'.format(preco + 0.2 * preco))
            print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(quant,(preco+0.2*preco)/quant))
            print('Obrigado pela compra. Agradecemos a preferência!')

    else:
        print('''ERRO: COMANDO DESCONHECIDO!
Para evitar maiores problemas, sua compra foi cancelada. Desculpe o transtorno.''')
main()