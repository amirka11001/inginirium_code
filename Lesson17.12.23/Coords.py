def coords(x,y):
    if x>0 and y>0:
        print("I")
    elif x<0 and y>0:
        print("II")
    elif x<0 and y<0:
        print("III")
    elif x>0 and y<0:
        print("IV")

x=int(input('Введите X'))
y=int(input('Введите Y'))
coords(x,y)

