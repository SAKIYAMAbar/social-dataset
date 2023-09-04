import pandas as pd

# データの読み込み
df = pd.read_csv('cit-HepPh.txt', sep='\t', header=None, names=['node1', 'node2'])#変更前

# すべてのユニークなノードを取得
unique_nodes = pd.unique(df[['node1', 'node2']].values.ravel('K'))

# ユニークなノードを新しいIDにマッピング
node_to_id = {old: new for new, old in enumerate(unique_nodes)}

# マッピングを適用して新しいIDに変更
df['node1'] = df['node1'].map(node_to_id)
df['node2'] = df['node2'].map(node_to_id)

# 結果の表示
print(df)
df_edges = df[['node1', 'node2']]

# DataFrameをテキストファイルに書き込む（インデックスとヘッダーなし）
df_edges.to_csv('cit-HepPh.txt', sep='\t', header=False, index=False)#変更後
