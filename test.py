import pandas as pd

path = r'Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\data\Run0\SiteIDs.csv'

file_path = 'path_to_your_file.csv'

df = pd.read_csv(path, header=None)

df.columns = ['ID', 'Sites']

data_dict = pd.Series(df['Sites'].values, index=df['ID']).to_dict()

print(data_dict[100000005])