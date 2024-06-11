import os
from Visualization.DataPy import *
from data_locator import *
from input_file_extraction import read_input_file
from Timer import Timer

search_directory = os.path.join('Examples','Nephrin-Nck-NWasp','Final_version_test_SIMULATIONS', 'Simulation0_SIM_SIMULATIONS')
input_file = find_txt_file(search_directory)

stopwatch = Timer()

stopwatch.start()
molecules, _= read_input_file(search_directory)
stopwatch.stop()

stopwatch.start()
obj = ReadInputFile(input_file)
molNames, molCounts = obj.getMolecules()
stopwatch.stop()