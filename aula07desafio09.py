#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

s0 = float(input('Qual é o seu salário atual?R$'))
aum = (s0/100)*15
total = s0+aum
print(f'O seu novo salário com um aumento de 15% é de R${total}')