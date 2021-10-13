def main():
    nome = str(input('Digite o nome completo de alguém: '))
    nome = nome.title().strip().split()
    if 'Silva' in nome:
        print ('O nome informado possui sobrenome "Silva"')
    else:
        print ('O nome informado não possui sobrenome "Silva"')
main()