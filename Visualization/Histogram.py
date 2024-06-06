from molclustpy import *
from data_locator import *
from Visualization.Molclustpy_visualization_funcitons import *
import pandas as pd
from input_file_extraction import *

def plot(search_directory, bins=[], time=None):

    path_list = ['data', 'Cluster_stat', 'Histograms', 'Size_Freq_Fotm', 'MEAN_Run']

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(search_directory)
    dt_data = float(split_file[0][4][9:])

    if time != None:
        #Round to nearest available time based on dt_data value
        if time % dt_data >= dt_data/2:
            time = time - (time % dt_data) + dt_data
        else:
            time = time - (time % dt_data)
        
        decimals = os.path.split(data_file_finder(search_directory, path_list, 'Size_Freq_Fotm.csv'))[1].split('_')[2].split('.')[1]

        time = format(float(time), f'.{len(decimals)}f')
        fotm_file = data_file_finder(search_directory, path_list, time)
    else:
        fotm_file = data_file_finder(search_directory, path_list, 'Size_Freq_Fotm.csv')
        time = float(os.path.split(fotm_file)[1].split('_')[2])
    
    outpath = os.path.normpath(fotm_file)
    outpath = os.path.join(*outpath.split(os.sep)[:-5])

    df = pd.read_csv(fotm_file) 
    New_columns = ['Cluster size','frequency','foTM']
    df.columns = New_columns
    df.to_csv(os.path.join(outpath,'pyStat','SteadyState_distribution.csv'), index=False)

    plotClusterDistCopy(outpath, time, bins)