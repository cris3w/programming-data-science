import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# Look pretty...
matplotlib.style.use('ggplot')


# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
seeds_dataset = pd.read_csv('Datasets/wheat.data')
print seeds_dataset.head(5), '\n'


# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
# .. your code here ..
slice1 = seeds_dataset[['area', 'perimeter']]


# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
# .. your code here ..
slice2 = seeds_dataset[['groove', 'asymmetry']]


# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..
slice1.plot.hist(alpha=0.75)
slice2.plot.hist(alpha=0.75)

plt.show()
