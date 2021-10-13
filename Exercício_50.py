def main():
    s_par = 0
    par = []
    for i in range(6):
        n = int(input('Digite um numero inteiro: '))
        if n%2 == 0:
            s_par += n
            par.append(n)
    print('Voce digitou {} números pares: {}'.format(len(par),par))
    print('A soma desses valores eh igual a {}'.format(s_par))
main()