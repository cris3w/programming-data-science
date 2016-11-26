import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves


matplotlib.style.use('ggplot')


seeds_dataset = pd.read_csv('Datasets/wheat.data')

seeds_dataset1 = seeds_dataset.drop(labels=['id', 'area', 'perimeter'], axis='columns')
seeds_dataset2 = seeds_dataset.drop(labels='id', axis='columns')


plt.figure()
andrews_curves(seeds_dataset1, 'wheat_type')
plt.show()


plt.figure()
andrews_curves(seeds_dataset2, 'wheat_type')
plt.show()
