import pandas as pd

# Loading Data
df = pd.read_csv('cit-HepPh.txt', sep='\t', header=None, names=['node1', 'node2'])#変更前

# Get all unique nodes
unique_nodes = pd.unique(df[['node1', 'node2']].values.ravel('K'))

# Mapping unique nodes to new IDs
node_to_id = {old: new for new, old in enumerate(unique_nodes)}

# Apply mapping and change to new ID
df['node1'] = df['node1'].map(node_to_id)
df['node2'] = df['node2'].map(node_to_id)


print(df)
df_edges = df[['node1', 'node2']]

# Write DataFrame to text file (without index and header)
df_edges.to_csv('cit-HepPh.txt', sep='\t', header=False, index=False)#変更後
