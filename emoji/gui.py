from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

window = Tk() #create a main window
window.title("Emojinator")
window.geometry('1200x770') #set window size
window.configure(bg="white") #set window colour

#Labels
emojinatorLabel = Label(window, text="      Emojinator: a software which generates emojis to represent different emotions!           ", wraplength=1500, justify="center",font=("Calibri Bold", 24), bg="#99ccff", fg="#003366")
emojinatorLabel.grid(column=0, row=0)

spaceLabel = Label(window, text=" ", bg="white")
spaceLabel.grid(column=0, row=1)

infoLabel = Label(window, text="You can create a new emoji too!\n\n Enter valence and arousal values (Option 1):\n", wraplength=1200, justify="center", font=("Calibri bold", 15), bg="white", fg="#003366")
infoLabel.grid(column=0, row=2)

valenceLabel = Label(window, text= "Valence describes the extent to which an emotion is positive or negative.\nHappinness is an example of positive valence, while sadness is an example of negative valence.\nEnter a value between -1.0 (very unpleasant) and 1.0 (very pleasant):\n", wraplength=1200, justify="center", font=("Calibri", 13), bg="white" )
valenceLabel.grid(column=0, row=3)

#get input using entry class

enterValence = Entry(window, bg="#cce6ff", width=20)
enterValence.grid(column=0, row=4)

#Arousal label and entry box
arousalLabel = Label(window, text= "\nArousal refers to an emotion's intensity, that is, the strength of its associated emotional state.\nEnter a value between -1.0 (very low intensity) and 1.0 (very high intensity):\n", wraplength=1000, justify="center", font=("Calibri", 13), bg="white" )
arousalLabel.grid(column=0, row=5)

enterArousal = Entry(window, width=20,bg="#cce6ff")
enterArousal.grid(column=0, row=6)

#Select an emotion option
emotionLabel = Label(window, text="\nSelect an emotion (Option 2):\n", wraplength=1500, justify="center",font=("Calibri Bold", 15), bg="white", fg="#003366")
emotionLabel.grid(column=0, row=11)

#dictionaries to store emotions and their valence & arousal
emotionValence = {"Adventurous": 0.49, "Afraid": -0.12, "Alarmed": -0.08, "Ambitious": 0.45, "Amorous": 0.85, "Amused": 0.55, "Angry": -0.4, "Annoyed": -0.45, "Anxious": -0.725, "Apathetic": -0.2, "Aroused": 0.36, "Ashamed": -0.45, "Astonished": 0.42, "At Ease": 0.75, "Attentive": 0.49, "Bellicose": -0.12, "Bitter": -0.8, "Bored": -0.35, "Compassionate": 0.38, "Conceited": 0.19, "Confident": 0.51, "Conscientious": 0.32, "Contemplative": 0.59, "Contemptuous": -0.58, "Content": 0.81, "Convinced": 0.42, "Courageous": 0.81, "Defiant": -0.62, "Dejected": -0.51, "Delighted": 0.89, "Depressed": -0.81, "Desperate": -0.8, "Despondent": -0.567, "Determined": 0.725, "Disappointed": -0.8, "Discontented": -0.625, "Disgusted": -0.66, "Dissatisfied": -0.6, "Distressed": -0.7, "Distrustful": -0.48, "Doubtful": -0.275, "Droopy": -0.32, "Embarassed": -0.31, "Enraged": -0.18, "Enthusiastic": 0.5, "Envious": -0.28, "Excited": 0.7, "Expectant": 0.32, "Feel Guilt": -0.4, "Feel Well": 0.91, "Feeling Superior": 0.325, "Friendly": 0.75, "Frustrated": -0.6, "Glad": 0.95, "Gloomy": -0.86, "Happy": 0.9, "Hateful": -0.58, "Hesitant": -0.31, "Hopeful": 0.61, "Hostile": -0.28, "Impatient": -0.05, "Impressed": 0.39, "Indignant": -0.25, "Insulted": -0.725, "Interested": 0.65, "Jealous": -0.06, "Joyous": 0.95, "Languid": -0.22, "Light Hearted": 0.41, "Loathing": -0.8, "Longing": 0.22, "Lusting": 0.22, "Melancholic": -0.06, "Miserable": -0.925, "Passionate": 0.32, "Peaceful": 0.55, "Pensive": 0.03, "Pleased": 0.89, "Polite": 0.39, "Relaxed": 0.72, "Reverent": 0.21, "Sad": -0.825, "Satisfied": 0.78, "Selfconfident": 0.81, "Serene": 0.85, "Serious": 0.21, "Sleepy": 0.02, "Solemn": 0.81, "Startled": -0.925, "Suspicious": -0.32, "Taken Aback": -0.4, "Tense": -0.04, "Tired": -0.02, "Triumphant": 0.6, "Uncomfortable": -0.675, "Wavering": -0.56, "Worried": -0.06}
emotionArousal = {"Adventurous": 0.91, "Afraid": 0.79, "Alarmed": 0.89, "Ambitious": 0.65, "Amorous": -0.15, "Amused": 0.2, "Angry": 0.79, "Annoyed": 0.65, "Anxious": -0.8, "Apathetic": -0.11, "Aroused": 0.92, "Ashamed": -0.5, "Astonished": 0.89, "At Ease": -0.6, "Attentive": -0.48, "Bellicose": 0.95, "Bitter": 0.26, "Bored": -0.8, "Compassionate": -0.925, "Conceited": 0.66, "Confident": -0.2, "Conscientious": -0.8, "Contemplative": -0.6, "Contemptuous": 0.66, "Content": -0.59, "Convinced": 0.42, "Courageous": 0.59, "Defiant": 0.725, "Dejected": -0.86, "Delighted": 0.35, "Depressed": -0.46, "Desperate": -0.5, "Despondent": -0.425, "Determined": 0.26, "Disappointed": -0.04, "Discontented": 0.32, "Disgusted": 0.49, "Dissatisfied": -0.175, "Distressed": 0.55, "Distrustful": 0.1, "Doubtful": -0.95, "Droopy": -0.925, "Embarassed": -0.6, "Enraged": 0.72, "Enthusiastic": 0.32, "Envious": 0.82, "Excited": 0.725, "Expectant": 0.06, "Feel Guilt": -0.425, "Feel Well": -0.06, "Feeling Superior": 0.55, "Friendly": -0.6, "Frustrated": 0.39, "Glad": -0.17, "Gloomy": -0.48, "Happy": 0.16, "Hateful": 0.85, "Hesitant": -0.725, "Hopeful": -0.3, "Hostile": 0.85, "Impatient": 0.3, "Impressed": -0.18, "Indignant": 0.45, "Insulted": 0.2, "Interested": 0.3, "Jealous": 0.56, "Joyous": 0.13, "Languid": -0.5, "Light Hearted": 0.29, "Loathing": 0.425, "Longing": -0.42, "Lusting": 0.85, "Melancholic": -0.5, "Miserable": -0.13, "Passionate": 0.12, "Peaceful": -0.8, "Pensive": -0.6, "Pleased": -0.1, "Polite": -0.68, "Relaxed": -0.65, "Reverent": -0.95, "Sad": -0.4, "Satisfied": -0.62, "Selfconfident": 0.66, "Serene": -0.47, "Serious": -0.68, "Sleepy": -0.99, "Solemn": -0.47, "Startled": 0.04, "Suspicious": 0.26, "Taken Aback": -0.23, "Tense": 0.85, "Tired": -0.99, "Triumphant": 0.79, "Uncomfortable": -0.375, "Wavering": -0.7, "Worried": -0.34}

