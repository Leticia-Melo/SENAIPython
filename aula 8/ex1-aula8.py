cas = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))

mes = anos * 12
pres = cas / mes

if pres > sal * 0.3:
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo foi aprovado, o valor será: R${}'.format(pres))
