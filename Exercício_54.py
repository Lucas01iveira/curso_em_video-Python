def main():
    tot = int(input('Quantas pessoas deseja analisar? '))
    maior18 = 0
    menor18 = 0
    for i in range(tot):
        nasc = int(input('Digite o ano de nascimento da {}a pessoa: '.format(i+1)))
        idade = 2020 - nasc
        if idade > 18:
            maior18 += 1
        else:
            menor18 += 1
    print('Entre as pessoas inseridas, {} atingiram a maioridade enquanto {} ainda não.'.format(maior18,menor18))
main()
