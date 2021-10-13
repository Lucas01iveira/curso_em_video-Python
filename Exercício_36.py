def main ():
    casa = int(input('Qual o valor da casa a qual está sendo negociada? R$ '))
    salario = int(input('Qual o salário do comprador? R$ '))
    tempo = int(input('Em quantos anos o comprador deseja parcelar a dívida? '))
    parcela = casa/tempo
    print ('='*30)
    if parcela <= (0.3*salario):
        print('Para pagar uma casa de R$ {} em {} anos, o valor de cada parcela deve ser R$ {:.2f}'.format(casa,tempo,parcela))
        print('Empréstimo pode ser CONCEDIDO')
    else:
        print('O valor das parcelas excede 30% do salário do comprador.')
        print ('Empréstimo NEGADO')
main()