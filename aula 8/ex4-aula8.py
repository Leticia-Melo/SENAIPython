num1 = float(input('Digite uma nota: '))
num2 = float(input('Digite uma nota: '))

media = (num1 + num2) / 2

if media < 5.0:
    print('Reprovado')
elif 5.0 <= media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')