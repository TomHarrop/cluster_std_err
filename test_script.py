#!/usr/bin/env python3

from cluster_std_err import ClusteredDataFrame
import pandas as pd

antismash = pd.read_csv('antismash.csv')
antismash['std_err'] = antismash['job_stderr']

ClusteredDataFrame(antismash)
