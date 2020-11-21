import re

def blast_to_dict(filename, start_window, end_window):
    """
    convert blast output to dict protein:state
    """
    with open(filename, 'r') as file:
        dico = {}
        sequence = ""
        for line in file: 
            line = line.rstrip()
            if line.startswith(">"): # it's a blast header
                espece = re.findall("\[(.+)\]", line)[0] # regex for "select all chars between two brackets" -> select species name
                dico[espece] = list()
                position = 1
                sequence = ""
                lp = ""

            else: # it's a protein line
                for l in line:
                    if position > end_window: # position is after the window : stop scan
                        break
                    elif position < start_window: # position is before the window : go to next pos
                        position += 1
                    else: # position is in window
                        lp = l + str(position) #  state is amino acid + pos of this amino acid in the sequence
                        dico[espece].append(lp) # add state to list corresponding to this protein's species
                        position +=1
        return dico

def create_neighborhoods(species_dict):
    neighbourhood = dict() # each char and his neighbors
    for i in species_dict: # i is a species
        for j in species_dict[i]: # j is a state of i
            if j not in neighbourhood: # ensure proper initialization
                neighbourhood[j]=set()
            neighbourhood[j].update(species_dict[i]) # add states from the same species to j' neighbors
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
    return incompatibility
    
def dict_to_mzn_array(neighbourhood_dict, name):
    final_table= name + " = [" # start of array in mzn
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
    enum="States_available = {"
    for i in neighbourhood_dict:
        enum += i + ","
    enum = enum[:-1]
    enum += "};"
    return enum

def dict_keys_to_mzn_set(neighbourhood_dict):
    mzn_set="number_States = 1.."
    mzn_set += str(len(neighbourhood_dict))
    mzn_set += ";"
    return mzn_set

def dict_keys_to_mzn_axis(neighbourhood_dict, axis_number):
    mzn_axis = "axe" + axis_number + " = "
    keys=list()
    for i in neighbourhood_dict:
        keys.append(i)
    mzn_axis += keys[0]
    mzn_axis += ".."
    mzn_axis += keys[-1]
    mzn_axis += ";"
    return mzn_axis

def sequence_length(filename):
    sequence_file = open(filename)
    int_set = set()
    length = 0
    for line in sequence_file:
        if line[0] == ">":
            if length > 0:
                int_set.add(length)
                length = 0
        else:
            length += len(line)
    return min(int_set)
