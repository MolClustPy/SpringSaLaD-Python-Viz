import numpy as np
from Visualization.ClusterCrossLinking import CrossLinkIndex

def plot():     
    txtfile = r"Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\Simulation0_SIM.txt"

    vf = r'Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\viewer_files\Simulation0_SIM_VIEW_Run0.txt'

    ss_tps = np.arange(0.02, 0.05+0.01, 0.01)

    AS = ["PRM", "SH3_1", "SH3_2","SH3_3","SH2","pTyr_1_2", "pTyr_3"]  # active sites

    #AS = ['sh3', 'prm']
    #AS = ['SH3', 'PRM', ]

    CLI = CrossLinkIndex(txtfile, ss_timeSeries=ss_tps, activeSites=AS)

    print(CLI)
    #d = cl.mapSiteToMolecule()
    #rif = ReadInputFile(txtfile)
    #print(rif.getReactiveSites())
    #print(len(cl.getActiveSiteIDs())) 
    CLI.getSI(vf) 
    CLI.getSI_stat() 
    #CLI.plot_SI_stat(color='k', fs=16, xticks=None, yticks=None) 
    #CLI.plot_SI_stat(color='c', xticks=None, yticks=None)

def hello():
    print('Hello')