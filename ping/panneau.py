from tkinter import *

class Panneau(Frame) :
	def __init__(self, boss =None) :
		Frame.__init__(self)
		self.nlig, self.ncol = 4, 4
		self.bind("<Configure>", self.redim)

		self.can = Canvas(self, bg ="dark olive green", borderwidth = 0, highlightthickness =1, highlightbackground ="white")

		self.can.bind("<Button-1>", self.clic)
		self.can.pack()
		self.initJeu()

	def initJeu(self) :
		self.etat =[]
		for i in range(12) :
			self.etat.append([0]*12)

	def redim(self, event) :
		self.width, self.height = event.width-4, event.height-4
		self.traceGrille()

	def traceGrille(self) :
		lmax = self.width/self.ncol
		hmax = self.height/self.nlig

		self.cote = min(lmax,hmax)

		larg, haut = self.cote*self.ncol, self.cote*self.nlig
		self.can.configure(width =larg, height =haut)

		self.can.delete(ALL)
		s = self.cote
		for l in range(self.nlig-1) :
			self.can.create_line(0, s, larg, s, fill ="white")
			s +=self.cote
		s =self.cote
		for c in range(self.ncol-1) :
			self.can.create_line(s, 0, s, haut, fill ="white")
			s += self.cote

		for l in range(self.nlig) :
			for c in range(self.ncol) :
				x1 = c*self.cote+5
				x2 = (c+1)*self.cote-5
				y1 = l*self.cote+5
				y2 = (l+1)*self.cote-5
				coul = ["white", "black"][self.etat[l][c]]
				self.can.create_oval(x1, y1, x2, y2, outline ="grey", width =1, fill =coul)
	def clic(self, event) :
		lig, col = int(event.y/self.cote), int(event.x/self.cote)

		for l in range(lig-1,lig+2) :
			if l < 0 or l >=self.nlig :
				continue
			for c in range(col-1, col+2) :
				if c <0 or c >=self.ncol :
					continue
				self.etat[l][c] = not(self.etat[l][c])
		self.traceGrille()