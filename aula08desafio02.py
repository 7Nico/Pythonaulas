#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
hyp = hypot(op, ad)
print(f'Sabendo que o cateto oposto é igual a {op} e o cateto adjacente é igual a {ad};\na hipotenusa do triângulo retângulo é igual a: {hyp}.')
