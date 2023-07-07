#import matplotlib
#matplotlib.use('Agg')
# from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#import sys

#fname = sys.argv[1]
job = 'bv_7285631'
#fname = '/projectnb/ryanlab/tmelsh/chargingProfiles/lammpsUpdate/results/pulse/'+ job
fnamech1 = '/projectnb/ryanlab/mmorey/lammps.sum2021/results/' + job

#T = 450
Nfreq = 968
totDump = 16
dumpT = 5.25e-3
time = 0

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

##Create array to hold mass and time mass[dendrite_mass,time]
##Mass is in index 6 of dump file (double check!)
##Assumes fluid mass is 0. Add one for t=0
#mass = np.zeros((totDump+1,2),dtype=float)
mass = np.zeros((totDump,2),dtype=float)
#count = np.zeros((totDump,2),dtype=int)

#loop through 6000 dumps that start at 0 (subtract t=0 from loop)
for i in range(0,totDump):
#    count[i,1] = time
    mass[i,1] = time
    time = time + dumpT
    num = i*Nfreq
    fid = fnamech1 + "/dump." + str(num) + ".dat"
    d = np.loadtxt(fid, skiprows=9, usecols=9) #Double check!
    mass[i,0] = np.sum(d)
#    print(d)
#    count[i,0] = np.count_nonzero(d==2, axis=0)
    print(i)


#Save mass data to csv
massData = pd.DataFrame(mass)
massData.to_csv('bv_7285631.dmM.csv',index=False)
#countData = pd.DataFrame(count)
#countData.to_csv('test_2754418.count.csv',index=False)

##Plot mass growth vs. time
# plt.figure(figsize=(11,7),dpi=100);
# plt.plot(mass[:,1],mass[:,0],'r.')
# for i in my_range(0,totDump+1,100):
#     plt.plot(mass[i,1],mass[i,0],'bo',ms=3)
# plt.title('"Pulse Charging Trial 1 Dendrite Growth (mass vs. time)')
# plt.xlabel('Time (s)')
# plt.ylabel('Dendrite Mass Growth()')
# plt.axis([0, (T+1), 0, 0.002])
# plt.minorticks_on()
# plt.xticks(np.arange(0, (T+1),step=1))
# plt.grid(which='both', axis='both', linestyle='--')
#matplotlib.axes.Axes.set_axisbelow(True)


# plt.savefig( 'trial1_5098531.png', bbox_inches='tight')
