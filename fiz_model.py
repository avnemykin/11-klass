from math import *
from tkinter import *

v_0=18
a = 35
s = 30
H = 2
g = 9.8

root = Tk()
root.geometry("500x500+100+100")

canv_h = 300
canv_w = 450

canv = Canvas(root, width = canv_w+10, height = canv_h+10, bg = "white")             #Создадим холст

canv.create_line(10,canv_h,canv_w,canv_h,width=2, fill='green',arrow=LAST)   # Добавим ось X

canv.create_line(10,canv_h,10,10,width=2, fill='green',arrow=LAST)          # Добавим ось Y

# Вычислим шаг
k_x= (canv_w)//s
k_y =(canv_h)//s
#Добавим надписи к оси X
for i in range(0,canv_w,k_x*6):
    canv.create_text(i+10, canv_w, text = str(round(s*((i)/canv_w))), fill="purple", font=("Helvectica", "10"))
    
#Добавим надписи к оси Y 
for i in range(round(k_y*6*i/canv_h), canv_h, k_y*6):
    canv.create_text(10, canv_h-(i+10), text = str(round(s*((i)/canv_h))), fill="purple", font=("Helvectica", "10"))

canv.create_line(k_x*s,canv_h,k_x*s,canv_h,width=2, fill='red')

for i in range(0,canv_h,k_x*3):
    #y = s*tan(radians(a)) - (g*(s**2/2)*v_0**2*cos(radians(a))**2)
    y = (v_0*sin(radians(a))*i-(g*i**2)/2)*100
    x = v_0*cos(radians(a))*i*100
    canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
    
lb_speed = Label(root); lb_speed["text"] = "V0"; ent_speed = Entry(root,width=5,bg = "white"); lb_speed_r = Label(root); lb_speed_r["text"] = "m/c";
lb_speed.place(x=15,y=5);lb_speed_r.place(x=85,y=5);ent_speed.place(x=35,y=5)

lb_grad = Label(root); lb_grad["text"] = "A"; ent_grad = Entry(root,width=5,bg = "white"); lb_grad_r = Label(root); lb_grad_r["text"] = "град";
lb_grad.place(x=15,y=35);lb_grad_r.place(x=85,y=35);ent_grad.place(x=35,y=35)

lb_s = Label(root); lb_s["text"] = "S"; ent_s = Entry(root,width=5,bg = "white"); lb_s_r = Label(root); lb_s_r["text"] = "м";
lb_s.place(x=15,y=65);lb_s_r.place(x=85,y=65);ent_s.place(x=35,y=65)

lb_h = Label(root); lb_h["text"] = "H"; ent_h = Entry(root,width=5,bg = "white"); lb_h_r = Label(root); lb_h_r["text"] = "м";
lb_h.place(x=15,y=95);lb_h_r.place(x=85,y=95);ent_h.place(x=35,y=95)

lb_l = Label(root,bg = "white",width=5); lb_l["text"] = "L"; lb_l_res= Label(root,bg = "white",width=25); lb_l_r = Label(root,bg = "white",width=5); lb_l_r["text"] = "м";
lb_l.place(x=125,y=5);lb_l_r.place(x=385,y=5);lb_l_res.place(x=185,y=5);
lb_res= Label(root,bg = "white",width=25);lb_res.place(x=185,y=35);


	 
canv.place(x=(500-canv_w)/2,y=(500-canv_h-10))

root.mainloop()
