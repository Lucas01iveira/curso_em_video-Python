def main():
    resp = 'sim'
    lista = []

    while resp == 'sim':
        num = int(input('Digite um número: '))
        if num not in lista:
            lista.append(num)

        resp = str(input('Deseja inserir mais valores? [sim/nao]: ')).strip().lower()
        if resp != 'sim' and resp != 'nao':
            while resp != 'sim' and resp != 'nao':
                resp = str(input('Resposta desconhecida. Digite novamente: ')).strip().lower()

    print('='*30)
    print('Voce digitou os valores {}'.format(sorted(lista)))


main()