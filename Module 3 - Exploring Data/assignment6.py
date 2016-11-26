import pandas as pd
import matplotlib.pyplot as plt


# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
seeds_dataset = pd.read_csv('Datasets/wheat.data')
print seeds_dataset.head(5), '\n'


# TODO: Drop the 'id' feature
# 
# .. your code here ..
seeds_dataset = seeds_dataset.drop(labels='id', axis='columns')
print seeds_dataset.head(5), '\n'


# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
print seeds_dataset.corr(), '\n'


# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(seeds_dataset.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(seeds_dataset.columns))]
plt.xticks(tick_marks, seeds_dataset.columns, rotation='vertical')
plt.yticks(tick_marks, seeds_dataset.columns)

plt.show()
