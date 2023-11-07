from tkinter import * 
import menuBar
import panneau

class Ping(Frame) :
	def __init__(self) :
		Frame.__init__(self)
		self.master.geometry("400x300")
		self.master.title("Jeu de ping")

		self.mbar = menuBar.MenuBar(self)
		self.mbar.pack(side =TOP, expand =NO, fill =X)
		
		self.jeu = panneau.Panneau(self)
		self.jeu.pack(expand =YES, fill =BOTH, padx =8, pady =8)

		self.pack()

	def options(self) :
		opt = Toplevel(self)
		curL = Scale(opt, length =200, label ="Nombre de lignes :", orient =HORIZONTAL, from_ =1, to =12, command =self.majLignes)
		curL.set(self.jeu.nlig)
		curL.pack()

		curH = Scale(opt, length =200, label ="Nombre de colonnes :", orient =HORIZONTAL, from_ =1, to =12, command =self.majColonnes)
		curH.set(self.jeu.ncol)
		curH.pack()

	def majColonnes(self, n) :
		self.jeu.ncol = int(n)
		self.jeu.traceGrille()

	def majLignes(self, n) :
		self.jeu.nlig = int(n)
		self.jeu.traceGrille()

	def reset(self) :
		self.jeu.initJeu()
		self.jeu.traceGrille()

	def nextLevel(self,n) :
		self.majLignes(n)
		self.majColonnes(n)
		self.jeu.initJeu()
		self.jeu.traceGrille()

	def principe(self) :
		msg = Toplevel(self) 
		Message(msg, bg ='navy', fg ='ivory', width =400, font ='Helvetica 10 bold', text ="Les pions de ce jeu possèdent chacun une face blanche et une face noire. Lorsque l'on clique sur un pion, les 8 pions adjacents se retournent\nLe jeu consiste a essayer de les retouner tous.\n\nSi l'exercice se révèle très facile avec une grille de 2 x 2 cases. Il devient plus difficile avec des grilles plus grandes. Il est même tout à fait impossible avec certaines grilles.\nA vous de déterminer lesquelles !\n\nRéf : revue 'Pour la Science' - Aout 2002").pack(padx =10, pady	=10)

	def aPropos(self) :
		msg = Toplevel(self)
		Message(msg, width =200, aspect =100, justify =CENTER, text ="Jeu de Ping\n\n(C) Gérard Swinnen, Aout 2002.\nLicence = GPL").pack(padx =10, pady =10)

if __name__ == '__main__' :
	Ping().mainloop()