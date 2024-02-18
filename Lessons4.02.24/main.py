class Car:
    def __init__(self,color,mark,max_speed,weight):
        self.color=color
        self.mark=mark
        self.max_speed=max_speed
        self.weight=weight

    def sound(self):
        print("beep")

    def long_sound(self):
        print('beep-beep')

Lada=Car('оранжевый','ламба',999,1)
Lada.sound()
Lada.long_sound()

print(Lada.color)
print(Lada.mark)
print(Lada.max_speed)
print(Lada.weight)
