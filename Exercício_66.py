def main():
    quantidade = soma = 0
    while True:
        n = int(input('Digite um número [999 para parar]: '))
        if n == 999:
            break
        soma += n
        quantidade += 1
    if quantidade == 1:
        print('Você digitou apenas 1 número')
    else:
        print(f'Voce digitou {quantidade} números e a soma entre eles é igual a {soma}')
main()