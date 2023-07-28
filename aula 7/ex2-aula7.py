# Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input('Digite a velocidade que seu carro estava: '))
limi = 80

print('O limite da velocidade é 80 Km/h')

valor = float(7.00)
multa = valor * (velo-80)

if velo>limi:
    print('Você foi multado!')
    print('O valor de sua multa é de: R${}'.format(multa))
else:
    print('Você não foi multado, continue assim!')
