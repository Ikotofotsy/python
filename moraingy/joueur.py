import random 

class Joueur :
	random_attack = False
	random_damage = 0

	def __init__(self,pseudo) :
		self.pseudo = pseudo
		self.vie = 180

	def getVie(self) :
		return self.vie

	def getPseudo(self) :
		return self.pseudo

	def attaquer(self, adversaire) :
		print(f"\n________________________\n{self.pseudo} attaque \n")
		random_attack = bool(random.randint(0,1))
		if(random_attack == True) :
			random_damage = random.randint(0,100)
			print(f"Damage : {random_damage}\n")
			adversaire.vie -= random_damage
			if adversaire.vie <= 0 :
				adversaire.vie = 0
			print(f"Points de vie :\n\t{self.pseudo} : {self.vie}\n\t{adversaire.pseudo} : {adversaire.vie} \n")
		else :
			print("Attaque rattee ! \n")
			print(f"Points de vie :\n\t{self.pseudo} : {self.vie}\n\t{adversaire.pseudo} : {adversaire.vie} \n")
