def main ():
    city = str(input('Digte o nome de uma cidade: '))
    city = city.title().strip().split()
    if city[0] == 'Santo':
        print ('O nome da cidade informada começa com a palavra "Santo"')
    else:
        print ('O nome da cidade informada não começa com a palavra "Santo"')
main()