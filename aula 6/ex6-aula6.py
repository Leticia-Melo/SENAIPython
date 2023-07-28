# Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro
# e último nome separadamente.
# Ex.: Anna Maria Prado
# primeiro=Anna
# último=Prado

nome = input('Digite seu nome completo: ')
nome1 = nome.split()[0]
nome2 = nome.split()[-1]

print('O seu primeiro nome é: {}\nSeu último sobrenome é: {}'.format(nome1, nome2))