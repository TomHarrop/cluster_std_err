#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='cluster_std_err',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'scikit-learn',
        'numpy',
        'pandas',
        'python-Levenshtein',
    ]
)
