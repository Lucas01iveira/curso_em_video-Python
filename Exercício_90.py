def main():
    alunos = []
    while True:
        dados = dict()
        dados['nome'] = str(input('Nome do aluno(a): '))
        dados['nota'] = float(input('Nota: '))
        if dados['nota'] >= 7:
            dados['situacao'] = 'Aprovado'
        else:
            dados['situacao'] = 'Reprovado'
        alunos.append(dados)

        resp = str(input('Deseja continuar? [s/n]: '))
        if resp not in 'SsNn':
            while resp not in 'SsNn':
                resp = str(input('Comando desconhecido. Por favor, digite novamente: '))
        if resp in 'Nn':
            break

    # Apresento os resultados
    print('-=' * 30)
    for i in range(len(alunos)):
        print('O(A) aluno(a) {} teve nota {}. Situação: {}'.format(alunos[i]['nome'], alunos[i]['nota'], alunos[i]['situacao']))


main()