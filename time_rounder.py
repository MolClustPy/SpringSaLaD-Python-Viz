import os
from data_locator import data_file_finder

def find_nearest_time(search_directory, path_list, time, dt_data, search_term):
    if time != None:
        #Round to nearest available time based on dt_data value
        if round(time % dt_data, 6) >= dt_data/2:
            time = round(time - (time % dt_data) + dt_data, 6)
        else:
            time = round(time - (time % dt_data), 6)
        
        decimals = os.path.split(data_file_finder(search_directory, path_list, search_term))[1].split('_')[2].split('.')[1]

        time = format(float(time), f'.{len(decimals)}f')
        file = data_file_finder(search_directory, path_list, time)
    else:
        file = data_file_finder(search_directory, path_list, search_term)
        time = float(os.path.split(file)[1].split('_')[2])

    return time, file