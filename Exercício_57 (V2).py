def main():
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    sexo = sexo[0]
    while sexo not in 'MmFf':
        sexo = str(input('Dado inválido. Por favor, informe seu sexo [M/F] : '))
    if sexo in 'Mm':
        print('Sexo "Masculino" registrado com sucesso!')
    elif sexo in 'Ff':
        print('Sexo "Feminino" registrado com sucesso!')
main()
