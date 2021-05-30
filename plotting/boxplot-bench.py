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
# bench_names = ('vanilla_base', 'spicy_base' )

df = pd.DataFrame(columns=['Binary', 'Env', 'Measurements'])

for test in benchmark_tests:
    print(test)

    # ax0: base runs    ax1: keystone runs
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 7))
    fig.suptitle(test, fontsize=12)

    # iterate over all kinds of measurements
    for bench in bench_names:
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


    ax0.ticklabel_format(useOffset=False)
    bp0 = ax0.boxplot(df['Measurements'][:2], showfliers=True)
    plt.setp(bp0['boxes'], color='#D7191C')
    plt.setp(bp0['whiskers'], color='#D7191C')
    plt.setp(bp0['caps'], color='#D7191C')
    plt.setp(bp0['medians'], color='#D7191C')

    ax0.set_xticks([1,2])
    ax0.set_xticklabels(['reference', 'proposal'], fontsize=12)
    ax0.set_title('Run as plain binary')
    ax0.set_ylabel('latency [cycles]')

    ax1.ticklabel_format(useOffset=False)
    bp1 = ax1.boxplot(df['Measurements'][2:4], showfliers=True)
    plt.setp(bp1['boxes'], color='#2C7BB6')
    plt.setp(bp1['whiskers'], color='#2C7BB6')
    plt.setp(bp1['caps'], color='#2C7BB6')
    plt.setp(bp1['medians'], color='#2C7BB6')

    ax1.set_xticks([1,2])
    ax1.set_xticklabels(['reference', 'proposal'], fontsize=12)
    ax1.set_title('Run as Keystone enclave')
    ax1.set_ylabel('latency [cycles]')
    
    plt.plot()

plt.show()