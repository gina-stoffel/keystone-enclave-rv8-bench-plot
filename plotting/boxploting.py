import numpy as np
import matplotlib.pyplot as plt
import csv
import os

fig1, ax1 = plt.subplots()
ax1.set_title('Box Plot')
ax1.ticklabel_format(useOffset=False)

data = {
    # "name": array of iruntime data measurements
}

for file in os.listdir('/home/gina/semester-thesis-benchmarks/keystone-enclave-rv8-bench-plot/data'):
    with open('data/'+file, newline='') as f:
        csvread = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        batch_data = list(csvread)
    
    data[str(file)] = batch_data

#print(data)
lst = (np.concatenate(data['spicy_keystone_aes.csv']), np.concatenate(data['spicy_base_aes.csv']))
ax1.boxplot(lst)

plt.setp(ax1, xticks=[1, 2], xticklabels=['aes', 'sha'])

ax1.set_xlabel('benchmark binaries')


plt.show()