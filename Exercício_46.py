from time import sleep
def main():
    print('{:=^30}'.format(' CONTAGEM REGRESSIVA '))
    for i in range(10,-1,-1):
        print('{:^28}'.format(i))
        sleep(1)
    print('{:=^30}'.format(' HOJE É O MANDELINHA DE QUEBRINHA '))
main()