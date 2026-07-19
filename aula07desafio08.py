#Faça um algoritmo que leia o preço de um produto e mostre o eu novo preço, com 5% de desconto.
#Nota: Para calcular a porcentagem de um número devemos dividi-lo por 100 e depois multiplicar o resultado pela porcentagem desejada.

preço = float(input('Qual é o valor do produto? R$'))
desconto = (preço/100)*5
total = preço - desconto
print(f'Valor total do produto com 5% de desconto é de R${total:.2f}' )

