import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]
print df, '\n'


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
df.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'PPG', 'PPA', 'SHG', 'SHA']
print df, '\n'


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(thresh=(len(df.columns)-4), axis='index')
print df, '\n'


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df.PLAYER != 'PLAYER']
print df, '\n'


# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'], axis='columns')
print df, '\n'


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)
print df, '\n'


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
print df.dtypes
df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
print df.dtypes


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print 'The number of rows in the dataframe is: %s' % len(df)
print 'There are', len(df.PCT.unique()), 'unique values in the PCT column'
print 'The addition of GP[15] and GP[16] is: %s' % (df.GP[15] + df.GP[16])
