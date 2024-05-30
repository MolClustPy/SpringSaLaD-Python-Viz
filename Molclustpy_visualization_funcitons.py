import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from numpy import array

def plotClusterDistCopy(path, sizeRange=[], time=None):
    # plotting the cluster size distribution (ACO: average cluster occupancy)
    plt.subplots(figsize=(7,4))
    df = pd.read_csv(path + '/pyStat/SteadyState_distribution.csv')
    cs, foTM = df['Cluster size'], df['foTM']
    
    if len(sizeRange) == 0:
        aco = sum(cs*foTM)
        plt.bar(cs, height=foTM, fc='grey',ec='k', label=f'ACO = {aco:.2f}')
        plt.axvline(aco, ls='dashed', lw=1.5, color='k')
        plt.xlabel('Cluster Size (molecules)')
        plt.ylabel('Fraction of total molecules')
        if time != None:
            plt.title(f'Cluster Size Distribution at {time} ms')
        else:
            plt.title(f'Cluster Size Distribution')
        plt.legend()
        plt.show()
    else:
        # sizeRange = [1,10,20]
        # clusters : 1-10, 10-20, >20
        idList = [0]
        #xbar = np.arange(1, len(sizeRange)+1, 1)
        xLab = [f'{sizeRange[i]} - {sizeRange[i+1]}' for i in range(len(sizeRange) - 1)]
        xLab.append(f'> {sizeRange[-1]}')
        
        for size in sizeRange[1:]:
            i = 0
            while cs[i] < size:
                i += 1
            if cs[i] == size:
                idList.append(i+1)
            else:
                idList.append(i)
            
        
        foTM_binned = [sum(foTM[idList[i]: idList[i+1]]) for i in range(len(idList)-1)]
        foTM_binned.append(sum(foTM[idList[-1]:]))
        
        try:
            plt.bar(xLab, foTM_binned, color='grey', ec='k')
            plt.xlabel('Cluster size range (molecules)')
            plt.ylabel('Fraction of total molecules')
            plt.ylim(0,1)
            plt.show()
        except:
            print('Invalid size range!! Maximal size range might be higher than largest cluster!')