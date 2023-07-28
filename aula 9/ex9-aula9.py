# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
data = date.today().year
max = 0
min = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ªpessoa: '.format(c)))
    idade = data - nasc
    if idade >= 18:
        max += 1
    else:
        min += 1

print('Existem {} maiores de idade.'.format(max))
print('Existem {} menores de idade.'.format(min))