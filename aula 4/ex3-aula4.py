# Crie um script Python que leia cinco notas de
# um aluno, calcule e mostre sua média final.

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))
nota5 = float(input('Digite sua nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print('A media de suas notas é: {}'.format(media))