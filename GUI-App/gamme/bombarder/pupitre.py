from tkinter import * 
import math
import canon

class Pupitre(Frame) :
	def __init__(self,boss,canon) :
		Frame.__init__(self, bd = 3, relief = GROOVE)
		self.score = 0
		self.appli = boss
		self.canon =  canon

		self.regl = Scale(self, from_ =90, to =-90, troughcolor =canon.coul, command =self.orienter )
		self.regl.set(45)
		self.regl.pack(side =LEFT)

		self.vitesse = Scale(self, from_ =15, to =0, troughcolor =canon.coul, command =canon.vitesse_initial)
		self.vitesse.pack(side =RIGHT)

		Label(self, text =canon.id).pack(side =TOP, anchor =W, pady =5)

		self.bTir = Button(self,text ='Feu !', command =self.tirer)
		self.bTir.pack(side =BOTTOM, padx =5, pady =5)
		Label(self, text ='points').pack()
		self.points = Label(self, text ='0', bg ='white')
		self.points.pack()

		if canon.sens == -1 :
			self.pack(padx =5, pady =5, side =RIGHT)
		else :
			self.pack(padx =5, pady =5, side =LEFT)

	def tirer(self) :
		self.canon.feu()

	def orienter(self, angle) :
		self.canon.orienter(angle)

	def attribuerPoint(self, p) :
		self.score +=p
		self.points.config(text ='%s'%self.score)