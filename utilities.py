species = dict()
species["S1"]="P1", "Z2", "C3", "F4"
species["S2"]="C1", "A2", "V3", "F4"
species["S3"]="A1", "A2", "M3", "F4"
species["S4"]="A1", "C2", "M3", "A4"

neighbourhood = dict()

for i in species:
    for j in species[i]:
        if j not in neighbourhood:
            neighbourhood[j]=set()
        j.update(species[i])
