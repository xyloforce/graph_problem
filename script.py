#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Faire Blast à partir d'une séquence de protéine d'une espèce de façon à trouver des séquences 
#homologues de façon a récupérer d'autres séquences de cette protéines pour d'autres espèces. 

##Initialization and file opening  

with open('raw','r') as file:
	dico = {}
	sequence = ""
	for line in file: 
		line = line.rstrip()
		if line.startswith(">"): 
			#On traite la première ligne du bloc de l'espèce 
			element = line.replace('[', ';').replace(']', ';').split(';') #On récupère le nom de l'espèce
			espece = element[1]
			dico[espece] = "" #On la stock en clé de dico
			position = 1
			sequence = ""
			lp = ""

		else:
			#On traite le bloc de séquence
			for l in line:
				lp=l+str(position)# Associe à l'AA sa position dans la séquence
				sequence += lp 
				position+=1 #incrémente position de +1
			dico[espece] = sequence #Dico avec clé espèce et valeur associée
	print(dico)

	

	
