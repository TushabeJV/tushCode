from Bio import SeqIO
import csv

def extract_fasta_sequences(fasta_file):
    fasta_sequences = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences

def extract_clustalw_sequences(clustalw_file):
    clustalw_sequences = {}
    with open(clustalw_file, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith("CLUSTAL") and not line.startswith(" "):
                parts = line.split()
                for part in parts:
                    if part.startswith("k101_"):  # Adjust based on actual ID format
                        internal_id = part
                        # Assuming sequence data follows the ID
                        sequence = next(part for part in parts if not part.startswith("k101_"))
                        clustalw_sequences[internal_id] = sequence
    return clustalw_sequences

def create_id_mapping(fasta_file, clustalw_file):
    fasta_sequences = extract_fasta_sequences(fasta_file)
    clustalw_sequences = extract_clustalw_sequences(clustalw_file)

    mapping = {}

    for clustal_id, clustal_seq in clustalw_sequences.items():
        for fasta_id, fasta_seq in fasta_sequences.items():
            if clustal_seq == fasta_seq:
                mapping[clustal_id] = fasta_id
                break

    return mapping

def save_mapping_to_csv(mapping, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ClustalW2_ID", "FASTA_ID"])
        for clustal_id, fasta_id in mapping.items():
            writer.writerow([clustal_id, fasta_id])

# define input and output
fasta_file = 'final_contigs.fa'
clustalw_file = 'final_merged.aln'
output_mapping_file = 'id_mapping.csv'

id_mapping = create_id_mapping(fasta_file, clustalw_file)
save_mapping_to_csv(id_mapping, output_mapping_file)

print(f"ID Mapping saved to {output_mapping_file}")
