# Faça um programa que leia algo pelo
# teclado, mostre na tela o seu tipo de
# dado e todas as informações possíveis
# sobre ele.

nome = input('Digite o seu nome completo: ')
peso = input('Digite o seu peso: ')
altura = input('Digite a sua altura: ')

print('O seu nome completo é {}, o seu peso é {} e a sua altura é {}, correto?'.format(nome, peso, altura))

print(type(nome))
print(type(peso))
print(type(altura))

print(nome .isalpha())
print(peso .isnumeric())
print(altura .isnumeric())