import matplotlib.pyplot as plt
import pandas as pd

def stdevPlots (path, data_selection):
    
    if type(data_selection) != list:
        print("Error: Your data_selection must be a list")
        return
    
    df = pd.read_csv(path, skiprows=1)
    
    output_columns = []
    molecule_list = []
    states = ['free', 'bound', 'total']
    num_entries = (df.shape[1] - 3)/2
    
    #Get list of molecule names from columns
    for item in df.columns:
        if item != ' ':
            split_item = item.split().pop()
            if '.1' not in split_item and split_item not in molecule_list and split_item != 'Time':
                molecule_list.append(split_item)
    
    #Determine the columns the user wants displayed based on the data_selection argument
    for item in data_selection:
        if type(item) == str:
            if item.upper() in (state.upper() for state in states):
                for column in df.columns:
                    if item.upper() in column and not '.1' in column:
                        if column not in output_columns:
                            output_columns.append(column)
            elif item in molecule_list:
                length = len(item)
                for column in df.columns:
                    if column[-length:] == item:
                        if column not in output_columns:
                            output_columns.append(column)
            else:
                print(f'Warning: "{item}" doesn\'t correspond to a recognized molecule name or state in the dataset provided')
        elif type(item) == int:
            if item < 1 or item > num_entries:
                print(f'Warrning: Entry {item} is out of range')
                continue
            if df.columns[item] not in output_columns:
                output_columns.append(df.columns[item])
        else:
            print('Error: Only str and int datatypes are allowed in the data_selection list')
            return

    if output_columns == []:
        print('Error: No data selected')
        return
    else:
        df.plot('Time', output_columns)
        for output in output_columns:
            plt.fill_between(df['Time'], 
                             df[output] - df[output + '.1'], 
                             df[output] + df[output + '.1'], 
                             alpha=0.2)

        plt.xlabel('Time (Seconds)')
        plt.ylabel('Average Molecule Counts')
        plt.show()
