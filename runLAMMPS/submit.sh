#! /bin/bash -l
#$ -l h_rt=120:00:00
#$ -P ryanlab
#$ -m bea
#$ -j y
#$ -N bv
#$ -o /projectnb/ryanlab/mmorey/LAMMPS_BATTERY_STRESS/results/final/$JOB_NAME.o$JOB_ID
#$ -e /projectnb/ryanlab/mmorey/LAMMPS_BATTERY_STRESS/results/final/$JOB_NAME.e$JOB_ID
#$ -pe mpi_16_tasks_per_node 64
module load openmpi/3.1.1
module load python3/3.6.5

lmp=/projectnb/ryanlab/mmorey/mylammps/src/lmp_mpi

dname1=6um_${JOB_ID}
output=/projectnb/ryanlab/mmorey/InterfacialPaper/interfacialresults/ECSFIGS/${dname1}
dname=${output}
mkdir -p ${dname}

mpirun -np $NSLOTS ${lmp} -in input_bv.lmp -var dname ${dname}

exit

