import tkinter

win=tkinter.Tk()

canvas=tkinter.Canvas(win, bg='#0ff',width=700,height=700)
canvas.create_oval((300,300),(500,500),fill='red')
canvas.create_line((0,0),(100,200),(300,300),(200,200),(0,0),fill='black')
canvas.pack()
win.mainloop()