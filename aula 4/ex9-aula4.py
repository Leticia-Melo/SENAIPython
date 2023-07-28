# Faça um script Python que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$'))
porc = 15 / 100
aumen = salario + (porc * salario)

print('O salário com o aumento ficará R${}'.format(aumen))