#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Faire Blast à partir d'une séquence de protéine d'une espèce de façon à trouver des séquences 
#homologues de façon a récupérer d'autres séquences de cette protéines pour d'autres espèces. 

##Initialization and file opening  
dico = {}
with open('raw','r') as file:
	position = 1 #initialiser la position
	sequences = [] 
	specie = []
	sequence = ""
	for line in file: 
		if line.startswith(">"): #première ligne avec nom d'espèce
			element = line.replace('[', ';').replace(']', ';').split(';') #on récupère le nom de l'espèce
			print(element[1])
			specie.append(element[1]) #on stock dans une liste les noms des espèces
		else:
			while line[0]!=">": #pour les lignes de séquence
				for l in line:
					print(line)
					#lp=l+str(position)# Associe à l'AA sa position dans la séquence
					#print(lp)
					#sequence += lp #Normalement doit faire une chaine de caractère avec AA + position
					#print(sequence)
					#position+=1 #incrémente position de +1
			#sequences.append(lp)
			#position = 1	
			#print(sequence)
	print(specie)