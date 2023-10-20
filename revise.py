import pandas as pd

#Loading Data
df = pd.read_csv('ca-HepPh(1).txt', sep='\s+', header=None, names=['node1', 'node2'])#'\s+'

#Get all unique nodes
unique_nodes = pd.unique(df[['node1', 'node2']].values.ravel('K'))

#Mapping unique nodes to new IDs
node_to_id = {old: new for new, old in enumerate(unique_nodes)}

# Apply mapping to new ID
df['node1'] = df['node1'].map(node_to_id)
df['node2'] = df['node2'].map(node_to_id)

# Remove opposite direction of same edge
df['min_node'] = df[['node1', 'node2']].min(axis=1)
df['max_node'] = df[['node1', 'node2']].max(axis=1)
df = df.drop_duplicates(subset=['min_node', 'max_node'], keep='first')
df = df.drop(columns=['min_node', 'max_node'])


print(df)

## Write DataFrame to text file (without index and header)
df.to_csv('ca-HepPh_revise.txt', sep='\t', header=False, index=False)
