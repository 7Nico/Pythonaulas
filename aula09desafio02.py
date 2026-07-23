# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = input('Digite um numero de 0 a 9999: ')
s =  '000' + n
print(f'unidade: {s[-1]}')
