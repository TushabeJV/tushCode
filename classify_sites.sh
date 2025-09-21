#!/bin/bash
#SBATCH --job-name=classify_sites
#SBATCH --output=classify_sites_%j.log
#SBATCH --error=classify_sites_%j.err
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

# Master output directory
mkdir -p kraken2_results_individual_sites

# Loop through each fasta file in current directory
for fasta in combined_contigs_*.fa; do
    sample=$(basename "$fasta" .fa)

    # Make a subfolder for this sample
    sample_dir=kraken2_results_individual_sites/$sample
    mkdir -p "$sample_dir"
    
    kraken2 \
    --db ../../kraken_db \
    --output ${sample_dir}/${sample}_kraken2_output.txt \
    --report ${sample_dir}/${sample}_kraken2_report.txt \
    --classified-out ${sample_dir}/${sample}_classified.fa \
    --unclassified-out ${sample_dir}/${sample}_unclassified.fa \
    --threads 32 \
    --confidence 0.5 \
    "$fasta"

       echo "[$(date)] Finished $sample."

done

echo "All samples processed!"
