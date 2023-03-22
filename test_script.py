#!/usr/bin/env python3

from cluster_std_err import ClusteredDataFrame
import pandas as pd

df = pd.read_csv('bedtools_closestbed.csv')
df['std_err'] = df['tool_stderr']

df_clustered = ClusteredDataFrame(df)

# check out some rows
df_clustered[df_clustered['levenshtein_cluster_id'] == 3]['tool_stderr']

df_clustered[df_clustered['jaccard_cluster_id'] == 3]['tool_stderr']

sorted_df = df_clustered.sort_values(by='levenshtein_cluster_id')
sorted_df.to_csv('bedtools_closestbed_sorted.csv')
