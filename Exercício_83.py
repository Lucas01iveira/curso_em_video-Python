def main():
    a = str(input('Digite a expressão: '))
    cont1 = 0
    cont2 = 0

    for i in a:
        if i == '(':
            cont1 += 1
        elif i == ')':
            cont2 += 1

    if cont1 == cont2:
        print('Sua expressão é válida')
    else:
        print('Sua expressão está errada')


main()