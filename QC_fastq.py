import os
import glob
import subprocess


fastqc_path = "fastqc"  #path to fastqc"

# Directory containing FASTQ files
input_dir = "fastq_42"

# Output directory for FastQC reports
output_dir = "fastqc_reports"
os.makedirs(output_dir, exist_ok=True)  # Create output dir if it doesn't exist

# Find all R1 files
r1_files = glob.glob(os.path.join(input_dir, "*_R1_*.fastq.gz"))

for r1 in r1_files:
    # Derive R2 filename from R1 filename
    r2 = r1.replace("_R1_", "_R2_")  # Adjust if naming differs

    # Check if R2 file exists
    if os.path.exists(r2):
        sample_name = os.path.basename(r1).split("_R1_")[0]
        print(f"Running FastQC on sample {sample_name} (R1 and R2)...")

        # Run FastQC on both files
        subprocess.run([
            fastqc_path,
            r1,
            r2,
            "--outdir", output_dir,
            "--threads", "4"
        ])
    else:
        print(f"Warning: R2 file for {r1} not found. Skipping.")

print("FastQC analysis completed for all samples.")