import os
import fnmatch

#Finds the first txt file in the search_directory
def find_txt_file(search_directory):
    for file in os.listdir(search_directory):
        if file.endswith(".txt"):
            return os.path.join(search_directory, file)

#Finds the last file in the search_directory and its subdirecotires that matches the file_name
def find_files(search_directory, file_name):
    for root, dirs, files in os.walk(search_directory):
        for filename in files:
            if fnmatch.fnmatch(filename, f"*{file_name}*"):
                match = os.path.join(root, filename)
    return match

#Finds the average molecule counts CSV for a given search_directory
def find_molecule_counts(search_directory, file_name = None):
    if file_name == None:
        file_name = find_txt_file(search_directory)
    else:
        file_name = os.path.join(search_directory, file_name)
    search_directory = os.path.join(file_name[:-4] + '_FOLDER', 'data')
    result = find_files(search_directory, 'AverageMoleculeCounts')
    return result