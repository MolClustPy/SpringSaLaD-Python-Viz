from input_file_extraction import *
import os
from ClusTopology_ss import ClusterDensity
from DataPy import *

def spatial_analysis(path, times=[]):
    last_item = os.path.split(path)[1][:-12] + '_FOLDER'
    specific_path  = os.path.join(path, last_item)

    _,split_file = read_input_file(specific_path)
    total_time = float(split_file[0][1].split(' ')[2])
    dt_data = float(split_file[0][4].split(' ')[1])
    count = int(total_time/dt_data)

    input_file = find_txt_file(specific_path)

    if times==[]:
        times = [0]
        for i in range(int(count) + 1):
            times.append(i*dt_data)
        times.pop(0)
    else:
        pass

    cd = ClusterDensity(input_file, ss_timeSeries=times)
    cd.getCD_stat(cs_thresh=1)