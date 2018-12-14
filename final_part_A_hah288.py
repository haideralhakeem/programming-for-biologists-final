import pandas as pd
import numpy as np

import warnings # Ignores warnings from seaborn
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt

tetrahymena = pd.read_table('tetrahymena.tsv')
tetrahymena = tetrahymena[tetrahymena.diameter >= 19.2]
tetrahymena = tetrahymena[tetrahymena.diameter <= 26.0]
tetrahymena_means = tetrahymena.groupby(['culture','glucose'],as_index=False).agg({'conc':'mean','diameter':'mean'})

