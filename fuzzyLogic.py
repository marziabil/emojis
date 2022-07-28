
from simpful import FuzzySystem, FuzzySet, Trapezoidal_MF, LinguisticVariable
# from simpful import *

FS = FuzzySystem()

# #define linguistic variable - valence - (x axis in scherer's model)
V_1 = FuzzySet( function=Trapezoidal_MF(a=0, b=0, c=2, d=4), term="veryLow" )
V_2 = FuzzySet( function=Trapezoidal_MF(a=1,b=3,c=8,d=11), term="low")
V_3 = FuzzySet( function=Trapezoidal_MF(a=6,b=8.5,c=11.5,d=14), term="medium")
V_4 = FuzzySet( function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
V_5 = FuzzySet( function=Trapezoidal_MF(a=16,b=18,c=20,d=20), term="veryHigh")
FS.add_linguistic_variable("Valence", LinguisticVariable( [V_1, V_2, V_3, V_4, V_5], concept="Valence Level", universe_of_discourse=[0,20]))

#define linguistic variable - arousal - (y axis in scherer's model)
A_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0,c=2,d=4 ), term="veryLow" )
A_2 = FuzzySet(function=Trapezoidal_MF(a=1, b=8,c=11,d=11), term="low" )
A_3 = FuzzySet(function=Trapezoidal_MF(a=6, b=8.5,c=11.5,d=14), term="medium")
A_4 = FuzzySet(function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
A_5 = FuzzySet(function=Trapezoidal_MF(a=16,b=18,c=20,d=20), term="veryHigh")
FS.add_linguistic_variable("Arousal", LinguisticVariable([A_1,A_2,A_3,A_4,A_5], concept="level of arousal", universe_of_discourse=[0,20]))

# # Define output fuzzy sets and linguistic variable for overall emotional state
F_1 = FuzzySet(function=Trapezoidal_MF(a=0,b=0,c=3.5,d=6), term="veryUnpleasant")
F_2 = FuzzySet(function=Trapezoidal_MF(a=3,b=6.5,c=10,d=11), term="unpleasant")
F_3 = FuzzySet(function=Trapezoidal_MF(a=9,b=10,c=13.5,d=17), term="pleasant")
F_4 = FuzzySet(function=Trapezoidal_MF(a=9,b=16.5,c=13.5,d=20), term="veryPleasant")
FS.add_linguistic_variable ("emotionalState", LinguisticVariable([F_1, F_2, F_3, F_4], universe_of_discourse=[0,20]))


# Define fuzzy rules.
#veryLow Valence
R1 = "IF (Valence IS veryLow) AND (Arousal IS veryLow) THEN (emotionalState IS veryUnpleasant)"
R2 = "IF ((Valence IS veryLow) AND (Arousal IS low)) OR ((Valence IS veryLow) AND (Arousal IS medium)) OR ((Valence IS veryLow) AND (Arousal IS high)) THEN (emotionalState IS unpleasant)"
R3 = "IF (Valence IS veryLow) AND (Arousal IS veryHigh) THEN (emotionalState IS pleasant)"
#Low Valence
R4 = "IF (Valence IS low) AND (Arousal IS veryLow) THEN (emotionalState IS veryUnpleasant)"
R5 = "IF ((Valence IS low) AND (Arousal IS low)) OR ((Valence IS medium) AND (Arousal IS veryLow)) OR ((Valence IS medium) AND (Arousal IS veryHigh)) THEN (emotionalState IS unpleasant) "
R6 = "IF ((Valence IS low) AND (Arousal IS medium)) OR ((Valence IS low) AND (Arousal IS high)) OR ((Valence IS low) AND (Arousal IS veryHigh)) THEN (emotionalState IS pleasant)"
#Medium Valence
R7 = "IF ((Valence IS medium) AND (Arousal IS medium)) OR ((Valence IS medium) AND (Arousal IS high)) THEN (emotionalState IS pleasant) "
R8 = "IF (Valence IS medium) AND (Arousal IS veryHigh) THEN (emotionalState IS veryPleasant) "
R9 = "IF ((Valence IS medium) AND (Arousal IS veryLow)) OR ((Valence IS medium) AND (Arousal IS low)) THEN (emotionalState IS unpleasant)"
#High Valence
R10 = "IF ((Valence IS high) AND (Arousal IS veryLow)) OR ((Valence IS high) AND (Arousal IS medium)) OR ((Valence IS high) AND (Arousal IS high)) THEN (emotionalState IS pleasant)  "
R11 = "IF (Valence IS high) AND (Arousal IS low) THEN (emotionalState IS unpleasant) "
R12 = "IF (Valence IS high) AND (Arousal IS veryHigh) THEN (emotionalState IS veryPleasant) "
#Very high valence
R13 = "IF ((Valence IS veryHigh) AND (Arousal IS veryLow)) OR ((Valence IS veryHigh) AND (Arousal IS medium)) OR ((Valence IS veryHigh) AND (Arousal IS high)) THEN (emotionalState IS pleasant)"
R14 = "IF (Valence IS veryHigh) AND (Arousal IS low) THEN (emotionalState IS unpleasant) "
R15 = "IF ((Valence IS veryHigh) AND (Arousal IS veryHigh)) THEN (emotionalState IS veryPleasant)  "

FS.add_rules([R1,R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15])

# Set antecedents values
FS.set_variable("Valence", 2) #enter values between 0 to 20
FS.set_variable("Arousal", 20) #enter values between 0 to 20

# print output
print(FS.Mamdani_inference(["emotionalState"]))


# # Perform Mamdani inference and print output
# def mouth_Type():
#     return(FS.Mamdani_inference(["mouthType"]))

# # mouth_Type()

# def mouthForEmoji():
#     if mouth_Type < 9:
#         mouthForEmoji = "smile"
#     else: 
#         mouthForEmoji = "frowning"









