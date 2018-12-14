"""The following script extracts data from the file 'tetrahymena.tsv', filters it, provides the mean values for replicated data, plots, and saves 
nonlog and log concentration versus diameter plots. This script was written on the editor Emacs. """


import pandas as pd
import numpy as np
import pdb

import warnings # Ignores warnings from seaborn
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
tetrahymena = pd.read_table('tetrahymena.tsv') # Reads in the data from tetrahymena.tsv

tetrahymena = tetrahymena[tetrahymena.diameter >= 19.2] # Filters out small cells with diameter less than 19.2 by only keeping data for cells with diameter greater than 19.2
tetrahymena = tetrahymena[tetrahymena.diameter <= 26.0] # Filters out large cells with diameter greater than 26.0 by only keeping data for cells with diameter less than 26.0
tetrahymena_means = tetrahymena.groupby(['culture','glucose'],as_index=False).agg({'conc':'mean','diameter':'mean'})
# Merges the data by combining rows that have the same 'culture' value
# When merged, the 'conc' values for both replicates are combined by finding the mean between them
# This also occurs for the diameter

plot = sns.FacetGrid(tetrahymena_means, hue="glucose", size=5, hue_order=["glucose_yes", "glucose_no"], hue_kws=dict(marker=["o", "s"])) \
   .map(plt.scatter, "diameter", "conc") \
   .add_legend()
# Creates a scatterplot with a legend using data from 'tetrahymena_means'
# The color of the points changes based on the values in the 'glucose' column. This is done using the 'hue=' argument
# The order of the hues is listed and corresponds to the hue_kws which gives each value a different marker shape
# "o" gives circle markers, "s" gives square markers
# The figure is plotted placing "diameter" on the x-axis and "conc" on the y-axis


plt.title("Nonlog Concentration versus Diameter") # Adds a title to the figure
plt.show() # Displays the figure
plot.savefig('final_part_A_nonlog_hah288.pdf') # Saves the figure


tetrahymena_means['log_concentration'] = np.log(tetrahymena_means['conc'])
# Computes the natural log of all values in the 'conc' column and adds them to a new column labelled 'log_concentration'
tetrahymena_means['log_diameter'] = np.log(tetrahymena_means['diameter'])
# Computes the natural log of all values in the 'diameter' column and adds them to a new column labelled 'log_concentration'


#pdb.set_trace()


plot = sns.FacetGrid(tetrahymena_means, hue="glucose", size=5, hue_order=["glucose_yes", "glucose_no"], hue_kws=dict(marker=["o", "s"])) \
   .map(plt.scatter, "log_diameter", "log_concentration") \
   .add_legend()
# Creates a second scatterplot with a legend using data from 'tetrahymena_means' with the new columns added
# This figure is similar to the first, except it creates the scatterplot using the "log_diameter" for the x-axis and "log_concentration" for the y-axis

plt.title("Log Concentration versus Diameter") # Adds a title to the figure
plt.show() # Displays the figure
plot.savefig('final_part_A_log_hah288.pdf') # Saves the figure
