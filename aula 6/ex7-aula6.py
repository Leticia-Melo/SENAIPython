# Faça um programa em que troque todas as
# ocorrências de uma letra L1 pela letra L2
# em uma string. A string e as letras L1 e L2
# devem ser fornecidas pelo usuário.

frase = input('Digite uma frase: ')
a = input('Digite a letra a ser trocada: ')
b = input('Digite uma letra: ')
nova = frase.replace(a,b)

print('Sua frase fica: {}'.format(nova))