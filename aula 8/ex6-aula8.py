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