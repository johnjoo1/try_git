import pandas as pd

# what it should be
#df = pd.read_csv('/mnt/data/my_dataset/us-counties.csv')

# current directory implementation
df = pd.read_csv('/mnt/datasets/my_dataset/latest/iris.csv')

print(df.head())