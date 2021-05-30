import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import glob
from matplotlib.patches import Polygon
import pandas as pd

# benchmark_tests = ('aes', 'dhrystone', 'norx', 'primes', 'qsort', 'sha512')
benchmark_tests = ["sha512"]
data_dir = '/home/gina/semester-thesis-benchmarks/keystone-enclave-rv8-bench-plot/data'
bench_names = ('vanilla_base', 'spicy_base', 'vanilla_keystone', 'spicy_keystone')

df = pd.DataFrame(columns=['Binary', 'Env', 'Measurements'])

for test in benchmark_tests:
    print(test)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
    #fig, ax1 = plt.subplots(figsize=(10, 10))
    plt.title(test)
    
    # iterate over all kinds of measurements
    for bench in bench_names:
        # with open(data_dir+'/'+bench+'_'+test+'.csv', newline='') as f:
        #     csvread = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        #     batch_data = np.concatenate(list(csvread))
        
        df2 = pd.read_csv(data_dir+'/'+bench+'_'+test+'.csv', sep='\t', dtype=np.int, header=None)
        df = df.append({'Binary': test, 'Env': bench, 'Measurements': np.concatenate(df2.values)}, ignore_index=True)
        

    # bp = ax1.boxplot(df['Measurements'], notch=0, sym='+', vert=1, whis=1.5)
    # plt.setp(bp['boxes'], color='black')
    # plt.setp(bp['whiskers'], color='black')
    # plt.setp(bp['fliers'], color='red', marker='+')
    #ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
    #            alpha=0.5)
    #ax1.set(
    #    axisbelow=True,  # Hide the grid behind plot objects
    #    title='RV8 benchmarks',
    #    ylabel='latency [cycles]',
    #)
    #ax1.set_xticklabels( df['Env'] ,
    #                    rotation=45, fontsize=8)

    plt.boxplot(df['Measurements'])

    ax.set_xticks([1,2,3,4])
    ax.set_xticklabels(df['Env'])

    plt.plot()


plt.show()