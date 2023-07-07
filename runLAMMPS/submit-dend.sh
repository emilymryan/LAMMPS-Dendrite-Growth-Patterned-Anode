#! /bin/bash -l
#$ -l h_rt=120:00:00
#$ -P ryanlab
#$ -m bea
#$ -j y
#$ -N bv
#$ -o /projectnb/ryanlab/mmorey/lammps.sum2021/interfacialresults/final/$JOB_NAME.o$JOB_ID
#$ -e /projectnb/ryanlab/mmorey/lammps.sum2021/interfacialresults/final/$JOB_NAME.e$JOB_ID
#$ -pe mpi_16_tasks_per_node 64
module load openmpi/3.1.1
module load python3/3.6.5

lmp=/projectnb/ryanlab/mmorey/mylammps/src/lmp_mpi

dname1=1um_${JOB_ID}
output=/projectnb/ryanlab/mmorey/InterfacialPaper/interfacialresults/WernerFigs/${dname1}
dname=${output}
mkdir -p ${dname}

mpirun -np $NSLOTS ${lmp} -in input_bv_heterogeo.lmp -var dname ${dname}

exit

