def existe_triangulo (a,b,c):
    aux = False
    if a < b+c and b < a+c and c < a+b:
        aux = True
    return aux

def analisa_triangulo(x,y,z):
    if x != y and y != z and x != z:
        print('Com as medidas inseridas eh possivel formar um triangulo ESCALENO')
    elif x == y and y == z:
        print('Com as medidas inseridas eh possivel formar um triangulo EQUILATERO')
    elif (x == y) or (x == z) or (y == z):
        print('Com as medidas inseridas eh possivel formar um triangulo ISOSCELES')


def main():
    lados = []
    for i in range(3):
        lados.append(int(input('Digite o valor de um dos lados do triangulo: ')))
    forma_tri = existe_triangulo(lados[0],lados[1],lados[2])
    if forma_tri:
        analisa_triangulo(lados[0],lados[1],lados[2])
    else:
        print('Com as medidas inseridas eh impossivel formar um triangulo')
main()