# Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos dólares
# ela pode comprar. Considere US$ 1,00 = R$4,78.

cart = float(input('Digite a quantidade de reais: R$'))
dolar = float(4.78)
cotacao = cart / dolar

print('Convertendo de reais para dólar: US${}'.format(cotacao))