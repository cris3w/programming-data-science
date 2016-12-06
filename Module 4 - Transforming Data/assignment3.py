import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper


matplotlib.style.use('ggplot')


scaleFeatures = False


df = pd.read_csv('./Datasets/kidney_disease.csv')

labels = ['red' if i=='ckd' else 'green' for i in df.classification]

df.drop(labels=['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'], axis='columns', inplace=True)


print df.dtypes, '\n'
df.pcv = pd.to_numeric(df.pcv, errors='coerce')
df.wc = pd.to_numeric(df.wc, errors='coerce')
df.rc = pd.to_numeric(df.rc, errors='coerce')

df.dropna(axis='index', how='any', inplace=True)
print df.dtypes, '\n'
print df, '\n'


print "This is the variance: \n", df.var(), '\n'
print "This is describe output: \n", df.describe(), '\n'


if scaleFeatures: df = helper.scaleFeatures(df)


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(df)
T = pca.transform (df)


ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()
