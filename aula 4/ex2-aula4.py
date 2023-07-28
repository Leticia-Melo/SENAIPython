# Crie um programa que leia um
# número real e mostre o seu dobro,
# triplo e a raiz quadrada.

num = float(input('Digite um número:'))
dob = num * 2
tri = num * 3
raiz = num ** 0.5

print('O dobro de {} é: {}\nO triplo é: {}\nE a raíz quadrada é: {}'.format(num, dob, tri, raiz))