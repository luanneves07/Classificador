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
#Incomming data
mistery1 = [1, 1, 1]
mistery2 = [1, 0, 0]
try_out = [mistery1, mistery2]
for item in model.predict(try_out):
    print("Porco" if item == 1 else "Cachorro")