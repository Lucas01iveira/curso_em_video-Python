def calcula_preco (d):
    if d <= 200:
        return d*(0.5)
    return d*(0.45)

def main():
    distancia = int(input('Informe a distância, em km, ao destino desejado: '))
    p = calcula_preco(distancia)
    print ('O preço da sua viagem é R$ {:.2f}'.format(p))
main()