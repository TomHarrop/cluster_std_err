#!/usr/bin/env Rscript

library(data.table)

# set the path to the compressed file
gzfile <- "jobs-dump-6mo.csv.gz"

# use fread to read the gzipped file directly into a data.table object
dt <- fread(cmd = paste0("gzip -cd ", gzfile), sep = ",", header = TRUE)

# print the first few rows of the data
head(dt)