# -*- coding: utf-8 -*-
"""MYP 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgYBp2yfQIAyWWrEYdndqk6siz8Rugdf
"""

import numpy as np

n = 25
p = 0.3

std_dev = np.sqrt(n * p * (1 - p))

print("Standard deviation of the binomial distribution:", std_dev)