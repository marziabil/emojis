
from simpful import FuzzySystem, FuzzySet, Trapezoidal_MF, LinguisticVariable, Triangular_MF

FS = FuzzySystem()

# #define linguistic variable - valence - (x axis in scherer's model)
V_1 = FuzzySet( function=Trapezoidal_MF(a=0, b=0, c=2, d=3), term="veryLow" )
V_2 = FuzzySet( function=Trapezoidal_MF(a=1,b=3,c=8,d=11), term="low")
V_3 = FuzzySet( function=Trapezoidal_MF(a=6,b=8.5,c=11.5,d=14), term="medium")
V_4 = FuzzySet( function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
V_5 = FuzzySet( function=Trapezoidal_MF(a=17,b=18,c=20,d=20), term="veryHigh")
FS.add_linguistic_variable("Valence", LinguisticVariable( [V_1, V_2, V_3, V_4, V_5], concept="Valence Level", universe_of_discourse=[0,20]))

#define linguistic variable - arousal - (y axis in scherer's model)
A_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0,c=2,d=3 ), term="veryLow" )
A_2 = FuzzySet(function=Trapezoidal_MF(a=1, b=8,c=8,d=11), term="low" )
A_3 = FuzzySet(function=Trapezoidal_MF(a=6, b=8.5,c=11.5,d=14), term="medium")
A_4 = FuzzySet(function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
A_5 = FuzzySet(function=Trapezoidal_MF(a=17,b=18,c=20,d=20), term="veryHigh")
FS.add_linguistic_variable("Arousal", LinguisticVariable([A_1,A_2,A_3,A_4,A_5], concept="level of arousal", universe_of_discourse=[0,20]))

# # Define output fuzzy sets and linguistic variable for overall emotional state
F_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0,c=4,d=8), term="veryUnpleasant")
F_2 = FuzzySet(function=Trapezoidal_MF(a=2, b=6,c=16,d=24), term="unpleasant")
F_3 = FuzzySet(function=Triangular_MF(a=16,b=20,c=20), term="neutral")
F_4 = FuzzySet(function=Trapezoidal_MF(a=16,b=24,c=34,d=38), term="pleasant")
F_5 = FuzzySet(function=Trapezoidal_MF(a=32,b=36,c=40,d=40), term="veryHigh")
FS.add_linguistic_variable ("emotionalState", LinguisticVariable([F_1, F_2, F_3, F_4, F_5], universe_of_discourse=[0,40]))

#Fuzzy rules.
#veryLow Valence
R1 = "IF (Valence IS veryLow) AND (Arousal IS veryLow) THEN ((emotionalState IS veryUnpleasant) NOT (emotionalState IS unpleasant))"
R2 = "IF ((Valence IS veryLow) AND (Arousal IS low)) THEN (emotionalState IS unpleasant)"
R3 = "IF ((Valence IS veryLow) AND (Arousal IS veryHigh)) OR ((Valence IS veryLow) AND (Arousal IS high)) THEN ((emotionalState IS unpleasant) OR (emotionalState IS neutral)) "
R4 = "IF (Valence IS veryLow) OR (Arousal IS medium) THEN ((emotionalState IS neutral) AND (emotionalState IS unpleasant)) "
#Low Valence
R5 = "IF (Valence IS low) AND (Arousal IS veryLow) THEN ((emotionalState IS unpleasant) AND (emotionalState IS veryUnpleasant))" #changed from or to and
R6 = "IF ((Valence IS low) AND (Arousal IS low)) OR ((Valence IS low) AND (Arousal IS medium)) THEN (emotionalState IS unpleasant) "
R7 = "IF ((Valence IS low) AND (Arousal IS high)) OR ((Valence IS low) AND (Arousal IS veryHigh)) THEN ((emotionalState IS unpleasant) AND ((emotionalState IS neutral))"

#Medium Valence
R8 = "IF ((Valence IS medium) AND (Arousal IS high)) OR ((Valence IS medium) AND (Arousal IS veryHigh)) THEN ((emotionalState IS neutral) OR (emotionalState IS pleasant))"
R9 = "IF ((Valence IS medium) AND (Arousal IS veryLow)) THEN ((emotionalState IS neutral) NOT (emotionalState IS pleasant))  "
R10 = "IF ((Valence IS medium) AND (Arousal IS low)) OR ((Valence IS medium) AND (Arousal IS medium)) THEN ((emotionalState IS unpleasant) OR (emotionalState IS neutral))"
#High Valence
R11 = "IF ((Valence IS high) AND (Arousal IS veryLow)) THEN ((emotionalState IS pleasant) OR (emotionalState IS neutral))"
R12 = "IF ((Valence IS high) AND (Arousal IS low)) THEN (emotionalState IS pleasant) "
R13 = "IF ((Valence IS high) AND (Arousal IS high)) OR ((Valence IS high) AND (Arousal IS veryHigh)) THEN (emotionalState IS pleasant) "
#Very high valence
R14 = "IF ((Valence IS veryHigh) AND (Arousal IS veryLow)) THEN ((emotionalState IS pleasant) NOT (emotionalState IS unpleasant))"
R15 = "IF ((Valence IS veryHigh) AND (Arousal IS low)) OR ((Valence IS veryHigh) AND (Arousal IS medium)) THEN ((emotionalState IS neutral) NOT (emotionalState IS pleasant)) "
R16 = "IF ((Valence IS veryHigh) OR (Arousal IS veryHigh)) THEN (emotionalState IS veryPleasant)"
R17 = "IF ((Valence IS veryHigh) AND (Arousal IS high)) THEN ((emotionalState IS pleasant) NOT (emotionalState IS veryPleasant)) "
R18 = "IF ((Valence IS high) AND (Arousal IS medium)) THEN (emotionalState IS pleasant) "


FS.add_rules([R1,R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18])

#change values to a scale of 0 to 20
def findEmotionalState(xValence, yArousal):
    finalXValence = (xValence + 1) *10
    finalYArousal = (yArousal + 1) *10

    # Set antecedents values
    FS.set_variable("Valence",finalXValence) #enter values between 0 to 20
    FS.set_variable("Arousal",finalYArousal) #enter values between 0 to 20

    emoState = (FS.Mamdani_inference(["emotionalState"]))
    floatEmoState = float(emoState["emotionalState"])

    #convert values to positive and negative based on quadrants. Q1 and Q3 will have positive values, while Q2 and Q4 will have negative values
    if (finalXValence < 10 and finalYArousal > 10) or (finalXValence > 10 and finalYArousal < 10):
        return (floatEmoState * -1)
    else:
        return (floatEmoState * 1)







