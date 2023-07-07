#Calculation of Current Density
import numpy as np
import pandas as pd

job = 'ver16_test' #update based on your job
fname = '/projectnb/ryanlab/mmorey/lammps.sum2021/bvtest/verification/' + job

#information for input files
Nfreq = 1
totDump = 101
nfreqsecs = 0.25
time = 0
dt = 3.47222222222221e-06 #change based on simulation                                                                              

#Current dnesity parameters
e = 1.602176634*pow(10,-19) #Coulombs
N = 1 #oxidation statefor Li
avagadro = 6.02214076*pow(10,23) #avagadro's number used in converstion from mol to g
mLi = 6.941  #atomic mass of Li
Faraday = 96485
L = 5 #um

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

##Create array to hold dmM and time dmM[ionicflux,time]
##Mass is in index 9 of dump file (double check!)
##Assumes fluid mass is 0. Add one for t=0
matrix = np.zeros((totDump,3),dtype=float)


#loop through X  dumps that start at 0 (subtract t=0 from loop)
for i in range(0,totDump):
    matrix[i,1] = time
    time = time + (Nfreq*dt)
    num = i*Nfreq
    fid = fname + "/dump." + str(num) + ".dat"
    data = np.loadtxt(fid, skiprows=9, usecols=9) #Double check placement of dmM value based on your dump files!
    dmM = np.sum(data)*pow(10,-15)#conversion to g/s
    # currentdensity = (dmM*N*e*avagadro)/(mLi) #A/um^2
    currentdensity = (dmM*Faraday)/(mLi*pow(L,2))
    matrix[i,2] = currentdensity
    matrix[i,0] = num
    #print("Current Density: " + str(currentdensity) + "\n time: " + str(time) + "\n")
    print("Print Out: " + str(num) + "\n time: " + str(time) + "\n Current Density: " + str(currentdensity) + "\n")
    #print("Print Out: " + str(num) + "\n time: " + str(time) + "\n sumdmM: " + str(dmM) + "\n")
#Save currentdensity data to csv
CurrentDensityData = pd.DataFrame(matrix)
CurrentDensityData.to_csv('LR_app0.01_newcalc.currentdensity.csv',index=False) #Change Job



