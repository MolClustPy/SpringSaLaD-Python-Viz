import os

file_name = 'test_name.txt'

path_list = ['viewer_files', 'another_folder']

path_list.insert(0, file_name[:-4] + '_FOLDER')

search_directory = os.path.join(*path_list)

print(search_directory)