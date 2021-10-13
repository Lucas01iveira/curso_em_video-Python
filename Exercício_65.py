def main():
    soma = 0
    total = 1

    maior = menor = n = int(input('Digite um número: '))
    soma += n
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp != 'S' and resp != 'N':
        while resp != 'S' and resp != 'N':
            print('Comando desconhecido. Por favor, responda novamente.')
            resp = str(input('Deseja continuar? [S/N] ')).strip().upper()

    while resp != 'N':
        print('-='*30)
        #tratamento do valor inserido pelo usuário
        n = int(input('Digite um número: '))
        soma += n
        total += 1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

        #tratamento da resposta do usuário
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp != 'S' and resp != 'N':
            while resp != 'S' and resp != 'N':
                print('Comando desconhecido. Por favor, responda novamente.')
                resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-='*30)
    if total == 1:
        print('Voce digitou apenas um número'.format(total))
    else:
        print('Voce digitou {} números'.format(total))
        media = soma/total
        print('A média entre eles foi {:.2f}'.format(media))
        print('O maior valor digitado foi {}; o menor foi {}'.format(maior,menor))
main()
