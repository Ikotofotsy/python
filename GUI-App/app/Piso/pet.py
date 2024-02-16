from tkinter import NORMAL, HIDDEN
class face :
    
    def __init__(self, canvas) :
        self.canvas = canvas
        self.body_color = 'thistle1'
        self.eyes_crossed = False
        self.tongue_out = False
        self.happy_level = 1
        self.createBody()
        self.createEar()
        self.createFoot()
        self.createEye()
        self.createMouthHappy()
        self.createMouthSad()
        self.createMouthNormal()
        self.createCheek()
        self.makeVeryWell()

    def createBody(self) :
        self.canvas.create_oval(35, 20, 365, 350, outline = self.body_color, fill = self.body_color)
    
    def createEar(self) :
        self.canvas.create_polygon(75, 80, 75, 10, 165, 70, outline = self.body_color, fill = self.body_color)
        self.canvas.create_polygon(255, 45, 325, 10, 320, 70, outline = self.body_color, fill = self.body_color)
    
    def createFoot(self) :
        self.canvas.create_oval(65, 320, 145, 360, outline = self.body_color, fill = self.body_color)
        self.canvas.create_oval(250, 320, 330, 360, outline = self.body_color, fill = self.body_color)

    def createEye(self) :
        self.eye_left = self.canvas.create_oval(130, 110, 160, 170, outline = 'black', fill = 'white')
        self.pupil_left = self.canvas.create_oval(140, 145, 150, 155, outline = 'black', fill = 'black')
        self.eye_right = self.canvas.create_oval(230, 110, 260, 170, outline = 'black', fill = 'white')
        self.pupil_right = self.canvas.create_oval(240, 145, 250, 155, outline = 'black', fill = 'black')
    
    def createMouthHappy(self) :
        self.mouth_happy = self.canvas.create_line(170, 250, 200, 280, 230, 250, smooth = 1, width = 2, state = HIDDEN)
    
    def createMouthSad(self) :
        self.mouth_sad = self.canvas.create_line(170, 250, 200, 232, 230, 250, smooth = 1, width = 2, state = HIDDEN)
    
    def createMouthNormal(self) :
        self.mouth_normal = self.canvas.create_line(170, 250, 200, 272, 230, 250, smooth = 1, width = 2, state = NORMAL)

    def makeVeryWell(self) :
        self.tongue_main = self.canvas.create_rectangle(170,250,230,290, outline = 'red', fill = 'red', state = HIDDEN)
        self.tongue_tip = self.canvas.create_oval(170,285,230,300, outline = 'red', fill = 'red', state = HIDDEN)

    def createCheek(self) :
        self.cheek_left = self.canvas.create_oval(70, 180, 120, 230, outline = 'pink', fill = 'pink', state = HIDDEN)
        self.cheek_right = self.canvas.create_oval(280, 180, 330, 230, outline = 'pink', fill = 'pink', state = HIDDEN)

    def toggleEyes(self) :
        current_color = self.canvas.itemcget(self.eye_left, 'fill')
        new_color = self.body_color if current_color == 'white' else 'white'
        current_state = self.canvas.itemcget(self.pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN

        self.canvas.itemconfigure(self.pupil_left , state = new_state) 
        self.canvas.itemconfigure(self.pupil_right , state = new_state)
        self.canvas.itemconfigure(self.eye_right , fill = new_color)
        self.canvas.itemconfigure(self.eye_left , fill = new_color)
    
    def showHappy(self, event) :
        if (20 <= event.x <= 350) and (20 <= event.y <= 350) :
            self.canvas.itemconfigure(self.cheek_left, state = NORMAL)
            self.canvas.itemconfigure(self.cheek_right, state = NORMAL)
            self.canvas.itemconfigure(self.mouth_happy, state = NORMAL)
            self.canvas.itemconfigure(self.mouth_normal, state = HIDDEN)
            self.canvas.itemconfigure(self.mouth_sad, state = HIDDEN)
            self.happy_level = 1
    
    def hideHappy(self, event) :
        self.canvas.itemconfigure(self.cheek_left, state = HIDDEN)
        self.canvas.itemconfigure(self.cheek_right, state = HIDDEN)
        self.canvas.itemconfigure(self.mouth_happy, state = HIDDEN)
        self.canvas.itemconfigure(self.mouth_normal, state = NORMAL)
        self.canvas.itemconfigure(self.mouth_sad, state = HIDDEN)

    def toogle_tongue(self) :
        if not self.tongue_out :
            self.canvas.itemconfigure(self.tongue_tip, state = NORMAL)
            self.canvas.itemconfigure(self.tongue_main, state = NORMAL)
            self.tongue_out = True
        else :
            self.canvas.itemconfigure(self.tongue_tip, state = HIDDEN)
            self.canvas.itemconfigure(self.tongue_main, state = HIDDEN)
            self.tongue_out = False
    
    def toogle_pupils(self) :
        if not self.eyes_crossed :
            self.canvas.move(self.pupil_left, 10, -5)
            self.canvas.move(self.pupil_right, -10, -5)
            self.eyes_crossed = True
        else :
            self.canvas.move(self.pupil_left, -10, 5)
            self.canvas.move(self.pupil_right, 10, 5)
            self.eyes_crossed = False

    
