#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#Nota: 1m é igual a 100cm e 1000mm

met = int(input('Qual o valor em metros?'))
cnt = met*100
mil = met*1000
print(f'{met}m é igual a {cnt}cm e {mil}mm')