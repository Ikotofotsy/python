from tkinter import *

class MenuBar(Frame) :

	def __init__(self,boss =None) :
		Frame.__init__(self, borderwidth =2, relief =GROOVE)
		
		fileMenu = Menubutton(self, text ='Fichier')
		fileMenu.pack(side =LEFT, padx =5)
		me1 = Menu(fileMenu)
		me1.add_command(label ='Options', underline =0, 
			command =boss.options)
		me1.add_command(label ='Restart', underline =0, command =boss.reset)
		me1.add_command(label ='Terminer', underline =0, command =boss.quit)
		fileMenu.configure(menu =me1)

		helpMenu = Menubutton(self, text ='Aide')
		helpMenu.pack(side =LEFT, padx =5)
		me1 = Menu(helpMenu)
		me1.add_command(label ='Principe du jeu', underline =0, command =boss.principe)
		me1.add_command(label ='A propos ...', underline =0, command =boss.aPropos)
		helpMenu.configure(menu = me1)
