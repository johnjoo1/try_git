import pandas as pd
import seaborn as sns
import glob

iris = sns.load_dataset('iris')

# what it should be
#iris.to_csv("/mnt/data/my_dataset/out/iris.csv")
# print(glob.glob('/mnt/data/my_dataset/out'))

# current directory implementation
iris.to_csv("/mnt/datasets/my_dataset/out/iris.csv")
print(glob.glob('/mnt/datasets/my_dataset/out'))