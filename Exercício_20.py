from random import shuffle
def main ():
    alunos = []
    n = int(input('Quantos alunos, no total, desenvolverão o trabalho? '))
    for i in range (n):
        nome = str(input('Digite o nome do {}o aluno(a): '.format(i+1)))
        alunos.append(nome)
    shuffle(alunos)
    print ()
    print ('A ordem de apresentação do trabalho desenvolvido é: ')
    for i in range (len(alunos)):
        print ('{}o - {}'.format(i+1,alunos[i]))
main ()
