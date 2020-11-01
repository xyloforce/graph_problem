def create_neighborhoods(species_dict):
    neighbourhood = dict() # each char and his neighbors
    for i in species_dict: # i is a species
        for j in species_dict[i]: # j is a state of i
            if j not in neighbourhood: # ensure proper initialization
                neighbourhood[j]=set()
            neighbourhood[j].update(species[i]) # add states from the same species to j' neighbors
    return neighbourhood
    
def dict_to_mzn_array(neighbourhood_dict):
    final_table="[" # start of array in mzn
    for i in neighbourhood_dict:
        final_table +="|" # start of line in mzn array
        for j in neighbourhood_dict:
            if j in neighbourhood_dict[i]:
                final_table += "TRUE, "
            else:
                final_table += "FALSE, "
        final_table += "|"
    final_table += "];"
    return final_table

species = dict() # entry data
species["S1"]="P1", "Z2", "C3", "F4"
species["S2"]="C1", "A2", "V3", "F4"
species["S3"]="A1", "A2", "M3", "F4"
species["S4"]="A1", "C2", "M3", "A4"

final_table=dict_to_mzn_array(create_neighborhoods(species))

result=open("table_mzn.txt", "w")
result.write(final_table);
result.close()
