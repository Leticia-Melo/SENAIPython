# Crie um script Python que recebe três inteiros
# como entrada do teclado e escreva na tela a
# média, a soma e o produto entre eles, usando
# uma linha para cada resultado.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))
soma = num1 + num2 + num3
produto = num1 * num2 * num3
media = soma / 3

print('O resultado da média é: {}\nO produto da é: {}\nO resultado da soma é: {}'.format(media, produto, soma))