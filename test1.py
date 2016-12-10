
# coding: utf-8

# In[6]:

# the first script to read, calculate, plot data
# and save a figure to a file
#
# import libs: pandas matplotlib.pyplot sys
import pandas as pd
import matplotlib.pyplot as plt
import sys

# get_ipython().magic('matplotlib inline')

filename = sys.argv[1] #[0] reserved for script name
print(filename)
# print(sys.argv[0])

# import data with panda
human_chr21 = pd.read_csv(filename,"\t")

# calc proportions
# save into new columns in the same dataframe
human_chr21['gc_content']= human_chr21['gc_bases']/     (human_chr21['win_start']-human_chr21['win_end'])
human_chr21['gene_content']= human_chr21['exon_bases']/     (human_chr21['win_start']-human_chr21['win_end'])

# make a plot of GC vs Gene content
plt.plot(human_chr21['gene_content'],human_chr21['gc_content'],'og')
plt.xlabel('gene_content')
plt.ylabel('gc_content')
#plt.show() # creates window with the figure

# save figure to the file
plt.savefig(filename + '.plot.png')




