# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão
# aritmética. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da progressão: '))
print(num)
for c in range(0, 10):
    num = num+raz
    print(num)