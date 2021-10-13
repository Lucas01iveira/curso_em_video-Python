#Detector de Palíndromo
frase = str(input('Digite uma frase: '))
frase = frase.strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Voce digitou a frase: {}'.format(junto))

# 1 maneira de construir o inverso
'''inverso = ''
for i in range(len(junto)-1,-1,-1):
    inverso += junto[i]'''

#segunda maneira de construir o inverso (por fatiamento de str)
inverso = junto[::-1]

print('A frase, reescrita ao contrário, fica da seguinte forma: {}'.format(inverso))
if junto == inverso:
    print('A frase digitada é palíndrome')
else:
    print('A frase digitada não é palíndrome')