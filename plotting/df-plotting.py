import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import glob
from matplotlib.patches import Polygon
import pandas as pd

benchmark_tests = ('aes', 'dhrystone', 'norx', 'primes', 'qsort', 'sha512')
#benchmark_tests = ["sha512"]
data_dir = '/home/gina/semester-thesis-benchmarks/keystone-enclave-rv8-bench-plot/data'
bench_names = ('vanilla_base', 'spicy_base', 'vanilla_keystone', 'spicy_keystone')
# bench_names = ('vanilla_base', 'spicy_base' )

df1 = pd.DataFrame(columns=['rv8-benchmarks', 'Env', 'Measurements'])
df = pd.DataFrame(columns=[ 'rv8-benchmarks', 'vanilla_base', 'spicy_base', 'vanilla_keystone', 'spicy_keystone'])

for test in benchmark_tests:
    d_temp = { 'rv8-benchmarks' : test }

    # iterate over all kinds of measurements
    for bench in bench_names:
        df_temp = pd.read_csv(data_dir+'/'+bench+'_'+test+'.csv', sep='\t', dtype=np.int, header=None)
        df1 = df1.append({'rv8-benchmarks': test, 'Env': bench, 'Measurements': np.median(df_temp.values) }, ignore_index=True)
        d_temp.update({ bench: np.median(df_temp.values) } )
    
    df = df.append(d_temp, ignore_index=True)

df = df.set_index('rv8-benchmarks')


ax = df.plot.bar( rot=0, color={ 'vanilla_base': 'gold', 'spicy_base' : 'khaki', 'vanilla_keystone' : 'darkolivegreen', 'spicy_keystone': 'darkkhaki' } )
ax.legend( ['ref. native', 'prop. native', 'ref. keystone', 'prop. keystone'] )

ax.set_ylabel('latency [cycles]')



plt.show()
