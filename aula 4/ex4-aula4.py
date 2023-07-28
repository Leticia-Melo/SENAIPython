# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite a metragem em metros: '))
cm = metros * 100
mm = metros * 1000

print('A sua metragem em centímetros é: {}\nE em milímetros é: {}'.format(cm, mm))