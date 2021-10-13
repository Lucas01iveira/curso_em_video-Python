def main():
    num = 0
    soma = 0
    total = 0
    while num != 999:
        #Colocando essas duas variáveis primeiro eu evito o 999 (pelo menos na soma)
        total += 1
        soma += num
        num = int(input('Digite um número [999 para parar]: '))
    #Ao sair do while, o programa ainda registrou +1 no total de valores (rodada do 999). Para ter o total 'correto' de valores inseridos,
    #basta subtrair 1
    total -= 1
    print('Voce digitou {} valores e a soma entre eles é igual a {}'.format(total,soma))
main()