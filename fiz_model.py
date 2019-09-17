from math import *
from tkinter import *

v_0=18
a = 35
s = 30
H = 2
g = 9.8

root = Tk()

canv = Canvas(root, width = 500, height = 500, bg = "white")             #Создадим холст

canv.create_line(10,490,490,490,width=2, fill='green',arrow=LAST)   # Добавим ось X

canv.create_line(10,490,10,5,width=2, fill='green',arrow=LAST)          # Добавим ось Y

# Вычислим шаг
k = 490//s

#Добавим надписи к оси X
canv.create_text(10, 495, text = str(0), fill="purple", font=("Helvectica", "10"))

for i in range(k*5,500,k*5):
    canv.create_text(i, 495, text = str(round(s*((i)/490))), fill="purple", font=("Helvectica", "10"))
    
#Добавим надписи к оси Y 
for i in range(round(k*6*i/490), 500, k*6):
    canv.create_text(20, 490-(i+10), text = str(round(s*((i)/490))), fill="purple", font=("Helvectica", "10"))

canv.create_line(k*s,490,k*s,450,width=2, fill='red')

for i in range(0,490,k*3):
    y = s*tan(radians(a)) - (g*(s**2/2)*v_0**2*cos(radians(a))**2)
   #y = (v_0*sin(radians(a))*i-(g*i**2)/2)*100
    #x = v_0*cos(radians(a))*i*100
   # canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
    

canv.pack()	
root.mainloop()
