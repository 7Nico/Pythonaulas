#Um professor quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um progrma que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = random.sample([input('Digite o nome do aluno 1: '),
                    input('Digite o nome do aluno 2: '),
                    input('Digite o nome do aluno 3: '),
                    input('Digite o nome do aluno 4: '),], k= 4)
print(f'A ordem sorteada é seguinte: {a}')

#Sempre utiliza uma chave pras listas, ex: k= 4
#Se quiser utilizar listas com repetição, utilizar random.choices e sem repetição random.sample
