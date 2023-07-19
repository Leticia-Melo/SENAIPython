nota = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota + nota2) / 2

if media >= 6:
    print('APROVADO!')
else:
    print('REPROVADO!')

print('Sua média vale {}'.format(media))
