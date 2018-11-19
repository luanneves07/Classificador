#!/usr/bin/env python3
from sklearn.naive_bayes import MultinomialNB
""" 
 ##########################################################
# Base de dados contendo os elementos que serão utilizados #
# para treinar o algorítmo.                                #
 ##########################################################
"""
pig1 = [1, 1, 0]
pig2 = [1, 1, 0]
pig3 = [1, 1, 0]
dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]
#Array com todos os dados da base de dados
data = [pig1, pig2, pig3, dog1, dog2, dog3]
"""Cada índice representa a característica de um elemento do array
de dados. +1 -> pig; -1 -> dog."""
marking = [1, 1, 1, -1, -1, -1]
model = MultinomialNB()
model.fit(data, marking)

""" 
 ##########################################################
# Base de dados contendo os elementos que serão utilizados #
# para verificar o erro do sistema                         #
 ##########################################################
"""
mistery1 = [1, 1, 1]
mistery2 = [1, 0, 0]
mistery3 = [0, 0, 1]
#Array com todos os dados da base de verificação
try_out = [mistery1, mistery2, mistery3]
marking_test = [-1, 1, -1]
result = model.predict(try_out)

print("Predicted\t\t\tCorrect", end="\n\n")
for index in range(len(try_out)):
    print("Porco\t" if result[index] == 1 else "Cachorro", end="")
    print("\t\t\t", end="")
    print("Porco" if marking_test[index] == 1 else "Cachorro")

print("", end="\n\n")
#Verifica a diferença para calcular o erro (Resultado obtido
# menos a marcação de teste feita na mão) -> Caso 0 acertou
# Caso diferente de 0 errou
diff = result - marking_test
correct = [d for d in diff if d==0]
total_correct = len(correct)
total_elements = len(try_out)
rate_percentage = 100.0 * total_correct/total_elements
print("Porcentagem de acertos: " + str(rate_percentage))