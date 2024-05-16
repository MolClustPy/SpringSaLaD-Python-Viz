import matplotlib.pyplot as plt
import pandas as pd

def stdevPlots (path, output):
    df = pd.read_csv(path, skiprows=1)
    
    molecules = []
    molecules2 = []

    group_inputs = ['free', 'bound', 'total']
    
    for item in df.columns:
        if item != ' ':
            split_item = item.split().pop()
            if '.1' not in split_item and split_item not in molecules2 and split_item != 'Time':
                molecules2.append(split_item)

    if type(output) != list:
        print("Your output must be a list")
        return
    
    for item in output:
        if type(item) == str:
            if item in group_inputs:
                for column in df.columns:
                    if item.upper() in column and not '.1' in column:
                        if column not in molecules:
                            molecules.append(column)
            elif item in molecules2:
                length = len(item)
                for column in df.columns:
                    if column[-length:] == item:
                        if column not in molecules:
                            molecules.append(column)
        elif type(item) == int:
            if df.columns[item] not in molecules:
                molecules.append(df.columns[item])
        else:
            print('Only str and int datatypes are allowed in the output list')
            return  

    df.plot('Time', molecules)
    for molecule in molecules:
        plt.fill_between(df['Time'], 
                        df[molecule] - df[molecule + '.1'], 
                        df[molecule] + df[molecule + '.1'], 
                        alpha=0.2)

    plt.xlabel('Time (Seconds)')
    plt.ylabel('Average Molecule Counts')
    plt.show()
