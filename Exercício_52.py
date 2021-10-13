def verifica_primo(x):
    divisores = 0
    cont = 1
    while cont <= x:
        if x%cont == 0:
            divisores += 1
        cont += 1
    if divisores == 2:
        return True
    else:
        return False

def main():
    n = int(input('Digite um numero: '))
    if verifica_primo(n):
        print('O número {} é primo.'.format(n))
    else:
        print('O número {} não é primo.'.format(n))
main()
