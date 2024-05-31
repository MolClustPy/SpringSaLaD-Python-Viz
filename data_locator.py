import os
import fnmatch
import glob
import pandas as pd

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

def data_file_finder(search_directory, path_list, search_term = None, file_name = None, run = None):
    if file_name == None:
        file_name = find_txt_file(search_directory)
    else:
        file_name = os.path.join(search_directory, file_name)
    path_list.insert(0, file_name[:-4] + '_FOLDER')
    lower_search_directory = os.path.join(*path_list)
    if run != None:
        result = find_files(lower_search_directory, f'Run{run}')
    else:
        result = find_files(lower_search_directory, search_term)
    return result