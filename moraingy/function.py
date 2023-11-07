def choisir_pseudo() :
	return input("\nChoisir un pseudo\n")

def vainqueure(j1,j2) :
	print(f"Points de vie final\n\t{j1.getPseudo()} : {j1.getVie()}\n\t{j2.getPseudo()} : {j2.getVie()} \n")
	if(j1.getVie()>j2.getVie()) :
		print(f"{j1.getPseudo()} gagne !")
	elif(j1.getVie()<j2.getVie()) :
		print(f"{j2.getPseudo()} gagne !")
	elif(j1.getVie()==j2.getVie()) :
		print("Combat null !")

def and_game(j1,j2) :
	if(j1.getVie() <= 0 or j2.getVie() <= 0) :
		return True
	else :
		return False
if __name__ == "__main__" :
	choisir_pseudo()
	
	