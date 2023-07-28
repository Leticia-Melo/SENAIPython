# O mesmo professor do desafio anterior quer sortear a
# ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
alunos = 'Duda', 'Felipe', 'Kath', 'Mel'
ordem = random.shuffle(alunos)

print('A ordem da apresentação será: {}\n'.format(ordem))