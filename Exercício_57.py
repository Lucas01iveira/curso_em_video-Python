def main():
    sexo = str(input('Informe seu sexo [M/F]: '))
    sexo = sexo.upper()
    if sexo == 'M':
        print('Sexo M registrado com sucesso.')
    elif sexo == 'F':
        print('Sexo F registrado com sucesso.')
    else:
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Dado inválido. Por favor, informe seu sexo [M/F]: ')).upper()
        #uma vez que o algoritmo tenha saido do while, verifico novamente se é M ou F
        if sexo == 'M':
            print('Sexo M registrado com sucesso.')
        elif sexo == 'F':
            print('Sexo F registrado com sucesso.')
main()

