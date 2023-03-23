#!/usr/bin/env python3

from cluster_std_err import ClusteredDataFrame
import pandas as pd

df = pd.read_csv('bedtools_closestbed.csv')
df_clustered = ClusteredDataFrame(df)

sorted_df = df_clustered.sort_values(by='cluster_id')
sorted_df.to_csv('bedtools_closestbed_sorted.csv')

# count and summarize the clusters
cluster_summary = df_clustered.get_cluster_summary()
print(cluster_summary)
cluster_summary.to_csv('bedtools_cluster_summary.csv')

