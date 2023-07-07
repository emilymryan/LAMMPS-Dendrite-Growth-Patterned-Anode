##Count the number of solid particles 
##Madison Morey
##21 Apr 2021
##Submit file: load python module 

#import numpy
import numpy as np
#import pandas
import pandas as pd

job = 'varRC_5989064'
fname = '/projectnb/ryanlab/mmorey/lammps.sp2021/results/varRC_5989064'

Nfreq = 26200
totDump = 16
dumpT = 5.25e-3
time = 0

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

count = np.zeros((totDump,2),dtype=int)

for i in range(0,totDump):
    count[i,1] = time
    time = time + dumpT
    num = i*Nfreq
    fid = fname + "/dump." + str(num) + ".dat"
    d = np.loadtxt(fid, skiprows=9, usecols=1)
    count[i,0] = np.count_nonzero(d==2, axis=0)
    print(i)


countData = pd.DataFrame(count)
countData.to_csv('varRC_5989064.count.csv',index=False)
