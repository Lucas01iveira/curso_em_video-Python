from math import sqrt
def main ():
    cat1 = float(input('Informe a medida de um dos catetos do triangulo retangulo: '))
    cat2 = float(input('Informe a medida do outro cateto do triangulo retangulo: '))
    hipotenusa = sqrt((cat1*cat1)+(cat2*cat2))
    print ('A hipotenusa desse triangulo mede {:.2f}'.format(hipotenusa))
main()