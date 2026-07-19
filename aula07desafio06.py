#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Nota: Cotação atual do dólar 18/07/2026 = 5,11 BRL

r = float(input('Quantos reais você tem na carteira?'))
d = r/ 5.11
print(f'Você pode comprar US${d:.2f}')
