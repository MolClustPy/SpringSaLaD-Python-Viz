import os
import fnmatch

def find_txt_file(search_directory):
    for file in os.listdir(search_directory):
        if file.endswith(".txt"):
            return os.path.join(search_directory, file)

def find_files(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, f"*{search_string}*"):
                match = os.path.join(root, filename)
    return match

def find_molecule_counts(search_directory, input_file = None):
    if input_file == None:
        input_file = find_txt_file(search_directory)
    else:
        input_file = search_directory + '\\' + input_file 
    simulation_directory = input_file[:-4] + '_FOLDER'
    search_directory = f'{simulation_directory}\data'
    result = find_files(search_directory, 'AverageMoleculeCounts')
    return result