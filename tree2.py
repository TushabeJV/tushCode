import pandas as pd
from ete3 import Tree, TreeStyle, TextFace, NodeStyle

# Step 1: Load the species data
species_df = pd.read_csv('seqID_species_taxoID.txt', delimiter='\t', header=None)
species_df.columns = ['seqIDs', 'Taxon_ID', 'Species_Name']

# Convert the DataFrame to a dictionary for fast lookup
species_dict = pd.Series(species_df.Species_Name.values, index=species_df.seqIDs).to_dict()

# Step 2: Read and process the tree
tree_file = 'final_merged.ph'
tree = Tree(tree_file, format=1)

# Update leaf names with species names
for leaf in tree.iter_leaves():
    if leaf.name in species_dict:
        # Replace the leaf name with the species name
        leaf.name = species_dict[leaf.name]

# Step 3: Customize and render the tree
ts = TreeStyle()
ts.mode = "c"  # Circular mode
ts.show_leaf_name = True  # Show the updated leaf names (species names)
ts.title.add_face(TextFace("Circular Phylogenetic Tree with Species Names", fsize=24, fgcolor="black"), column=0)

# Render the tree to a file with increased dimensions
tree.render("circular_phylogenetic_tree_with_species_names.png", tree_style=ts, w=2400, h=2400)

# Optionally show the plot
tree.show(tree_style=ts)
