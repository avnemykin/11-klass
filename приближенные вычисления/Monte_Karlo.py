from random import *
from tkinter import *


mainwindow = Tk()
mainwindow.title("Решение методом Монте-Карло")
mainwindow.geometry("500x350")
canv = Canvas(mainwindow, width = 250, height = 250, bg = "white")             #Создание canvas
canv.place(x=10,y=10)


bt_calc = Button(mainwindow, width = 20, font="Arial 20", text = "Выполнить")  #Создание кнопки 
bt_calc.place(x=90,y=300)

lb_n = Label(mainwindow,text="N", font="Arial 20", bg = "white"); lb_n.place(x=270,y=20)               #Создание  контролов количество случайных точек
ent_n = Entry(mainwindow, bg = "white",font="Arial 20", width = 10); ent_n.place(x=320, y = 20)

lb_r = Label(mainwindow,text="R", font="Arial 20", bg = "white"); lb_r.place(x=270,y=80)              #Создание контролов радиуса
ent_r = Entry(mainwindow, bg = "white", font="Arial 20", width = 10); ent_r.place(x=320, y = 80)

lb_s = Label(mainwindow,text="S", font="Arial 20", bg = "white"); lb_s.place(x=270,y=140)              #Создание лайблов отображения площади окружности
otv_s = Label(mainwindow, bg = "white", font="Arial 20", width = 10); otv_s.place(x=320, y = 140)

lb_pi = Label(mainwindow,text="Пи", font="Arial 20", bg = "white"); lb_pi.place(x=270,y=200)             #Создание лайблов отображения числа pi
otv_pi = Label(mainwindow, bg = "white", font="Arial 20", width = 10); otv_pi.place(x=320, y = 200)

def fire(event):                               #Функция вычисления площади и pi
    
    canv.delete("all")                         #Очищаем canvas от прошлого графика                    
    
    R = int(ent_r.get())                        #Считывание исходных данных        
    N = int(ent_n.get())
    M = 0                                       #Количество попадание в окружность обнуляем
   
                            
    canv.create_rectangle(15, 15, R+15, R+15, outline="black", fill="white")     #Создание квадрата 
    canv.create_oval(15, 15, R+15, R+15,  outline="black", fill="white")         #Создание  окружности 
    
    
    for i in range(N):                        #Цикл генерации точек
                   x= randint(15,R+15)
                   y = randint(15,R+15)

                   
                   if (x-15)**2+(y-15)**2<=R**2:         #Проверяем попали в окружность
                       M +=1
                       
                   canv.create_oval(x, y, x+1, y+1, outline="black", fill="white") #Отображаем созданную точку
                
    otv_s["text"] = str(4*(R**2)*M/N)      #Подсчет площади окружности
    otv_pi["text"] = str(4*M/N)             #Подсчет pi
    

    
                   
bt_calc.bind("<Button-1>",fire)


mainwindow.mainloop()
