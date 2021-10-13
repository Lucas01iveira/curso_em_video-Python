def main():
    lista = []
    for i in range(5):
        num = int(input('Digite um número: '))
        if i == 0:
            lista.append(num)
            print('Adicionado ao final da lista...')
        else:
            if num >= lista[i-1]:
                lista.append(num)
                print('Aidicionado ao final da lista...')
            else:
                '''for c,j in enumerate(lista):
                    if num < j:
                        lista.insert(c,num)
                        print('Adicionado na posição {}...'.format(c))
                        # break'''
                for j in range(len(lista)):
                    if num < lista[j]:
                        lista.insert(j,num)
                        print('Adicionado na posição {}...'.format(j))
                        #O break é necessário pois desejamos acrescentar o valor na lista logo na primeira ocorrencia
                        #do if; (caso tiremos o break o valor em questão pode ser adicionado mais vezes à lista)
                        break

    print('-='*30)
    print('Os valores digitados, em ordem, foram: {}'.format(lista))


main()