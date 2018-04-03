from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import back



def get_selecte_row(event):
    try:

        for val in tree.selection():
            Item = tree.item(val, 'values')

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)

            e1.insert(END, Item[5])
            e2.insert(END,Item[6])
            e3.insert(END,Item[7])

            C1.set(Item[0])
            c2.set(Item[1])
            c3.set(Item[2])
            c4.set(Item[3])
            c5.set(Item[4])


    except IndexError:
        pass





def view_command():
    tree.delete(*tree.get_children())

    for row in back.view():
        tree.insert('',END,text= row[0] ,values= (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))


def insert_command():
    tree.delete(*tree.get_children())
    back.insert(school_text.get(),date_text.get(),Month_text.get(),year_text.get(),day_text.get(),session_text.get(),Present_text.get(),Total_text.get())
    for row in back.view():
        tree.insert('',END,text= row[0] ,values= (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

def search_command():
    tree.delete(*tree.get_children())
    for row in back.search(school_text.get(),date_text.get(),Month_text.get(),year_text.get(),day_text.get(),session_text.get(),Present_text.get(),Total_text.get()):
        tree.insert('',END,text= row[0] ,values= (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))


def delete_command():

    currrent = tree.focus()
    back.delete(tree.item(currrent,'text'))
    tree.delete(*tree.get_children())
    for row in back.view():
        tree.insert('',END,text= row[0] ,values= (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

def update_command():
    current = tree.focus()
    aba = tree.item(current,'text')
    back.update(aba,school_text.get(),date_text.get(),Month_text.get(),year_text.get(),day_text.get(),session_text.get(),Present_text.get(),Total_text.get())

    tree.delete(*tree.get_children())
    for row in back.view():
        tree.insert('',END,text= row[0] ,values= (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))


def clear_all():
    for text in e1,e2,e3:
        text.delete(0,END)




window = Tk()

window.wm_title("Mind Grind Robotronics")
#labls
lab1 = Label(window ,text = "School" )
lab1.grid(row =0 ,column = 0)

lab2 = Label(window,text = "Date")
lab2.grid(row = 0,column = 2)

lab3 = Label(window,text = "Session")
lab3.grid(row = 1,column = 0)

lab3 = Label(window,text = "Present")
lab3.grid(row = 1,column = 2)

lab4 = Label(window,text = "Total")
lab4.grid(row = 1,column = 4)

#Combobox

school_text = StringVar()
C1 = ttk.Combobox(window, width=18,state = "readonly", textvariable=school_text)
C1['values'] = ("----Select School----","St Edwards","Stokes Memorial","St Thomas","ECI Chalet Day","Mount Shivalik","Trinity International School","Shimla Public School")
C1.grid(row=0,column=1)
C1.current(0)

date_text = StringVar()
c2 = ttk.Combobox(window,width = 17,state = "readonly", textvariable = date_text)
c2['values'] = ["Date",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
c2.grid(row = 0,column = 3)
c2.current(0)

Month_text = StringVar()
c3 = ttk.Combobox(window,width = 6,state = "readonly", textvariable = Month_text)
c3['values'] = ["Month",1,2,3,4,5,6,7,8,9,10,11,12]
c3.grid(row = 0,column = 4)
c3.current(0)

year_text = StringVar()
c4 = ttk.Combobox(window,width = 16,state = "readonly", textvariable = year_text)
c4['values'] = ["Year",2018,2019,2020,2021,2022,2023,2024,2025,2026,2027]
c4.grid(row = 0,column = 5)
c4.current(0)

day_text = StringVar()
c5 = ttk.Combobox(window,width =10 ,state = "readonly",textvariable = day_text)
c5['values'] = ["Day","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
c5.grid(row = 0,column = 6 )
c5.current(0)

#Entry TextBoxes
session_text = StringVar()
e1 = Entry(window,textvariable = session_text)
e1.grid(row = 1 ,column =1)

Present_text = StringVar()
e2 = Entry(window,textvariable = Present_text)
e2.grid(row = 1 ,column =3)

Total_text = StringVar()
e3 = Entry(window,textvariable = Total_text)
e3.grid(row = 1 ,column =5)

#Treebox

tree = ttk.Treeview(window)
tree["columns"] = ("one", "two", "three","four","five","six","seven","eight")
tree.column("one", width=100)
tree.column("two", width=50)
tree.column("three", width=50)
tree.column("four", width=50)
tree.column("five", width=80)
tree.column("six", width=130)
tree.column("seven", width=50)
tree.column("eight",width = 50)
tree.column("#0",width =50)


tree.heading("#0", text='ID', anchor='w')
tree.column("#0", anchor="w")
tree.heading("one", text="School")
tree.heading("two", text="Date")
tree.heading("three", text="Month")
tree.heading("four", text="Year")
tree.heading("five", text="Day")
tree.heading("six", text="Session")
tree.heading("seven", text="Present")
tree.heading("eight",text = "Total")
tree.grid(row= 3,column =0, rowspan = 8,columnspan = 8)

tree.bind('<<TreeviewSelect>>',get_selecte_row)

#Scrollbar
scrol1 = Scrollbar(window,orient = VERTICAL)
scrol1.grid(row= 4,column = 8,rowspan = 9)

scrol2 = Scrollbar(window,orient = HORIZONTAL)
scrol2.grid(row = 12,column =4,columnspan= 9)

#configure tree and Scrollbar
tree.configure(yscrollcommand = scrol1)
scrol1.configure(command = tree.yview)

tree.configure(xscrollcommand = scrol1)
scrol2.configure(command = tree.xview)

#buttons
b1 = Button(text = "Enter",width = 10 , command = insert_command,bg = "green")
b1.grid(row = 3 , column = 9)

b2 = Button(text = "View All",width = 10 ,command = view_command,bg = "green")
b2.grid(row = 4 , column = 9)

b3 = Button(text = "Update",width = 10, command = update_command,bg = "blue")
b3.grid(row = 5 , column = 9)

b4 = Button(text = "Search",width = 10,command = search_command,bg = "green")
b4.grid(row = 6 , column = 9)

b5 = Button(text = "Delete",width = 10,command = delete_command,bg ="red")
b5.grid(row = 7 , column = 9)

b6 = Button(text = "Clear all",width = 10,command = clear_all,bg = "green")
b6.grid(row = 8 , column = 9)

b7 = Button(text = "Close",width = 10,bg ="green",command = window.destroy)
b7.grid(row = 9 , column = 9)

img = PhotoImage(file = "Untitled.png")
panel = Label(window, image = img)
panel.grid(row = 13 ,column = 2,columnspan = 4)


window.mainloop()
