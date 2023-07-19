from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

if ano > date.today().year:
    print('Não faz sentido, mas aí está sua resposta:')
if idade == 18:
    print('É hora de se alistar')
if idade > 18:
    print('Já passou da hora de se alistar')
    passou = idade - 18
    print('Passou {} anos do prazo'.format(passou))
if idade < 18:
    print('Ainda irá se alistar')
    falta = 18 - idade
    print('Ainda faltam {} anos'.format(falta))