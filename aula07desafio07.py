#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta nescessária para pintá-la.
#Nota: A área é igual a altura x largura. Cada litro de tinta pinta uma área de 2m².

a = float(input('Qual é a altura da sua parede?'))
l = float(input('Qual é a largura da sua parede?'))
area = a*l
tin = area/2
print(f'A área de sua parede é igual a {area}m² e a quantidade de tinta nescessária é de {tin}L')