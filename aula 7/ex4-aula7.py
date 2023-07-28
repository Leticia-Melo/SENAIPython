# Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até
#  200Km e R$0,45 para viagens mais longas.

dist = int(input('Digite a distância de sua viagem: '))
curt = float(0.50)
long = float(0.45)

if dist<=200:
    pas = curt * dist
    print('O valor de passagem que você irá pagar é: R${}'.format(pas))
else:
    pas = long * dist
    print('O valor de passagem que você irá pagar é: R${}'.format(pas))