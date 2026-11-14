from tkinter import *
from tkinter.ttk import *
# importing the library

window = Tk()
# creating a window

window.geometry("600x600")
# giving width and height to the window

window.title("My First GUI App")
# giving the title

heading = Label(window,text="Training from Renuka my city mate",font=("Arial",20))
heading.place(x=100,y=50)
# creating the label

Name = Label(window,text="Name")
Name.place(x=100,y=200)
namentry = Entry(window)
namentry.place(x=200,y=200)
#entry box


submitbutton = Button(window,text="Submit",command=window.destroy) 
submitbutton.place(x=150,y=300)
#to place the button

spinbox = Spinbox(window,values=("Apple","Mango","Banana","Watermelon","Orange"))
spinbox.place(x=200,y=350)
#spinbox just like list dropdown

spinboxnum = Spinbox(window,values=(2,5,8,6,1))
spinboxnum.place(x=250,y=400)
#spinbox just like list dropdown for numbers

spinboxnumseries = Spinbox(window,from_=1,to=10)
spinboxnumseries.place(x=300,y=450)
#spinbox to generate the series

combobox = Combobox(window,values=("Apple","Mango","Banana","Watermelon","Orange"))
combobox.place(x=350,y=500)
#same as spinbox as a drop down

Age = Label(window,text="Age")
Age.pack(side="bottom")
namentry = Entry(window)
namentry.place(x=200,y=200)


 




































window.mainloop()
# to see the output