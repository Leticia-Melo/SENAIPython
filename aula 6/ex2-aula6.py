# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
uni = n[3]
deze = n[2]
cente = n[1]
mil = n[0]

print('Digite um número: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num, uni, deze, cente, mil))