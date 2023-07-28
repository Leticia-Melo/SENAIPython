# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ele não pode
# exceder 30% do salário ou o empréstimo será negado.

cas = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))

mes = anos * 12
pres = cas / mes

if pres > sal * 0.3:
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo foi aprovado, o valor será: R${}'.format(pres))
