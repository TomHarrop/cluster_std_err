#!/usr/bin/env python3

from setuptools import setup

setup(
    name='cluster_std_err',
    version='0.1',
    install_requires=[
        'nltk',
        'scikit-learn',
        'transformers',
        'Levenshtein',
        'numpy',
        'pandas',
        'torch',
    ],
)