# Desenvolva um programa que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seus status, de acordo com a tabela abaixo:
# Abaixo de 18.5: ABAIXO DO PESO
# Entre 18.5 e 25: PESO IDEAL
# 25 até 30: SOBREPESO
# 30 até 40: OBESIDADE
# Acima de 40: OBESIDADE MÓRBIDA

peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso, seu IMC é de: {:.2f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('Peso ideal, seu IMC é de: {:.2f}'.format(imc))
elif 25.1 <= imc <= 30:
    print('Sobrepeso, seu IMC é de: {:.2f}'.format(imc))
elif 30.1 <= imc <= 40:
    print('Obesidade, seu IMC é de: {:.2f}'.format(imc))
else:
    print('Obesidade mórbida, seu IMC é de: {:.2f}'.format(imc))