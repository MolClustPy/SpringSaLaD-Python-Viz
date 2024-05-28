output_columns = ['Apples', 'Bananas', 'Oranges']

stdev_list = [x + '.1' for x in output_columns]
stdev_list.insert(0,'Time')

print(stdev_list)