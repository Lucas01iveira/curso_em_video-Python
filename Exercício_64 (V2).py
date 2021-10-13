def main():
    num = 0
    soma = 0
    total = 0
    while num != 999:
        num = int(input('Digite um número [999 para parar]: '))
        if num != 999:
            soma += num
            total += 1
    print('Voce digitou {} valores e a soma entre eles é igual a {}'.format(total,soma))
main()