"""
	Un programme simulant un combat qui respect les contraites suivantes :
		- Deux jouers, auxquels on demande de choisir un pseudo
		- Les deux combantant demarrent avec 2500 points de vie chacun
		- Chaque attaque est une tentative (si elle reusssitm le joueur infligera un nombre de degat entre 0 et 100 - si elle echoue, l'attaque est ratee , et c'est au tour de l'autre joueur)
		- A la fin du combat (un joueur KO), en declare le gagnant ,celui qui il reste le plus de points de vie
"""


import joueur
import function



j1 = joueur.Joueur(function.choisir_pseudo())
j2 = joueur.Joueur(function.choisir_pseudo())

print("\n\tLe combat commence !\n=================================================\n")

while function.and_game(j1,j2) == False:
	j1.attaquer(j2)
	input()
	j2.attaquer(j1)


print("=================================================\n\tFin du combat !\n")
function.vainqueure(j1,j2)




