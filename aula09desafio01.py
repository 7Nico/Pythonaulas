# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras ao todo (sem considerar os espaços).
# - Quantas letras tem o primeiro nome.


nome = str(input('Olá! Qual é o seu nome? '))
np = nome.upper()
nl = nome.lower()
ncs = nome.count(' ')
nla = len(nome)
nc = nla-ncs
ns = nome.split()
nlc = len(ns[0])
print(f'Apenas com letras maiúsculas:{np} \nApenas com letras minúsculas: {nl}')
print(f'Número de letras: {nc} \nNúmero de letras do primeiro nome: {nlc}')
