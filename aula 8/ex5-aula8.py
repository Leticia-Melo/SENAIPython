# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos:INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é Mirim')
elif 10 <= idade <= 14:
    print('Sua categoria é Infantil')
elif 15 <= idade <= 19:
    print('Sua categoria é Júnior')
elif idade==20:
    print('Sua categoria é Sênior')
else:
    print('Sua categoria é Master')
