def main ():
    l1 = int(input('Informe o comprimento de uma reta: '))
    l2 = int(input('Informe o comprimento de outra reta: '))
    l3 = int(input('Informe o comprimento de uma terceira reta: '))
    if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
        print ('Com as retas informdas, é possível formar um triângulo!')
    else:
        print ('Com as retas informadas, é impossível formar um triângulo!')
main()