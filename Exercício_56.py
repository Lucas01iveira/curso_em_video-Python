#so funciona se necesseriamente houverem homens e mulheres em uma execucao do programa
def main():
    tot = int(input('Quantas pessoas serão analisadas? '))
    idade_max = 0
    soma_idade = 0
    m_menor20 = 0

    for i in range(tot):
        print('{:=^20}'.format(' {}a Pessoa '.format(i+1)))
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        soma_idade += idade
        sexo = str(input('Sexo [M/F] : '))

        if sexo == 'F' or sexo == 'f':
            if idade < 20:
                m_menor20 += 1

        if sexo == 'M' or sexo == 'm':
            if idade > idade_max:
                idade_max = idade
                mais_velho = nome

    media_idade = soma_idade/tot
    print('='*20)
    print('A média de idade do grupo é de aproximadamente {:.1f} anos.'.format(media_idade))
    print('O homem mais velho é {}, com {} anos.'.format(mais_velho,idade_max))
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(m_menor20))
main()