#!/bin/bash
#SBATCH --job-name=classify_combined
#SBATCH --output=classify_combined_%j.log
#SBATCH --error=classify_combined_%j.err
#SBATCH --partition=standard
#SBATCH --mem=150G
#SBATCH --cpus-per-task=32
#SBATCH --time=500:00:00

# Environment setup
export LANGUAGE=en_GB.UTF-8
export LC_ALL=en_GB.UTF-8
export LC_CTYPE=en_GB.UTF-8
export LANG=en_GB.UTF-8

# Activate conda environment
source /home/postgrads/2488158T/miniconda3/bin/activate myenv

# Define Threads
THREADS=$SLURM_CPUS_PER_TASK

# Classify combined  schools


kraken2 \
--db ../kraken_db --output kraken2_output.txt --report kraken2_report.txt --classified-out kraken2_classified.fa --unclassified-out kraken2_unclassified.fa --threads 32 --confidence 0.5  megahit_combined/all_21_final.contigs.fa
