from ete3 import Tree, TreeStyle, TextFace, NodeStyle

# Replace 'path_to_your_tree_file.ph' with the actual path to your .ph file
tree_file = 'final_merged.ph'

# Read the tree
tree = Tree(tree_file, format=1)

# Prune the tree to keep a subset of representative taxa
taxa_to_keep = [leaf.name for leaf in tree.iter_leaves()][:50]  # Keeping first 50 taxa
tree.prune(taxa_to_keep, preserve_branch_length=True)

# Collapse clades with more than a specified number of leaves
def collapse_clades(node, max_leaves=5):
    if node.is_leaf():
        return
    if len(node) > max_leaves:
        node.delete()
        collapsed_node = Tree(name=node.name)
        collapsed_node.add_face(TextFace(f"Collapsed ({len(node)} leaves)", fsize=12, fgcolor="black"), column=0, position="branch-right")
        node.add_child(collapsed_node)
    else:
        for child in node.get_children():
            collapse_clades(child, max_leaves)

collapse_clades(tree, max_leaves=10)  # Adjust the max_leaves to collapse more clades

# Create a tree style for a circular plot
ts = TreeStyle()
ts.mode = "c"  # Circular mode
ts.show_leaf_name = True
ts.title.add_face(TextFace("Circular Phylogenetic Tree", fsize=40, fgcolor="black"), column=0)
ts.show_branch_length = True
ts.branch_vertical_margin = 30  # Increase vertical margin between branches
ts.min_leaf_separation = 15  # Set minimum leaf separation

# Customize node styles
for node in tree.traverse():
    if node.is_leaf():
        name_face = TextFace(node.name, fsize=10, fgcolor="black")
        node.add_face(name_face, column=0, position="branch-right")
    else:
        node_style = NodeStyle()
        node_style["size"] = 0
        node.set_style(node_style)
    # Adjust branch length to ensure visibility
    if node.dist < 0.1:
        node.dist = 0.1

# Render the tree to a file
tree.render("circular_phylogenetic_tree_adjusted.png", tree_style=ts, w=2400, h=2400)  # Increase width and height for clarity

# Show the plot
tree.show(tree_style=ts)
