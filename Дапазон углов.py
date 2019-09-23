from math import *
from tkinter import *

root = Tk()
root.geometry("400x150")



def f_calc(event):
    s = ''
    v_0 = int(ent_speed.get())
    g = 9.8
    s = int(ent_s.get())
    h = int(ent_h.get())
    for a in range(1,90):
        if 0<=s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2) <=h:
            lb_grad["text"]+=str(a)+'  '



#Контроллы скорости мяча
lb_speed = Label(root); lb_speed["text"] = "V0"; ent_speed = Entry(root,width=5,bg = "white"); lb_speed_r = Label(root); lb_speed_r["text"] = "m/c";
lb_speed.place(x=15,y=5);lb_speed_r.place(x=85,y=5);ent_speed.place(x=35,y=5)

#Контроллы расстояния до стены
lb_s = Label(root); lb_s["text"] = "S"; ent_s = Entry(root,width=5,bg = "white"); lb_s_r = Label(root); lb_s_r["text"] = "м";
lb_s.place(x=15,y=35);lb_s_r.place(x=85,y=35);ent_s.place(x=35,y=35)

#Контроллы  высоты стены
lb_h = Label(root); lb_h["text"] = "H"; ent_h = Entry(root,width=5,bg = "white"); lb_h_r = Label(root); lb_h_r["text"] = "м";
lb_h.place(x=15,y=65);lb_h_r.place(x=85,y=65);ent_h.place(x=35,y=65)

# Лайблы о градусах
lb_n_grad = Label(root, text="A"); lb_n_grad.place(x=15,y=105);
lb_grad = Label(root,width=25,bg = "white"); lb_grad.place(x=35,y=105);
lb_grad_r = Label(root, text="град");  lb_grad_r.place(x=195,y=105);


bt_calc = Button(root,
                 text = "Диапзон углов",
                 width=30, height=2)
bt_calc.bind("<Button-1>", f_calc)
bt_calc.place(x=135,y=35)


root.mainloop()
