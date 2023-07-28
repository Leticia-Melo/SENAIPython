# O prof.o Paza quer sortear um dos seus 4 alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random
alunos = 'Duda', 'Felipe', 'Kath', 'Mel'
aluno = random.choice(alunos)

print('Quem irá apagar o quadro será: {}'.format(aluno))