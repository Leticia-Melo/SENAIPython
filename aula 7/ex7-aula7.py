# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários
# superiores a R$1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o seu salário: R$'))

if sal > 1.250:
    valor = sal + (sal * 0.10)
    print('O seu salário será: R${}'.format(valor))
if sal <= 1.250:
    valor = sal + (sal * 0.15)
    print('O seu salário será: R${}'.format(valor))