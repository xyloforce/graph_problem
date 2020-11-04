def create_neighborhoods(species_dict):
    neighbourhood = dict() # each char and his neighbors
    for i in species_dict: # i is a species
        for j in species_dict[i]: # j is a state of i
            if j not in neighbourhood: # ensure proper initialization
                neighbourhood[j]=set()
            neighbourhood[j].update(species[i]) # add states from the same species to j' neighbors
    return neighbourhood

def create_incompatibilities(species_dict):
    incompatibility = dict() # each char and his same characters
    pos_by_char = dict()
    for i in species_dict:
        for j in species_dict[i]: # j is a state in the species i
            index = species_dict[i].index(j)
            if j not in pos_by_char: # ensure proper initialization
                pos_by_char[j] = set()
            pos_by_char[j].add(index) # add value to set in order to avoid duplicates 
    for i in pos_by_char:
        if i not in incompatibility:
            incompatibility[i]=set()
        for j in pos_by_char:
            if i != j and pos_by_char[i]==pos_by_char[j]:
                incompatibility[i].add(j)
    print(incompatibility)
    return incompatibility
    
def dict_to_mzn_array(neighbourhood_dict):
    final_table="[" # start of array in mzn
    for i in neighbourhood_dict:
        final_table +="| " # start of line in mzn array
        for j in neighbourhood_dict:
            if j in neighbourhood_dict[i]:
                final_table += "true, "
            else:
                final_table += "false, "
        final_table = final_table[:-2]
        final_table += " "
    final_table += "|"
    final_table += "];"
    return final_table

def dict_keys_to_mzn_enum(neighbourhood_dict):
    enum="{"
    for i in neighbourhood_dict:
        enum += i + ","
    enum = enum[:-1]
    enum += "};"
    return enum

species = dict() # entry data
species["S1"]="A1", "B1", "C1"
species["S2"]="A1", "B2", "C1"

neighbourhood = create_neighborhoods(species)
final_table=dict_to_mzn_array(neighbourhood)
enum = dict_keys_to_mzn_enum(neighbourhood)
incompatibility = dict_to_mzn_array(create_incompatibilities(species))

result=open("table_mzn.txt", "w")
result.write(final_table + "\n");
result.write(incompatibility + "\n");
result.write(enum)
result.close()
