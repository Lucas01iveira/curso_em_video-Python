from datetime import date
sexo = str(input('Sexo: '))
if sexo.strip().lower() == 'feminino':
    print('O alistamento militar não é obrigatório para as mulheres')
elif sexo.strip().lower() == 'masculino':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
    if idade == 18:
        print('Voce deve se alistar ainda este ano!')
    elif idade > 18:
        saldo = idade - 18
        print('Voce deveria ter se alistado há {} ano(s) (ou seja, em {})'.format(saldo,atual-saldo))
    elif idade < 18:
        saldo = 18 - idade
        print('Voce deve se alistar daqui {} ano(s) (ou seja, em {})'.format(saldo,atual + saldo))