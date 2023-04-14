from tkinter import *
root = Tk()
#title box
root.title("GUI Calculator")
#create insert box
EntryBox= Entry(root, width=45, borderwidth=6)
EntryBox.grid(row=0, column=0, columnspan=5, padx= 15, pady=15)
#define function for button insert
def ButtonClick(number):
    current= EntryBox.get()
    EntryBox.delete(0, END)
    EntryBox.insert(0, str(current)+ str(number))

def Add():
    first_no= EntryBox.get()
    global int_first_no
    int_first_no = int(first_no)
    global math
    math= "add"
    EntryBox.delete(0, END)


    
def ButtonClear():
    EntryBox.delete(0, END)    


def Substract():
    first_no= EntryBox.get()
    global int_first_no
    int_first_no= int(first_no)
    global math
    math= "subtract"
    EntryBox.delete(0, END)

def Multiply():
    first_no= EntryBox.get()
    global int_first_no
    int_first_no= int(first_no)
    global math
    math= "multiply"
    EntryBox.delete(0, END)

def Divide():
    first_no= EntryBox.get()
    global int_first_no
    int_first_no= int(first_no)
    global math
    math= "divide"
    EntryBox.delete(0, END)

def Equals():
    second_no= EntryBox.get()
    int_second_no = int(second_no)
    EntryBox.delete(0, END)
    global math
    if math== "add":
        EntryBox.insert(0, int_first_no + int_second_no)
    if math== "subtract":
        EntryBox.insert(0, int_first_no - int_second_no)
    if math== "multiply":
        EntryBox.insert(0, int_first_no * int_second_no) 
    if math== "divide":
        EntryBox.insert(0, int_first_no / int_second_no)           




#button design and placement
button_1= Button (root, text="1", padx=30, pady=30, command=lambda:ButtonClick(1)).grid(row=1,column=0)
button_2= Button (root, text="2", padx=30, pady=30, command=lambda:ButtonClick(2)).grid(row=1,column=1)
button_3= Button (root, text="3", padx=30, pady=30, command=lambda:ButtonClick(3)).grid(row=1,column=2)
button_4= Button (root, text="4", padx=30, pady=30, command=lambda:ButtonClick(4)).grid(row=2,column=0)
button_5= Button (root, text="5", padx=30 , pady=30, command=lambda:ButtonClick(5)).grid(row=2,column=1)
button_6= Button (root, text="6", padx=30 , pady=30, command=lambda:ButtonClick(6)).grid(row=2,column=2)
button_7= Button (root, text="7", padx=30 , pady=30, command=lambda:ButtonClick(7)).grid(row=3,column=0)
button_8= Button (root, text="8", padx=30 , pady=30, command=lambda:ButtonClick(8)).grid(row=3,column=1)
button_9= Button (root, text="9", padx=30 , pady=30, command=lambda:ButtonClick(9)).grid(row=3,column=2)
button_0= Button (root, text="0", padx=30 , pady=30, command=lambda:ButtonClick(0)).grid(row=4,column=1)
button_add= Button (root, text="+", padx=30 , pady=30,command=Add).grid(row=1,column=4)
button_subtract= Button (root, text="-", padx=30 , pady=30,command=Substract).grid(row=2, column=4)
button_divide= Button (root, text="/", padx=30 , pady=30, command=Divide).grid(row=4, column=4)
button_multiply= Button (root, text="*", padx=30 , pady=30,command=Multiply).grid(row=3, column=4)
button_equals=Button (root, text="=", padx=30 , pady=30, command=Equals).grid(row=4,column=2)
button_clear=Button (root, text="C", padx=30 , pady=30,command= ButtonClear).grid(row=4,column=0)


root.mainloop()


