import os
from data_locator import *

def read_input_file(directory_path):
    path = find_txt_file(directory_path)

    with open(path, "r") as f:
        lines = f.readlines()

    split_file = []
    current_list = []

    for line in lines:
        if line[0:3] == '***':
            split_file.append(current_list)
            current_list = []
        current_list.append(line.strip())
    split_file.append(current_list)
    split_file.pop(0)

    if len(split_file) < 10:
        print(f'Error: Input file {path} doesn\'t match the expected format. Please ensure your input file is unmodified and that there are no other .txt files at the top level of your search directory.')

    #Extract molecule data
    molecules = []
    molecule = []
    for line in split_file[2]:
        if line[0:9] == 'MOLECULE:':
            molecules.append(molecule)
            molecule = []
        molecule.append(line)
    molecules.append(molecule)    
    molecules.pop(0)

    return(molecules, split_file)