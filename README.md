## Standard error clustering rough-up

### Install from github (use a venv)

```python
pip install git+https://github.com/TomHarrop/cluster_std_err.git
```

### Basic usage

```python
from cluster_std_err import ClusteredDataFrame
import pandas as pd

# csv dumped from the galaxy job database
df = pd.read_csv('bedtools_closestbed.csv')

# cluster messages in the `tool_stderr` column
df_clustered = ClusteredDataFrame(df)

# count errrors and get a representative error
cluster_summary = df_clustered.get_cluster_summary()
print(cluster_summary)
```