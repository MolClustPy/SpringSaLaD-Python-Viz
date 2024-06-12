import numpy as np
from Visualization.ClusterCrossLinking import CrossLinkIndex
from Visualization.times_2_title import *
from data_locator import *

def plot(search_directory, times, hist=False):     
    #txtfile = r"Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\Simulation0_SIM.txt"
    #vf = r'Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\viewer_files\Simulation0_SIM_VIEW_Run2.txt'

    txtfile = data_file_finder(search_directory, [], search_term='.txt')
    vf = data_file_finder(search_directory, ['viewer_files'], run = 0)

    #ss_tps = np.arange(0.02, 0.05+0.01, 0.01)

    #AS = ["PRM", "SH3_1", "SH3_2","SH3_3","SH2","pTyr_1_2", "pTyr_3"]  # active sites

    #AS = ['sh3', 'prm']
    #AS = ['SH3', 'PRM', ]

    CLI = CrossLinkIndex(txtfile, ss_timeSeries=times)

    title_str = times_2_title(times)

    print(CLI)
    #d = cl.mapSiteToMolecule()
    #rif = ReadInputFile(txtfile)
    #print(rif.getReactiveSites())
    #print(len(cl.getActiveSiteIDs())) 
    CLI.getSI(vf) 
    CLI.getSI_stat() 
    CLI.plot_SI_stat(color='k', fs=16, xticks=None, yticks=None, hist=hist, title_str=title_str)
    #CLI.plot_SI_stat(color='c', xticks=None, yticks=None)