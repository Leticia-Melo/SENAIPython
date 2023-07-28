# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
x = 0
for c in range(1,num+1):
    if num%c==0:
        x += 1
if x == 2:
    print('É um número primo')
else:
    print('Não é um número primo')