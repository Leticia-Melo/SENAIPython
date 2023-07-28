# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().upper()
x = frase.split()
frajun = ''.join(x)
inver = ''
for c in range(len(frajun)-1, -1, -1):
    inver += frajun[c]
if inver == frajun:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')