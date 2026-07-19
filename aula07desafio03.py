#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
# Nota: A média é a soma de números e a divisão do resultado dessa soma pela quantidade de números.


nome = input('Qual é o seu nome?')
nt1 = int(input(f'Qual foi a nota da sua primeira prova {nome}?'))
nt2 = int(input('Qual foi a nota de sua segunda prova?'))
média = (nt1+nt2)/2
print(f'A média de {nome} foi igual {média}')