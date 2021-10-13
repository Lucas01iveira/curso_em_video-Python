def main():
    nome = str(input('Digite seu nome completo meu chapa: '))
    #Escrevo o nome do usuário com todas as letras maiúsculas
    if nome.isupper():
        print('Voce ja digitou seu nome com as letras maiúsculas =)')
    else:
        print('Reescrevendo todas as letras agora como maiúsculas, seu nome fica da seguinte forma: {}'.format(nome.upper()))

    #Escrevo o nome do usuário com todas as letras minúsculas
    if nome.islower():
        print('Voce ja inseriu seu nome com todas as letras  minúsculas =)')
    else:
        print('Reescrevendo todas as letras agora como minúsculas, seu nome fica da seguinte forma: {}'.format(nome.lower()))

    #Conto a quantidade de letras sem considerar espaços'''
    aux = nome.strip().split()
    aux = ''.join(aux)
    print('Seu nome possui, no total, {} letras'.format(len(aux)))

    #Verifico quantas letras tem o primeiro nome
    aux = nome.strip().split()
    print('Seu primeiro nome possui, no total, {} letras'.format(len(aux[0])))
main()