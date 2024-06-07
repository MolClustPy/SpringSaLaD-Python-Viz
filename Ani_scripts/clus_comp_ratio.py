# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:06:15 2021

@author: achattaraj
"""

from glob import glob
import numpy as np
from numpy import log10, mean, log2, array
import matplotlib.pyplot as plt
import json
import re
from mpl_toolkits.axes_grid1 import make_axes_locatable


font = {'family' : 'Arial',
        'size'   : 16}

plt.rc('font', **font)

def getIndicies(n):
    idx = [1]
    for i in range(n-1):
        idx.append(idx[-1]+3)
    return idx


def getData(path, thresh=1):
    cs, comp, freqList = [], [], []
    with open (path + '/pyStat/Cluster_stat/Clusters_composition.txt', 'r') as tf:
        for line in tf.readlines()[1:]:
            if not line == '\n':
                line02 = line.split()
                if float(line02[0]) > thresh:
                    comp_count = len(re.findall("%", line))
                    if comp_count == 1:
                        freq = float(line02[-1].replace('%',''))
                        freqList.append(freq)
                        ratio = line02[1]
                        a,b = ratio.split(',')
                        cs.append(float(line02[0]))
                        comp.append(float(a)/float(b))
                    else:
                        print(line02)
                        idx = getIndicies(comp_count)
                        for i in idx:
                            ratio = line02[i]
                            freq = float(line02[i+2].replace('%',''))
                            freqList.append(freq)
                            a,b = ratio.split(',')
                            cs.append(float(line02[0]))
                            comp.append(float(a)/float(b))
    return array(cs), array(comp), array(freqList)
                     
                    
           
path = 'Z:/Springsalad/sims/SH3_PRM_weakBinding_count_40_40_SIM_FOLDER'
#title = 'A5, B5 = 100, 100 #'
cs, comp, freq = getData(path)
non_zero_idx = np.where(comp != 0)
cs = cs[non_zero_idx]
comp = comp[non_zero_idx]
freq = freq[non_zero_idx]/100

import matplotlib 
fig, ax = plt.subplots(figsize=(6,4))

cm = matplotlib.colormaps.get_cmap('rainbow')
scat = ax.scatter(cs, log2(comp), c=freq, s=20, cmap=cm)
m_comp = np.mean(comp[cs>1])

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.1)
cbar = fig.colorbar(scat, cax=cax, orientation='vertical')
#cbar.set_ticks([0.02, 0.04, 0.06, 0.08, 0.01, 0.12, 0.14, 0.16])
ax.set_yticks([-1,0,1], labels=['0.5','1','2'])

ax.set_xlabel('Cluster Size (molecules)')
ax.set_ylabel('Composition (SH3 : PRM)')
cbar.ax.set_ylabel('Frequency', rotation=270, labelpad=16)
#comp = 1/comp





