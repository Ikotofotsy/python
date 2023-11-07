from tkinter import * 
from random import randrange
import keyboard
import canon
import pupitre

class Application(Frame) :
	def __init__(self) :
		Frame.__init__(self)
		self.master.title('>>>>> Gain ! Gain ! Gain <<<<<<')
		self.pack()
		self.jeu = Canvas(self, width =400, height =250, bg ='ivory', bd =3, relief =SUNKEN)
		self.jeu.pack(padx =8, pady =8, side =TOP)

		self.guns ={}
		self.pupi ={}

		self.guns["Za"] = canon.Canon(self.jeu, "Za", 30, 200, 1, 'red')
		self.guns["Pema"] = canon.Canon(self.jeu, "Pema", 370, 200, -1, 'blue')

		self.pupi['Za'] = pupitre.Pupitre(self, self.guns['Za'])
		self.pupi['Pema'] = pupitre.Pupitre(self, self.guns['Pema'])





	def disperser(self) :
		for id in self.guns :
			gun = self.guns[id]

			if gun.sens == -1 :
				x = randrange(310,380)
			else :
				x =randrange(20,90)
			gun.deplacer(x, randrange(50, 250))

	def goal(self, i, j) :
		if i != j :
			self.pupi[i].attribuerPoint(1)
		else :
			self.pupi[i].attribuerPoint(-1)
		self.disperser()

	def dictionnaireCanons(self) :
		return self.guns

	


if __name__ == '__main__' :
	Application().mainloop()

