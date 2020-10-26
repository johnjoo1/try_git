'''
This script testing writing files back to the working directory /mnt/code when executed as a Job.
'''

import pandas as pd
import seaborn as sns
import glob

iris = sns.load_dataset('iris')

iris.to_csv("iris.csv")
print(glob.glob('*'))
