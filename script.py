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
	lp = ""
	for line in file: 
		line = line.rstrip()
		if line.startswith(">"): #première ligne avec nom d'espèce
			element = line.replace('[', ';').replace(']', ';').split(';') #on récupère le nom de l'espèce
			espece = element[1]
			dico[espece] = ""
			#print(dico) #on stock dans une liste les noms des espèce
			position = 1
		else:
			for l in line:
				lp=l+str(position)# Associe à l'AA sa position dans la séquence
				sequence += lp #Normalement doit faire une chaine de caractère avec AA + position
				position+=1 #incrémente position de +1
			dico[espece] = sequence
	print(dico)

	

	
