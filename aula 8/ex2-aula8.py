# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem entre as seguintes opções:
# ▪ O primeiro valor é maior
# ▪ O segundo valor é maior
# ▪ Não existe valor maior, os dois valores são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é o maior')
if num2 > num1:
    print('O segundo número é o maior')
if num1==num2:
    print('Não existe valor maior, os dois números são iguais')