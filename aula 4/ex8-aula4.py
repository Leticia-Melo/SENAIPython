produto = float(input('Digite o preço do produto: R$'))

desc = 5 / 100
valor_final = produto - (desc * produto)

print('O valor do produto com o desconto fica R${}'.format(valor_final))