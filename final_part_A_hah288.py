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

plot = sns.FacetGrid(tetrahymena_means, hue="glucose", size=5, hue_order=["glucose_yes", "glucose_no"], hue_kws=dict(marker=["o", "s"])) \
   .map(plt.scatter, "diameter", "conc") \
   .add_legend()
plt.title("Nonlog Concentration versus Diameter")
plt.show()
plot.savefig('final_part_A_nonlog_hah288.pdf')

