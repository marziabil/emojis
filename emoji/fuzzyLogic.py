from ast import Is
import simpful as sf
#from eyebrows import Eyebrows

FS = sf.FuzzySystem()

#define linguistic variable - arousal
S_1 = sf.FuzzySet( points=[[0,1], [ 1,1], [2,1]] , term="very_low" )
S_2 = sf.FuzzySet( points=[ [1,0],[2,1], [3.5,1], [5,0]], term="low")
S_3 = sf.FuzzySet( points = [ [3,0], [4,1], [5.5, 1], [7,0]], term="medium")
S_4 = sf.FuzzySet( points = [ [5,0], [5.5,1], [8.5,1], [9,0]], term="high" )
S_5 = sf.FuzzySet( points= [[8,0], [9,1], [10,1]], term="very_high")
FS.add_linguistic_variable("Arousal", sf.LinguisticVariable( [S_1, S_2, S_3, S_4, S_5]))

#define linguistic variable - valence
F_1 = sf.FuzzySet( points=[[0,1], [ 1,1], [2,0]] , term="very_low" )
F_2 = sf.FuzzySet( points=[ [1,0],[2,1], [3.5,1], [5,0]], term="low")
F_3 = sf.FuzzySet( points = [ [3,0], [4,1], [5.5, 1], [7,0]], term="medium")
F_4 = sf.FuzzySet( points = [ [5,0], [5.5,1], [8.5,1], [9,0]], term="high" )
F_5 = sf.FuzzySet(points= [[8,0], [9,1], [10,1]], term="very_high")
FS.add_linguistic_variable("Valence", sf.LinguisticVariable( [F_1, F_2, F_3, F_4, F_5]))

# Define output crisp values
FS.set_crisp_output_value("VERY LOW", -0.6)
FS.set_crisp_output_value("LOW", -0.2)
FS.set_crisp_output_value("MEDIUM", 0.2)
FS.set_crisp_output_value("HIGH", 0.6)
FS.set_crisp_output_value("VERY HIGH", 1)

# Define fuzzy rules.
#Mouth
#very low mouth is zigzag, low is frowning, 
RULE1 = "IF(Valence IS low) AND (Arousal IS low) THEN (Mouth IS LOW)"
RULE2 = "IF(Valence IS very_low) THEN (Mouth IS VERY LOW)" 
RULE3 = "IF (Valence IS low) AND (Arousal IS very_low) THEN (Mouth IS VERY LOW)" #open mouth. how do i indicate this?
FS.add_rules([RULE1, RULE2, RULE3])

# Set antecedents values
FS.set_variable("Valence", 4)
FS.set_variable("Arousal", 8)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["Tip"]))