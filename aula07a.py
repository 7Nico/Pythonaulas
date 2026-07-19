# ANOTAÇÕES

# Operadores aritméticos:

# Operadores (números que vem primeiro) e Operandos (números que vem em seguida)

# Ordem de precedência:
# 1- ()
# 2- **
# 3- *, /, //, %
# 4 - +, -

# Raiz quadrada de um número é a mesma coisa dele sobre a potência de 1/2
# Ex: 25**(1/2) = 5
# Raiz cúbica é 1/3
# Ex: 8**(1/3) = 2
print(8*(1/3))

# É possível fazer "multiplicações" com letras
# Ex: Se você colocar print('='*50), ele resultará em = 50x
print('='*50)

# Também é possível brincar com as formatações do print. Ex:
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome:20}!')
# Dessa forma o nome tem 20 espaços após ele. Outro ex para alinhado a direita:
nome = input('Qual o seu nome?')
print(f'Prazer em te conhecer {nome:>20}!')
# Ou a esquerda:
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome:<20}!')
# Ou centralizado:
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome:^20}!')
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome:!<20}')