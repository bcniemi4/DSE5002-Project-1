# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:25:46 2025

@author: techi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import plotnine as p9 

infile="Project 01\\r project data-1-1_Test.csv"

DS_hire_df=pd.read_csv(infile)
DS_hire_df.head()