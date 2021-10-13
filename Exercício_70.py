def main():
    print('-' * 30)
    print('{:^30}'.format('INSIRA UM PRODUTO'))
    print('-' * 30)

    #entro com os dados iniciais
    mais1000 = 0
    nome_menor = str(input('Nome: '))
    total = menor = preco = float(input('Preço R$ '))
    if preco > 1000:
        mais1000 += 1

    #verifico se o usuario deseja inserir mais produtos ou nao
    resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    if resp != 's' and resp != 'n':
        while resp != 's' and resp != 'n':
            resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()

    #aqui nao precisa colocar um if, se a resp for n o programa nem entra no while
    while resp == 's':
        print('-'*30)
        print('{:^30}'.format('INSIRA UM PRODUTO'))
        print('-'*30)
        nome = str(input('Nome: '))
        preco = float(input('Preço R$ '))
        total += preco

        if preco > 1000:
            mais1000 += 1

        if preco < menor:
            menor = preco
            nome_menor = nome

        resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
        if resp not in 'ns':
            while resp not in 'ns':
                resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()

    print('Voce deverá pagar R$ {}.'.format(total))
    print('Entre os produtos comprados, {} possuem preço maior que R$ 1000.00 e o {} foi o mais barato comprado.'.format(mais1000, nome_menor))


main()