from tkinter import *

window = Tk() #create a main window
window.title("EmojiGen")
window.geometry('875x900') #set window size
window.configure(bg="white") #set window colour

#Labels
emojiGenLabel = Label(window, text="EmojiGen: a software which generates emojis to represent different emotions!", wraplength=900, justify="center",font=("Calibri Bold", 26), bg="#99ccff", fg="#003366")
emojiGenLabel.grid(column=0, row=0)

spaceLabel = Label(window, text=" ", bg="white")
spaceLabel.grid(column=0, row=1)

infoLabel = Label(window, text="EmojiGen uses valence and arousal to generate emojis:", wraplength=500, justify="center", font=( 16), bg="white"  )
infoLabel.grid(column=0, row=2)

infoLabel2 = Label(window, text= "- Valence describes the extent to which an emotion is positive or negative. Happinness is an example of positive valence, while sadness is an example of negative valence.\n \n- Arousal refers to an emotion's intensity, that is, the strength of its associated emotional state.\n", wraplength=500, justify="left", font=("Fira Sans", 14), bg="white" )
infoLabel2.grid(column=0, row=3 )

#get input using entry class
enterValence = Label(window, text="Valence: Enter a value between -1 (very unpleasant) and 1 (very pleasant):", font=15)
enterValence.grid(column=0, row=4)

entryText = StringVar()
entryText.set("Type a number...")

xValence = Entry(window, width=20, bg="#cce6ff", textvariable=entryText)
xValence.grid(column=0, row=5)

enterArousal = Label(window, text="Arousal: Enter a value between -1 (very low intensity) and 1 (very high intensity):", font=15)
enterArousal.grid(column=0, row=6)

yArousal = Entry(window, width=20,bg="#cce6ff", textvariable=entryText )
yArousal.grid(column=0, row=7)

clickLabel = Label(window,font=("Calibri", 14), bg="white" )
clickLabel.grid(column=0, row=8)
#handle button click event
def buttonClicked():
    clickLabel.configure(text="Emoji is being generated")

submitButton = Button(window, text="SUBMIT", bg="#cccccc", font=("Calibri", 15), fg="#1f1f2e", command=buttonClicked, padx=50,height=1, width=1)
submitButton.grid(column=0, row=8)



# #creating a button
# myButton = Button(root, text= "Click here", padx=50) #padx makes button wider

window.mainloop() #opens window till its closed


