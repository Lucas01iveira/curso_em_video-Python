def main ():
    v = float(input('Velocidade do veículo em km/h: '))
    if v > 80:
        v_acima = v - 80
        multa = 7*v_acima
        print ('O motorista deve receber uma multa de R$ {:.2f}'.format(multa))
    else:
        print ('O veículo está dentro do limite de velocidade.')
main ()