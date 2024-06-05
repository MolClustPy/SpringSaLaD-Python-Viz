from molclustpy import *
from data_locator import *
import matplotlib.pyplot as plt
from Molclustpy_visualization_funcitons import *
import pandas as pd
from input_file_extraction import *

def Histogram(search_directory, bins=[], time_ms=0):

    path_list = ['data', 'Cluster_stat', 'Histograms', 'Size_Freq_Fotm', 'MEAN_Run']

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(search_directory)
    dt_data = 1000*float(split_file[0][4][9:])

    if time_ms % dt_data >= dt_data/2:
        time_ms = time_ms - (time_ms % dt_data) + dt_data
    else:
        time_ms = time_ms - (time_ms % dt_data)

    print(search_directory)
    print(path_list)

    if time_ms != None:
        time_s = format(float(time_ms/1000), '.3f')
        fotm_file = data_file_finder(search_directory, path_list, f'MEAN_Run_{time_s}_Size_Freq_Fotm.csv')
    else:
        fotm_file = data_file_finder(search_directory, path_list, f'Size_Freq_Fotm.csv')

    print(fotm_file)
    
    outpath = os.path.normpath(fotm_file)
    outpath = os.path.join(*outpath.split(os.sep)[:-5])

    df = pd.read_csv(fotm_file) 
    New_columns = ['Cluster size','frequency','foTM']
    df.columns = New_columns
    df.to_csv(os.path.join(outpath,'pyStat','SteadyState_distribution.csv'), index=False)

    plotClusterDistCopy(outpath, bins, time_ms)