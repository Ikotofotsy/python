from tkinter import Tk, Canvas, Toplevel, Button, Entry, Label
from datetime import date, datetime
import events


TODAY = date.today()
ROOT = Tk()

def start() :

    btn_add_event = Button(ROOT, text='Add Event', command=form_add)
    btn_add_event.pack()

    canvas = Canvas(ROOT, width = 800, height = 800, bg = 'black')
    canvas.pack()


    set_title(canvas, 'My Countdown Calendar')
    listing_events(canvas)
    
    ROOT.mainloop()

def listing_events(canvas) :
    evts = events.get_events()
    vertical_space = 100
    for evt in evts :
        event_name = evt[1]
        event_date = datetime.strptime(evt[2], '%d/%m/%Y %H:%M').date()
        days_until = events.day_between_dates(event_date, TODAY)
        display = 'It is %s days until %s' % (days_until, event_name)
        canvas.create_text(100, vertical_space, anchor='w' , fill = 'lightblue', font = 'Arial 28 bold', text = display )
        vertical_space+=30
    
def set_title(canvas, title) :
    canvas.create_text(100, 50, anchor = 'w', fill = 'orange', font = 'Arial 28 bold underline', text = title)

def form_add() :
    form = Toplevel(ROOT)
    
    Label(form, text='Event',width=25).pack()
    input_event = Entry(form)
    input_event.pack()

    Label(form, text='Date',width=25).pack()
    input_date = Entry(form)
    input_date.pack()

    Button(form, text='Confirm', command = lambda:add_event(input_event.get(), input_date.get())).pack()

    print('btn clicked !')

def add_event(event, date) :
    events.add_event(event, date)
if __name__ == '__main__' :
    start()