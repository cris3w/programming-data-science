import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates


# Look pretty...
matplotlib.style.use('ggplot')


# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
seeds_dataset = pd.read_csv('Datasets/wheat.data')
print seeds_dataset.head(5), '\n'


# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..
seeds_dataset = seeds_dataset.drop(labels=['id', 'area', 'perimeter'], axis='columns')
print seeds_dataset.head(5), '\n'


# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
plt.figure()
parallel_coordinates(seeds_dataset, 'wheat_type', alpha=0.4)
plt.show()
