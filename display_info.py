import os
import glob

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

#Displays all the files in the same directory as the input file (given by a path)
def file_info(path, list_neighbors=False):
    print('Selected File:\n' + os.path.split(path)[1] + '\n')
    print('Parent Directory:\n' + os.path.split(path)[0] + '\n')
    search_pattern = os.path.join(os.path.split(path)[0], '*Average*')
    entries = glob.glob(search_pattern)
    
    if list_neighbors:
        print('Average Files:')
        for entry in entries:
            #print(os.path.split(entry)[1][23:], )
            print('{0:50}  {1}'.format(os.path.split(entry)[1][23:], convert_bytes(os.path.getsize(entry))))

def column_info(path):
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