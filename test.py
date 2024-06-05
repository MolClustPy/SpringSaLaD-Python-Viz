from data_locator import *
from histogram import Histogram

search_directory = os.path.join('Examples','R_L_test_difficult_SIMULATIONS','Simulation0_SIM_SIMULATIONS')

path_list = ['data', 'Cluster_stat', 'Histograms', 'Size_Freq_Fotm', 'MEAN_Run']

fotm_file = data_file_finder(search_directory, path_list, f'Size_Freq_Fotm.csv')

Histogram(search_directory, bins=[], time_ms=100)