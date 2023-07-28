# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
maius = frase.count('A')
minus = frase.count('a')
pos1 = frase.find('A')
pos2 = frase.find('a')
pos3 = frase.rfind('A')
pos4 = frase.rfind('a')

print('A letra a maiúsculo aparece: {} vezes'.format(maius))
print('A letra a minúsculo aparece: {} vezes'.format(minus))
print('A primeira vez que a maiúsculo aparece é na posição: {}'.format(pos1))
print('A primeira vez que a minúsculo aparece é na posição: {}'.format(pos2))
print('A última vez que a maiúsculo aparece é na posição: {}'.format(pos3))
print('A última vez que a minúsculo aparece é na posição: {}'.format(pos4))