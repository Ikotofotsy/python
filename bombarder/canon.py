from tkinter import * 
import math

class Canon(object) :
	"""
		Petit canon graphique
		Attributs:
			boss 		: référence du canevas
			x1 , y1 	: axe de rotation du canon
	"""

	def __init__(self, boss, id, x, y, sens, coul) :
		self.boss = boss 
		self.appli = boss.master
		self.id = id
		self.coul  = coul
		self.x1, self.y1 = x, y
		self.sens = sens
		self.xMax = int(boss.cget('width'))
		self.yMax = int(boss.cget('height'))
		self.v_intital = 15

		#dessiner la buse du canon a l'horizontal
		self.lbu = 30
		self.angle = 0
		self.x2, self.y2 = x + self.lbu*sens, y
		self.buse = boss.create_line(self.x1, self.y1, self.x2, self.y2, width = 10)

		#dessiner le corp du canon
		self.rayon = 15
		self.corps = boss.create_oval(x-self.rayon, y-self.rayon, x+self.rayon, y+self.rayon, fill=coul, width = 3)

		#dessiner un obus
		self.obus = boss.create_oval(-10, -10, -10, -10, fill = 'red')
		self.anim = False
		self.explo =False

		

	def orienter(self, angle) :
		#choisir l'angle de tir du canon

		self.angle = float(angle)*math.pi/180

		self.x2 = int(self.x1 + self.lbu*math.cos(self.angle) * self.sens)
		self.y2 = int(self.y1 - self.lbu*math.sin(self.angle))

		self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2)

	def deplacer(self, x, y) :
		dx, dy = x -self.x1, y -self.y1
		self.boss.move(self.buse, dx, dy)
		self.boss.move(self.corps, dx,dy)
		self.x1 += dx
		self.y1 += dy
		self.x2 += dx
		self.y2 += dy

	def vitesse_initial(self,v) :
		self.v_intital = 15

		
	def feu(self) :
		if not (self.anim or self.explo):
			self.anim = True

			self.guns = self.appli.dictionnaireCanons()

			self.boss.coords(self.obus, self.x2-3, self.y2-3, self.x2+3, self.y2+3) #position au depart


			self.vy = -self.v_intital*math.sin(self.angle)
			self.vx = self.v_intital*math.cos(self.angle) * self.sens
			self.animer_obus()
			return True
		else :
			return False

	def animer_obus(self) :
		if self.anim :
			self.boss.move(self.obus, int(self.vx), int(self.vy))
			c = tuple(self.boss.coords(self.obus))
			xo, yo = c[0] +3, c[1] +3
			self.test_obstacle(xo,yo)
			self.vy += .4
			self.boss.after(20, self.animer_obus)

	def test_obstacle(self, xo, yo) :
		if yo > self.yMax or xo < 0 or xo > self.xMax :
			self.anim = False
			return

		for id in self.guns :
			gun = self.guns[id]
			if xo < gun.x1 +self.rayon and xo > gun.x1 -self.rayon and yo < gun.y1 +self.rayon and yo > gun.y1 -self.rayon:
				self.anim = False
				self.explo = self.boss.create_oval(xo -12, yo -12, xo +12, yo+12, fill = 'yellow', width = 0)
				self.hit = id
				self.boss.after(150, self.fin_explosion)
				break
	def fin_explosion(self) :
		self.boss.delete(self.explo)
		self.explo = False
		self.appli.goal(self.id, self.hit)

	def fin_animation(self) :
		self.appli.disperser()
		self.boss.coords(self.obus, -10, -10, -10, -10)

if __name__ == '__main__' :
	f = Tk()
	can = Canvas(f, width = 250, height = 250, bg = 'ivory')
	can.pack(padx = 10, pady = 10)
	c1 = Canon(can,  "Za", 30, 200, 1, 'red')

	s1 = Scale(f, label = 'hausse', from_ = 90, to = 0, command = c1.orienter)
	s1.pack(side = LEFT, pady = 5, padx = 20)
	s1.set(25)

	s2 = Scale(f, label = 'puissance', from_ = 90, to = 0, command = c1.orienter)
	s2.pack(side = RIGHT, pady = 5, padx = 20)

	Button(f, text='Feu !', command = c1.feu(s2.get())).pack(side=LEFT)

	f.mainloop()
