from math import hypot
def main ():
    cat1 = float(input('Informe o comprimento de um dos catetos do triangulo retangulo: '))
    cat2 = float(input('Informe o comprimento do outro cateto do triangulo retangulo: '))
    print ('A hipotenusa desse triangulo mede {:.2f}'.format(hypot(cat1,cat2)))
main()