#Dropdown box to select emotion
emotion = StringVar()
dropdownBox = Combobox(window, values=list(emotionValence.keys()), justify="center", textvariable=emotion, state="readonly")
# # dropdownBox.current(0) #set the selected item
dropdownBox.grid(column=0,row=12)

spacerLabel = Label(window, text="", bg="white")
spacerLabel.grid(column=0, row=8)

# #click label which shows text after submit button is selected
clickLabel = Label(window,font=("Calibri", 14), bg="white" )
clickLabel.grid(column=0, row=10)

# #handle button click event
def buttonClicked():
    clickLabel.configure(text="Emoji is being generated")

#validate values entered in the entry box
def validation():
    global valenceValue, arousalValue
    valenceValue = enterValence.get()
    arousalValue = enterArousal.get()

    try:
        if type(valenceValue)==str and type(arousalValue)==str:
            try:
                valenceValue=float(valenceValue)
                arousalValue=float(arousalValue)
            except Exception as e:
                raise Exception("Cannot convert string to float")
        #check if both value are float
        if type(valenceValue)==float and type(arousalValue)==float:
            if (-1.0<valenceValue<1.0) and (-1.0<valenceValue<1.0):
                msg ="Success"
            else:
                msg="Enter a value between the range of -1 and 1"
                raise Exception("Enter a value between the range of -1 and 1")
        else:
            msg="Enter a decimal or numeric value"
            raise Exception("Enter a decimal or numeric value")
    except Exception as ep:
        messagebox.showerror("error", ep)
        messagebox.showinfo("message", msg)

#submit button for option 1
submitButton = Button(window, text="SUBMIT", bg="#003399", font=("Calibri", 15), fg="#ffffff", command=lambda:[validation(), buttonClicked()] , padx=50,height=1, width=1)
submitButton.grid(column=0, row=9)

spaceLabel = Label(window, text="", bg="white")
spaceLabel.grid(column=0, row=13)

#submit button for dropdown (option 2)
submitButton2 = Button(window, text="SUBMIT", bg="#003399", font=("Calibri", 15), fg="#ffffff", padx=50,height=1, width=1)
submitButton2.grid(column=0, row=14)



window.mainloop() #opens window till its closed
