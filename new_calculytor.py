from tkinter import *
from tkinter import messagebox 
from string_float import *
from parse_string import *
from func_count import * 
from PIL import ImageTk,Image

root = Tk()
root.title("MY CHILD")

w = root.winfo_screenwidth()  #высота и ширина экрана
h = root.winfo_screenheight() 
w = w//2 - 200 
h = h//2 -150

root.geometry('400x300+{}+{}'.format(w, h))
root.resizable(False, False)

img = Image.open('C:\\Users\\Admin\\see.jpg') # идентефецирует файл, но файл остается открытым и не считанным
render = ImageTk.PhotoImage(img) # создает совместимость Tk с растровым изображением render = оказывать
initil = Label(root, image = render) 
initil.pack()


lab1 = Label(text = "calculate", font = ('Halvetica', '12')) #, foreground = 'black', background = None)
lab1.place(relx = 0.05, rely = 0.02)

lab2 = Label(text = "result", font = ('Halvetica', '12'), foreground = 'black',  background = None)
lab2.place(relx = 0.6, rely = 0.02)

mess1 = StringVar() # говорит о том, что будет содержать строковое значение
message_entry1 = Entry(textvariable = mess1 )
message_entry1.place(relx=.05, rely=.1) # относительные единицы, относительно окна

mess2 = StringVar # говорит о том, что будет содержать строковое значение
message_entry2 = Entry(textvariable = mess2 )
message_entry2.place(relx=.6, rely=.1) # относительные единицы, относительно окна

def buttons(x, y, sign):
    frame = Frame(bg = 'black')
    frame.pack()

    message_button = Button(text = sign, command = lambda: message_entry1.insert(len(message_entry1.get()), sign),
        padx = 5, pady = 8, font = ('Halvetica', '15'), bg = "#ffaf8a", width = 1  )
    message_button.place(relx = x, rely = y)
    
def delete():
    
    message_entry1.delete(0, END)
    message_entry2.delete(0, END)

button_delete = Button (text = "DELETE", command = delete, bd = 3, bg = '#ffaf8a', padx = 5, pady = 8, font = ('Halvetica', '10'))
button_delete.place (relx = .6, rely = .25)

def one_meaning_delete():

    message_entry1.delete(first = (len(message_entry1.get()) - 1))
    
button_one_delete = Button(text = "<-", command = one_meaning_delete, bd = 3, bg = '#ffaf8a', padx = 5, pady = 8, font = ('Halvetica', '10'))
button_one_delete.place(relx = 0.82, rely = 0.25)

def func_continue():
    copy_mess2 = message_entry2.get()
    message_entry2.delete(0, END)
    message_entry1.delete(0, END)
    message_entry1.insert(len(message_entry1.get()), copy_mess2) 

button_continue = Button(text = "CONTINUE", command = func_continue, bd = 3, bg = '#ffaf8a', padx = 5, pady = 8, font = ('Halvetica', '10'))
button_continue.place(relx = .6, rely = 0.45)   #relx = .6, rely = .35

buttons(0.05, 0.2, "1")
buttons(0.15, 0.2, "2")
buttons(0.25, 0.2, "3")
buttons(0.05, 0.4, "4")
buttons(0.15, 0.4, "5")
buttons(0.25, 0.4, "6")
buttons(0.05, 0.6, "7")
buttons(0.15, 0.6, "8")
buttons(0.25, 0.6, "9")
buttons(0.15, 0.8, "0")
buttons(0.25, 0.8, ".")

buttons(0.45, 0.1, "+")
buttons(0.45, 0.32, "-")
buttons(0.45, 0.54, "*")
buttons(0.45, 0.76, "/")

def equally():
    operands, operators = parse_string(str(mess1.get()))
    answer = defining_func(operands, operators)
    message_entry2.insert(0, answer)


equally_button = Button (text = "EQUAL TO", command = equally, bd = 3, bg = '#ffaf8a', padx = 5, pady = 8, font = ('Halvetica', '10')) 
equally_button.place(relx = .6, rely = .65)



root.mainloop()