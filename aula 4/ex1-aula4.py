# Faça um programa que leia um
# número inteiro e mostre na tela
# o seu antecessor e o seu sucessor.

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('O antecessor do número {} é: {}\nE o sucessor é: {}'.format(num, ant, suc))