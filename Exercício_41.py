def main():
    nasc = int(input('Ano de nascimento: '))
    idade = 2020 - nasc
    if idade <= 9:
        print('O atleta possui {} anos; se encaixa na categoria MIRIM.'.format(idade))
    else:
        if 9 < idade and idade <= 14:
            print('O atleta possui {} anos; se encaixa na categoria INFANTIL.'.format(idade))
        else:
            if 14 < idade and idade <= 19:
                print('O atleta possui {} anos; se encaixa na categoria JUNIOR.'.format(idade))
            else:
                if 19 < idade and idade <= 25:
                    print('O atleta possui {} anos; se encaixa na categoria SENIOR.'.format(idade))
                else:
                    if 25 < idade:
                        print('O atleta possui {} anos; se encaixa na categoria MASTER.'.format(idade))
main()