import re

def blast_to_dict(filename, start_window, end_window):
    """
    Faire Blast à partir d'une séquence de protéine d'une espèce de façon à trouver des séquences homologues de façon a récupérer d'autres séquences de cette protéines pour d'autres espèces. 
    """
    with open(filename, 'r') as file:
        dico = {}
        sequence = ""
        for line in file: 
            line = line.rstrip()
            if line.startswith(">"): 
                #On traite la première ligne du bloc de l'espèce
                espece = re.findall("\[(.+)\]", line)[0] # regex for "select all chars between two brackets"
                # element = line.replace('[', ';').replace(']', ';').split(';') #On récupère le nom de l'espèce
                # espece = element[1]
                dico[espece] = list()
                position = 1
                sequence = ""
                lp = ""

            else:
                #On traite le bloc de séquence
                for l in line:
                    if position > end_window:
                        break
                    elif position < start_window:
                        position+=1 #incrémente position de +1
                    else:
                        lp = l + str(position) # Associe à l'AA sa position dans la séquence
                        dico[espece].append(lp)
                        position+=1 #incrémente position de +1
                # dico[espece] = sequence #Dico avec clé espèce et valeur associée
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
