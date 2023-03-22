#!/usr/bin/env python3

from cluster_std_err import ClusteredDataFrame
import pandas as pd

df = pd.read_csv('bedtools_closestbed.csv')
df['std_err'] = df['tool_stderr']

df_clustered = ClusteredDataFrame(df)
