from math import sin,cos,tan,radians
def main ():
    x = radians(float(input('Digite um angulo em graus: ')))
    #A conversão para radianos poderia ser feita também com o auxilio da formulinha: (x*pi)/180
    print('O seno desse angulo é igual a {:.2f}'.format(sin(x)))
    print ('O cosseno desse angulo é igual a {:.2f}'.format(cos(x)))
    print('A tangente desse angulo é igual a {:.2f}'.format(tan(x)))
main()

