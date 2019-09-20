from math import *
from tkinter import *

v_0=40
a = 30
s = 60
H = 2
g = 9.8

root = Tk()
root.geometry("500x500")

canv_h = 300
canv_w = 450

canv = Canvas(root, width = canv_w+10, height = canv_h+10, bg = "white")             #Создадим холст

canv.create_line(10,canv_h,canv_w,canv_h,width=2, fill='green',arrow=LAST)   # Добавим ось X

canv.create_line(10,canv_h,10,10,width=2, fill='green',arrow=LAST)          # Добавим ось Y

# Вычислим шаг
k_x= (canv_w)//s
k_y =(canv_h)//s
#Добавим надписи к оси X
for i in range(0,canv_w-5,k_x*5):
    canv.create_text(i+10, canv_h, text = str(round(s*((i)/canv_w))), fill="purple", font=("Helvectica", "10"))
    
#Добавим надписи к оси Y 
for i in range(s//5*k_y,canv_h,s//5*k_y):
    canv.create_text(10, canv_h-(i), text = str(round(s*((i)/canv_h))), fill="purple", font=("Helvectica", "10"))

canv.create_line(k_x*s,canv_h,k_x*s,canv_h,width=2, fill='red')

for i in range(0,100,1):
    #y = s*tan(radians(a)) - (g*(s**2)/2)*v_0**2*cos(radians(a))**2)
    y = (v_0*sin(radians(a))*(i/10)-g*((i/10)**2)/2); 
    x = v_0*cos(radians(a))*(i/10); 
    canv.create_oval( (x*k_x//5),(canv_h-y*k_y), (x*k_x + 1)//5, (canv_h-y*k_y + 1), fill = 'black')
def f_calc():
    a = int(ent_grad.get())
    v_0 = int(ent_speed.get())
    g = 9.8
    s = int(ent_s.get())
    h = int(ent_h.get())
    
    y = s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2)
    if y>0 and h>=y:
        lb_res["text"] = 'Попадение'
    elif y<0:
        lb_res["text"] = 'Недолет'
    else:
        lb_res["text"] = 'Перелет'


        
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
lb_res= Label(root,
              bg = "white",
              width=25);
lb_res.place(x=185,y=35);

bt_calc = Button(root,
                 text = "Вычислить",
                 width=20)
bt_calc.bind("<Button-1>", f_calc())

bt_calc.place(x=135,
              y=65)

bt_view = Button(root,
                 text = "Показать",
                 width=20)

bt_view.place(x=295,
              y=65)



	 
canv.place(x=(500-canv_w)/2,y=(500-canv_h-10))

root.mainloop()
