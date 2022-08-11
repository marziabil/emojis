from tkinter import *

root = Tk() #main window

#Creating a Label widget
myLabel1 = Label(root, text= "Hello World!")
myLabel2 = Label(root, text= "My name is Marzia")

#creating a button
myButton = Button(root, text= "Click here", padx=50) #padx makes button wider

#putting it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myButton.grid(row=2, column=2)

root.mainloop()


