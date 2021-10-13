def main():
    peso = float(input('Informe sua massa corporal (kg): '))
    altura = float(input('Informe sua altura (m): '))
    imc = peso/(altura**2)
    if imc < 18.5:
        print('''Seu IMC é igual a {:.2f}. Procure um nutricionista ou se informe sobre sua situação,
pois voce está ABAIXO DO PESO.'''.format(imc))
    elif imc < 25:
        print('''Seu IMC é igual a {:.2f}. Parabéns, você está em seu PESO IDEAL!'''.format(imc))
    elif imc < 30:
        print('''Seu IMC é igual a {:.2f}. Experimente uma dieta 
ou uma prática de exercícios físicos; você está ACIMA DO PESO.'''.format(imc))
    elif imc < 40:
        print('''Seu IMC é igual a {:.2f}. Procure um médico nutricionista; o resultado 
indica grau inicial de OBESIDADE.'''.format(imc))
    else:
        print('''Seu IMC é igual a {:.2f}. Procure um médico nutricionista; o resultado
indica OBESIDADE MÓRBIDA.'''.format(imc))
main()
