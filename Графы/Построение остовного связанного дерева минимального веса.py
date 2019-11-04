from tkinter import*

from random import *

chis=Tk()
chis.title("Построение графа")
chis.geometry("550x580")

canv = Canvas(chis, width = 350, height = 300, bg = "white")             #Создание canvas
canv.place(x=15,y=264)

#Создание виджетов ввода количества вершин

lb_a=Label(chis, bg="white",  width=25,font="Arial,");lb_a["text"]="Количество вершин";lb_a.place(x=15, y=46) 
ent_nr=Entry(chis, width=5, bg="white",font="Arial"); ent_nr.place(x=300, y=46)
bt_ct=Button(chis, text="Создать таблицу",foreground="green",font="Arial"); bt_ct.place(x=370, y=46);

#Создание фрейма для отображения таблицы из Entry

frm = Frame(chis, bg="white"); frm.place(x=15, y=86);

#Функция создания таблицы

def creat_table(event):
    if 2<int(ent_nr.get()) <7:
        
        for i in range(1,int(ent_nr.get())+1):
            for j in range(1,int(ent_nr.get())+1):
                name = "ent"+str(i)+str(j)
            
                name = Entry(frm, width=5,bg="white")
                name.grid(row=i,column=j)
                
    else:
        
        ent_nr.delete(0, END)

        
 #Функция  отрисовки остовного дерева минимального веса

def creat_osd(event):   

    
    for i in range(1,int(ent_nr.get())+1):
        x = randint(10,340)
        y = randint(10,290)
        canv.create_oval(x, 300-y, x+1, 300-y,  outline="black", fill="white")
        canv.create_text(x, 300-y,  anchor="nw", text=str(i))

    for i in range(1,int(ent_nr.get())+1):
        for j in range(1,int(ent_nr.get())+1):
            name = "ent"+str(i)+str(j)
            if  int(name.get()) > 0:
                canv.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
            
        
bt_cg=Button(chis, text="Остнов. связан. дерево мин веса",foreground="green",font="Arial"); bt_cg.place(x=270, y=86);


bt_ct.bind("<Button-1>", creat_table)
bt_cg.bind("<Button-1>", creat_osd)




chis.mainloop()  
