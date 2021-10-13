import random

def advinhe (n):
    resp = int(input('Eu pensei em um número entre 0 e 5. Tente advinhá-lo! \n'))
    if resp == n:
        print('Uau, temos um xerox holmes aqui =O')
    else:
        print('Errado! O numero que eu pensei foi {}.'.format(n))

def main():
    resp = 'sim'
    while resp == 'sim':
        x = random.randrange(0,5)
        advinhe(x)
        resp = str(input('Deseja tentar novamente? '))
        resp = resp.strip().lower()
        print ('-'*20)
main ()