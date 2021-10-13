def le_matriz():
    a = int(input('Digite a quantidade de linhas da sua matriz: '))
    b = int(input('Digite a quantidade de colunas da sua matriz: '))
    return cria_matriz(a,b)


def cria_matriz(lin,col):
    m = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append(int(input('Entre com o elemento [{}][{}] da matriz: '.format(i+1,j+1))))
        m.append(linha)
    return m


def main():
    A = le_matriz()
    print()
    print('-='*30)
    print('A matriz construída está representada a seguir: ')
    for i in range(len(A)):
        for j in range(len(A[0])):
            print('[{:^5}]'.format(A[i][j]), end='')
        print()

    print('-='*30)
    # O código a seguir refere-se à análise da matriz:
    # 1) Verifico a soma dos valores pares:
    soma_pares = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] %2 == 0:
                soma_pares += A[i][j]

    # 2) Verifico a soma dos valores da 3ª coluna:
    soma_coluna3 = 0
    for i in range(len(A)):
        soma_coluna3 += A[i][2]

    # 3) Verifico o maior valor da segunda linha
    maior = 0
    for j in range(len(A[0])):
        if j == 0:
            maior = A[1][j]
        else:
            if A[1][j] >= maior:
                maior = A[1][j]

    # Apresento os resultados:
    print('A soma dos valores pares é {}.'.format(soma_pares))
    print('A soma dos valores da terceira coluna é {}.'.format(soma_coluna3))
    print('O maior valor da segunda linha é {}.'.format(maior))


main()