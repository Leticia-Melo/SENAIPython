# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome 'Santo'.

cidade = input('Digite o nome da sua cidade: ')
print('Sua cidade começa com Santo:')
print(cidade[:5] == 'Santo')