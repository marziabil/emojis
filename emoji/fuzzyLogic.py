from simpful import *

FS = FuzzySystem()

#define linguistic variable - arousal - (y axis in scherer's model)
A_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0,c=2,d=4 ), term="very_low" )
A_2 = FuzzySet(function=Trapezoidal_MF(a=1, b=8,c=11,d=11), term="low" )
A_3 = FuzzySet(function=Trapezoidal_MF(a=6, b=8.5,c=11.5,d=14), term="medium")
A_4 = FuzzySet(function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
A_5 = FuzzySet(function=Trapezoidal_MF(a=16,b=18,c=20,d=20), term="very_high")
FS.add_linguistic_variable("Arousal", LinguisticVariable([A_1,A_2,A_3,A_4,A_5], concept="level of arousal", universe_of_discourse=[0,20]))

# #define linguistic variable - valence - (x axis in scherer's model)
V_1 = FuzzySet( function=Trapezoidal_MF(a=0, b=0, c=2, d=4), term="very_low" )
V_2 = FuzzySet( function=Trapezoidal_MF(a=1,b=3,c=8,d=11), term="low")
V_3 = FuzzySet( function=Trapezoidal_MF(a=6,b=8.5,c=11.5,d=14), term="medium")
V_4 = FuzzySet( function=Trapezoidal_MF(a=8,b=12,c=17,d=19), term="high")
V_5 = FuzzySet( function=Trapezoidal_MF(a=16,b=18,c=20,d=20), term="very_high")
FS.add_linguistic_variable("Valence", LinguisticVariable( [V_1, V_2, V_3, V_4, V_5], concept="Valence Level", universe_of_discourse=[0,20]))

# # Define output fuzzy sets and linguistic variable for mouth type
F_1 = FuzzySet(function=Trapezoidal_MF(a=0,b=0,c=3,d=6), term="frown")
F_2 = FuzzySet(function=Trapezoidal_MF(a=4,b=6,c=12,d=14), term="clenched")
F_3 = FuzzySet(function=Trapezoidal_MF(a=12,b=14,c=20,d=20), term="smiling")
FS.add_linguistic_variable ("mouthType", LinguisticVariable([F_1, F_2, F_3], universe_of_discourse=[0,20]))


# Define fuzzy rules.
#Mouth type
R1 = "IF (Valence IS low) AND (Arousal IS low) THEN (mouthType IS frown)"
R2 = "IF (Valence IS high) AND (Arousal IS very_high) THEN (mouthType IS smiley)"
R3 = "IF (Valence IS medium) OR (Arousal IS medium) THEN (mouthType IS clenched) "
FS.add_rules([R1,R2, R3])

# Set antecedents values
FS.set_variable("Valence", 9)
FS.set_variable("Arousal", 2)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["mouthType"]))





