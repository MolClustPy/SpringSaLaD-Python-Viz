import os
import subprocess

path = r'C:\Users\cpero\Downloads\SpringSaLaD-Python-Viz\Executable\langevin-windows-latest.exe'
model = 'Executable\output\Simulation0_SIM.txt'
model_path = os.path.abspath(model)

raw_s = r'{}'.format(model_path)

subprocess.run([path, 'simulate', raw_s, '1'])