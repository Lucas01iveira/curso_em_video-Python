from time import sleep
def main():
    while True:
        print('-='*40)
        n = int(input('Digite o valor do qual você deseja verificar a tabuada [-1 para parar]: '))
        sleep(0.5)
        if n == -1:
            break
        for i in range(11):
            print(f'{n} x {i} = {i*n}')
            sleep(1)
    print('Programa encerrado!')
main()