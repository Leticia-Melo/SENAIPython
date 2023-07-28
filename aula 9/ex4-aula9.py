# Refaça o desafio 5 da aula 4, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando o laço for.

num = int(input('Digite um número: '))
print(f'Tabuada do {num}:')
for c in range(1, 11):
    valor = num * c
    print(f'{num} X {c} = {valor}')
