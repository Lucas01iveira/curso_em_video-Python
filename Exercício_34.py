def main ():
    s = float(input('Informe o valor do salário: '))
    if s >= 1250:
        print ('Esse funcionário deverá receber um aumento de R$ {:.2f} '.format(0.1*s))
    else:
        print ('Esse funcionário deverá receber um aumento de R$ {:.2f} '.format(0.15*s))
main ()