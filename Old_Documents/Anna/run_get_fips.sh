#!/usr/bin/bash

#SBATCH --account=ucb338_asc3
#SBATCH --ntasks=96
#SBATCH --ntasks-per-node=32
#SBATCH --nodes=3
#SBATCH --time=2:00:00
#SBATCH --job-name=get_fips
#SBATCH --partition=amilan
#SBATCH --output=get_fips.%j.out
#SBATCH --constraint=ib
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Anna.Zuckerman@colorado.edu

# activate conda environment
source activate base
conda activate erdos_spring_2025

# run the file
python ./get_fips_from_lat_lon.py