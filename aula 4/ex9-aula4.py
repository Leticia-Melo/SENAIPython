salario = float(input('Digite seu salário: R$'))

porc = 15 / 100
aumen = salario + (porc * salario)

print('O salário com o aumento ficará R${}'.format(aumen))