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

#Finds the last file in the search_directory that contains substring in the name
def find_files_substring(search_directory, substring):
    for file in os.listdir(search_directory):
        if substring in file:
            match = os.path.join(search_directory, file)
    return match

#Finds the average molecule counts CSV for a given search_directory
def find_timecourse_data(search_directory, data_selection, file_name = None):
    if file_name == None:
        file_name = find_txt_file(search_directory)
    else:
        file_name = os.path.join(search_directory, file_name)
    search_directory = os.path.join(file_name[:-4] + '_FOLDER', 'data')
    result = find_files_substring(search_directory, data_selection)
    return result

#Finds the cluster fotm CSV for a given search_directory
def find_cluster_fotm(search_directory, file_name = None):
    if file_name == None:
        file_name = find_txt_file(search_directory)
    else:
        file_name = os.path.join(search_directory, file_name)
    search_directory = os.path.join(file_name[:-4] + '_FOLDER', 'data', 'Cluster_stat', 'Histograms', 'Size_Freq_Fotm', 'MEAN_Run')
    result = find_files(search_directory, 'Size_Freq_Fotm')
    return result, file_name

#Finds the cluster fotm CSV for a given search_directory
def find_viewer_file(search_directory, file_name = None, run = 0):
    if file_name == None:
        file_name = find_txt_file(search_directory)
    else:
        file_name = os.path.join(search_directory, file_name)
    search_directory = os.path.join(file_name[:-4] + '_FOLDER', 'viewer_files')
    result = find_files(search_directory, f'Run{run}')
    return result

#Displays all the files in the same directory as the input file (given by a path)
def list_neighbors(path):
    print('Selected File:\n' + os.path.split(path)[1] + '\n')
    print('Parent Directory:\n' + os.path.split(path)[0] + '\n')
    search_pattern = os.path.join(os.path.split(path)[0], '*Average*')
    entries = glob.glob(search_pattern)
    print('Average Files:')
    for entry in entries:
        print(os.path.split(entry)[1])

def describe_columns(path):
    df = pd.read_csv(path, skiprows=1)
    entries = int((df.shape[1] - 3)/2)

    print('Columns:')
    for i in range(1,entries+1):
        print(f'{i}: {df.columns[i]}')

    lines = []
    for i in range(entries):
        lines.append(i + 1)

    print('\nList of indicies:')
    print(lines)