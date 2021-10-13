def main():
    tot = int(input('Quantos alunos estao inscritos na turma? '))
    cont = 1
    while cont <= tot:
        print('='*30)
        print('           Aluno {}'.format(cont))
        n1 = float(input('Insira a primeira nota desse aluno: '))
        n2 = float(input('Insira a segunda nota desse aluno: '))
        media = (n1 + n2)/2
        if media < 5.0:
            print('Media final: {:.1f}'.format(media),'.O aluno foi reprovado.')
        elif media < 7.0 and media >= 5.0:
            print('Media final: {:.1f}'.format(media),'.O aluno esta de recuperacao')
        else:
            print('Media final {:.1f}'.format(media),'.O aluno foi aprovado!')
        cont += 1
main()
