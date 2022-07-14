from ast import Is
import simpful as sf
from eyebrows import Eyebrows

FS = sf.FuzzySystem()

#define a linguistic variable
S_1 = sf.FuzzySet( points=[[0,0.125], [12.5, 0.125], [12.5,0]] , term="no_eyebrows" )
S_2 = sf.FuzzySet( points=[ [0,0.05],[27.5,0.15], [27.5,0]], term="horizontal")
S_3 = sf.FuzzySet( points = [ [0,0.15], [35,0.4], [40,0]], term="slightly_furrowed")
S_4 = sf.FuzzySet( points = [ [0,0.395], [39.5,0]], term="highly_furrowed" )
FS.add_linguistic_variable("EB", sf.LinguisticVariable( [S_1, S_2, S_3, S_4]))

# Define consequents
FS.set_crisp_output_value("NO_EYEBROWS", 0)
FS.set_crisp_output_value("HORIZONTAL", 25)
FS.set_crisp_output_value("LOW", 50)
FS.set_crisp_output_value("HIGH", 75)

# Define fuzzy rules.
RULE1 = "IF(EB IS no_eyebrows) THEN (Eyebrows IS NO_EYEBROWS)"
RULE2 = "IF(EB IS horizontal) THEN (Eyebrows IS HORIZONTAL)"
RULE3 = "IF (EB IS slightly_furrowed) THEN (Eyebrows IS LOW)"
RULE4 = "IF (EB IS highly_furrowed) THEN (Eyebrows IS HIGH) "
FS.add_rules([RULE1, RULE2, RULE3, RULE4])

# Set antecedents values, perform Sugeno inference and print output values.
FS.set_variable("OXI", .51)
print (FS.Sugeno_inference(['POWER']))