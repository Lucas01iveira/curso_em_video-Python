import random
def main ():
    alunos = []
    for i in range (4):
        nome = str(input('Digite o nome do {}o aluno(a): '.format(i+1)))
        alunos.append(nome)
    print ('O aluno sorteado para apagar a lousa é:  \n {}'.format(random.choice(alunos)))
main ()