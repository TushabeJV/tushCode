# viewing fastq stats

import subprocess

#defining input file in output directory

input_files = ["Fastq/BO4_S1_L001_R1_001.fastq", "Fastq/BO4_S1_L001_R2_001.fastq", "Fastq/B05_S0_L001_R1_001.fastq", "Fastq/B05_S0_L001_R2_001.fastq",
              "Fastq/G03_S3_L001_R1_001.fastq", "Fastq/G03_S3_L001_R2_001.fastq", "Fastq/G11_S4_L001_R1_001.fastq", "Fastq/G11_S4_L001_R2_001.fastq" ]
output_dir = "Fastq"

# run fastqc using suprocess

for input_file in input_files:
    subprocess.run(f"fastqc {input_file} -o {output_dir}", shell=True)