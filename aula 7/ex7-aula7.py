sal = float(input('Digite o seu salário: R$'))

if sal > 1.250:
    valor = sal + (sal * 0.10)
    print('O seu salário será: R${}'.format(valor))
if sal <= 1.250:
    valor = sal + (sal * 0.15)
    print('O seu salário será: R${}'.format(valor))