# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

import math
cateto1 = int(input('Digite a medida do cateto oposto: '))
cateto2 = int(input('Digite a medida do cateto adjacente: '))

soma = math.pow(cateto1, 2) + math.pow(cateto2, 2)
hipo = int(math.sqrt(soma))

print('O comprimento da hipotenusa é: {}'.format(hipo))