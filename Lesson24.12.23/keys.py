import tkinter

def move_by_keys(event):
    qq=canvas.coords(oval)
    x=qq[0]
    y=qq[1]
    label.config(text=str(x)+''+str(y))
    if event.keysym=='Up':
        canvas.move(oval,0,-20)
    elif event.keysym == 'Down':
        canvas.move(oval, 0,20)
    elif event.keysym == 'Left':
        canvas.move(oval,-20,0)
    elif event.keysym == 'Right':
        canvas.move(oval,20, 0)

win=tkinter.Tk()
label=tkinter.Label(win,text='INGINIRIUM')
label.pack()
canvas=tkinter.Canvas(win, bg='red',width=700,height=700)
oval=canvas.create_oval((300,300),(400,400),fill='white')
canvas.pack()
win.bind('<KeyPress>', move_by_keys)
win.mainloop()((0,0),(100,200),(300,300),(200,200),(0,0),fill='black')