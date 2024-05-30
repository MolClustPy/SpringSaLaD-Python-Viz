path = 'Examples\R_L_test_difficult_SIMULATIONS\Simulation0_SIM.txt'

with open(path, "r") as f:
    lines = f.readlines()

for line in lines:
    if '     TYPE' in line:
        print(line)