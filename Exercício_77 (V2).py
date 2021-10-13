def main():
    palavras = ('Rotacional', 'Divergente', 'Gradiente', 'Nabla', 'Eletrodinamica')
    for p in palavras:
        print(f'Na palavra {p.upper()} temos: ', end='')
        for letra in p:
            if letra.lower() in 'aeiou':
                print(letra.lower(), end=' ')
        # esse print vazio eh para corrigir o end da linha anterior e a visualizacao do programa nao ficar ruim
        print()


main()