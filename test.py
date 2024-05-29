from molclustpy import *
from data_locator import *
import pandas as pd

path = r'Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS'

fotm_file, file_name = find_cluster_fotm(path)

df = pd.read_csv(fotm_file) 
New_columns = ['Cluster size','frequency','foTM']
df.columns = New_columns

print(df)

df.to_csv(path + r'\data\pyStat\SteadyState_distribution.csv', index=False)

#Remember to rename the columns, file name, and add it to pyStat
#Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_FOLDER\data\Cluster_stat\Histograms\Size_Freq_Fotm\MEAN_Run\MEAN_Run_0.500_Size_Freq_Fotm.csv
outpath = path + '\data'

plotClusterDist(outpath)