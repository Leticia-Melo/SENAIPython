# Crie um programa que leia um número real qualquer
#  pelo teclado e mostre na tela a sua porção inteira.
# Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

num = float(input('Digite um número real: '))
print(num)
num2 = int(num)
print('A porção inteira de seu número real é: {}'.format(num2))