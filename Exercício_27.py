def main ():
    nome = str(input('Digite um nome completo: '))
    nome = nome.title().strip().split()
    print ('Primeiro nome: {}'.format(nome[0]))
    print ('Ultimo nome: {}'.format(nome[len(nome)-1]))
main ()