#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, cos, sin, tan

r = float(input('Digite um ângulo qualquer: '))
d = radians(r)
cos = cos(d)
sen = sin(d)
tan = tan(d)
print(f'O cosseno de {r} = {cos:.2f} \nO seno de {r} = {sen:.2f} \nA tangente de {r} = {tan:.2f}')