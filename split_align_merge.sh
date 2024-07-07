#! /bin/bash
#$ -N split_align_merge
#$ -q postgrad.q,college.q,gcec.q,pg-long.q,materials.q,pg-long.q,ug-long.q
#$ -l mem_tokens=100.0G
#$ -o /home/postgrads/2488158T/split_align_merge.out
#$ -e /home/postgrads/2488158T/split_align_merge.out
#$ -M j.tushabe.1@research.gla.ac.uk
#$ -m beas

# Ensure that the PATH includes the directory containing clustalw2
export PATH=/home/postgrads/2488158T/spack/opt/spack/linux-centos7-x86_64_v3/gcc-4.8.5/clustalw-2.1-4ew5abwo7fe3fky3cfh7exbvn4fwilvk/bin:$PATH
echo "PATH is set to: $PATH"

# Input FASTA file
input_fasta="/home/postgrads/2488158T/final_contigs.fa"
echo "Input FASTA file: $input_fasta"

# Directories
split_dir="/home/postgrads/2488158T/split_files"
aligned_dir="/home/postgrads/2488158T/aligned_files"
merged_output="/home/postgrads/2488158T/final_merged.aln"

# Create directories if they don't exist
mkdir -p $split_dir
mkdir -p $aligned_dir
echo "Directories created or already exist."

# Number of sequences per split file
chunk_size=3500  # Adjust this value based on your needs

# Function to split the FASTA file into chunks with multiple sequences
split_fasta() {
    echo "Splitting FASTA file into chunks with multiple sequences..."
    awk -v n=$chunk_size 'BEGIN {file = 1} /^>/ {if (seq++ % n == 0) {close(out); out = sprintf("'$split_dir'/seq%02d.fa", file++);} } {print > out;}' $input_fasta
}

# Function to align sequences
align_sequences() {
    local file="$1"
    echo "Aligning $file..."
    clustalw2 -INFILE=$file -OUTFILE=${aligned_dir}/$(basename ${file%.fa}).aln
}

# Function to merge alignments
merge_alignments() {
    echo "Merging aligned files..."
    find ${aligned_dir} -name "*.aln" -print0 | xargs -0 cat > $merged_output
}

# Split the input FASTA file
split_fasta

# Process each split fasta file
for file in $split_dir/*.fa; do
    align_sequences "$file"
done

# Merge all aligned files into one
merge_alignments

