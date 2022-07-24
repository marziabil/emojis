# # from simpful import *
# # import numpy as np
# import simpful as sf

# FS = sf.FuzzySystem()

# #define linguistic variable - arousal - (y axis in scherer's model)
# A_1 = sf.FuzzySet( points=[[0,1], [ 2,2], [4,0]] , term="very_low" )
# A_2 = sf.FuzzySet( points=[ [1,0],[3,1], [8,1], [11,0]], term="low")
# A_3 = sf.FuzzySet( points = [ [6,0], [8.5,1], [11.5, 1], [14,0]], term="medium")
# A_4 = sf.FuzzySet( points = [ [8,0], [12,1], [17,1], [19,0]], term="high" )
# A_5 = sf.FuzzySet( points= [[16,0], [18,1], [20,1]], term="very_high")
# FS.add_linguistic_variable("Arousal", sf.LinguisticVariable( [A_1, A_2, A_3, A_4, A_5]))

# #define linguistic variable - valence - (x axis in scherer's model)
# V_1 = sf.FuzzySet( points=[[0,1], [ 2,2], [4,0]] , term="very_low" )
# V_2 = sf.FuzzySet( points=[ [1,0],[3,1], [8,1], [11,0]], term="low")
# V_3 = sf.FuzzySet( points = [ [6,0], [8.5,1], [11.5, 1], [14,0]], term="medium")
# V_4 = sf.FuzzySet( points = [ [8,0], [12,1], [17,1], [19,0]], term="high" )
# V_5 = sf.FuzzySet( points= [[16,0], [18,1], [20,1]], term="very_high")
# FS.add_linguistic_variable("Valence", sf.LinguisticVariable( [V_1, V_2, V_3, V_4, V_5]))

# # Define output fuzzy sets and linguistic variable for face colour
# F_1 = sf.FuzzySet( points=[[0,1], [5,0]] , term="red" )
# F_2 = sf.FuzzySet(points=[[2.5,0], [7.5,1], [20,1]], term="yellow")
# FS.add_linguistic_variable ("faceColour", sf.LinguisticVariable([F_1, F_2]))

# # Define fuzzy rules.

# #Face Colour
# RULE1 = "If((Valence IS low) OR (Valence IS medium) AND (NOT(Valence IS high))) AND (Arousal IS high) AND (NOT(Arousal IS medium)) AND (NOT(Arousal IS low)) THEN (faceColour IS red))"
# RULE2 = "If ((Valence IS very_low) OR (Valence IS high OR (Valence IS very_high)) AND ((Arousal IS low) OR (Arousal IS high) OR (Arousal IS very_high) OR (Arousal IS medium) OR (Arousal is very_low)) THEN (faceColour is yellow) "

# # Set antecedents values
# FS.set_variable("Valence", 4)
# FS.set_variable("Arousal", 8)

# # Perform Mamdani inference and print output
# print(FS.Mamdani_inference(["faceColour"]))