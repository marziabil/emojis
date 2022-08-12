from tkinter import *

window = Tk() #create a main window
window.title("EmojiGen")
window.geometry('1000x800') #set window size
window.configure(bg="white") #set window colour

welcomeLabel = Label(window, text="Welcome to EmojiGen, a software which generates emojis for all emotions (amost)!", wraplength=1000, justify="center",font=("Calibri Bold", 20), bg="white", fg="#003366")
welcomeLabel.grid(column=0, row=0)

spaceLabel = Label(window, text=" ", bg="white")
spaceLabel.grid(column=1, row=1)

infoLabel = Label(window, text="EmojiGen uses valence and arousal to generate emojis:", wraplength=700, justify="center", font=("Calibri", 14), bg="white"  )
infoLabel.grid(column=0, row=2)

valenceLabel = Label(window, text= "Valence describes the extent to which an emotion is positive or negative. Happinness is an example of positive valence, while sadness is an example of negative valence.", wraplength=500, justify="left", font=("Calibri", 14), bg="white" )
valenceLabel.grid(column=0, row=3 )


# window, text="Valence describes the extent to which an emotion is positive or negative. Happinness is an example of positive valence, while sadness is an example of negative valence.", font=("Calibri", 12), bg="white")

clickLabel = Label(window,font=("Calibri", 14), bg="white" )
clickLabel.grid(column=1, row=4)
#handle button click event
def buttonClicked():
    clickLabel.configure(text="Emoji is being generated")

submitButton = Button(window, text="SUBMIT", bg="white", font=("Calibri", 15), fg="#1f1f2e", command=buttonClicked)
submitButton.grid(column=1, row=3)

# #creating a button
# myButton = Button(root, text= "Click here", padx=50) #padx makes button wider

# #putting it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
# myButton.grid(row=2, column=2)

window.mainloop() #opens window


