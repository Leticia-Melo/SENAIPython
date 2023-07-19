dist = int(input('Digite a distância de sua viagem: '))
curt = float(0.50)
long = float(0.45)

if dist<=200:
    pas = curt * dist
    print('O valor de passagem que você irá pagar é: R${}'.format(pas))
else:
    pas = long * dist
    print('O valor de passagem que você irá pagar é: R${}'.format(pas))