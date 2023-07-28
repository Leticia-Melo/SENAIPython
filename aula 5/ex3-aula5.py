# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

import math
angulo = int(input('Digite um ângulo: '))

rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O valor do seu ângulo em:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sen, cos, tan))