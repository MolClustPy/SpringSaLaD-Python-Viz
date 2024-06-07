from molclustpy import *
from data_locator import *
from Visualization.Molclustpy_visualization_funcitons import *
import pandas as pd
from input_file_extraction import *
from time_rounder import find_nearest_time

def plot(search_directory, bins=[], time=None):

    path_list = ['data', 'Cluster_stat', 'Histograms', 'Size_Freq_Fotm', 'MEAN_Run']

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(search_directory)
    dt_data = float(split_file[0][4][9:])

    search_term = 'Size_Freq_Fotm'

    time, fotm_file = find_nearest_time(search_directory, path_list, time, dt_data, search_term)
    
    outpath = os.path.normpath(fotm_file)
    outpath = os.path.join(*outpath.split(os.sep)[:-5])

    df = pd.read_csv(fotm_file) 
    New_columns = ['Cluster size','frequency','foTM']
    df.columns = New_columns
    df.to_csv(os.path.join(outpath,'pyStat','SteadyState_distribution.csv'), index=False)

    plotClusterDistCopy(outpath, time, bins)