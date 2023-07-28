# Desenvolva um programa que leia o nome, a idade e
# o gênero de 4 pessoas. No final do programa, mostre:
# ▪ A média de idade do grupo
# ▪ Qual é o nome do homem mais velho
# ▪ Quantas mulheres têm menos de 20 anos

somaidade = 0
media = 0
maxhomem = 0
nomemax = 0
mulhermin20 = 0

for c in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo (M ou F) da {}ª pessoa: '.format(c))).strip().upper()
    print('-' * 20)
    somaidade += idade
    if c == 1 and sexo == 'M':
        maxhomem = idade
        nomemax = nome
    if sexo == 'M' and idade > maxhomem:
        maxhomem = idade
        nomemax = nome
    if sexo == 'F' and idade < 20:
        mulhermin20 += 1
media = somaidade / 4

print('A média de idade é {} anos.'.format(media))
print('{} é o homem mais velho e tem {} anos.'.format(nomemax, maxhomem))
print('Existem {} mulheres com menos de 20 anos.'.format(mulhermin20))