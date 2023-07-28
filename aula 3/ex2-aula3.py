# Crie um script Python que leia
# três números e converta todos para números reais.
# Imprima os três números e a soma
# entre eles em uma única mensagem.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

soma = num1 + num2 + num3

print('O resultado de {} + {} + {} é: {}'.format(num1, num2, num3, soma))