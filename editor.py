import re
from input_file_extraction import *
import tempfile
from Project_reader import *
from data_locator import *
import os

def edit_input_file(search_directory, counts=[], on_rate=[], off_rate=[]):

    path = find_txt_file(search_directory)

    molecules, split_file = read_input_file('Input_File_Editor')

    molecule_descriptions = []
    reaction_descriptions = []
    for molecule in molecules:
        if molecule[0][0:8] == 'MOLECULE':
            molecule_descriptions.append(molecule[0].split())

    if counts != []:
        for i, count in enumerate(counts):
            molecule_descriptions[i][4] = count
            molecule_descriptions[i] = (' '.join(map(str, molecule_descriptions[i])))

    for section in split_file:
        if section[0][:15] == '*** BIMOLECULAR':
            for reaction in section[2:-1]:
                reaction_descriptions.append(reaction.split())

    if on_rate != []:
        for i, count in enumerate(on_rate):
            diff = len(reaction_descriptions[i]) - 18
            reaction_descriptions[i][13 + diff] = count
    
    if off_rate != []:
        for i, count in enumerate(off_rate):
            diff = len(reaction_descriptions[i]) - 18
            reaction_descriptions[i][15 + diff] = count

    for i in range(len(reaction_descriptions)):
        reaction_descriptions[i] = (' '.join(map(str, reaction_descriptions[i])))

    with open(path, 'r') as file: 
        data = file.readlines() 
    file.close()

    if counts != []:
        count = 0
        for i, line in enumerate(data):
            if line[0:11] == 'MOLECULE: "':
                data[i] = molecule_descriptions[count] + '\n'
                count = count + 1
    
    if on_rate != [] or off_rate != []:
        for i, line in enumerate(data):
            if line[:15] == '*** BIMOLECULAR':
                for j, item in enumerate(reaction_descriptions):
                    data[i+j+2] = item + '\n'

    #file_name = "output.txt"
    #file_path = os.path.join(search_directory, file_name)

    with open(path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(data)

    output_file.close()