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


main()