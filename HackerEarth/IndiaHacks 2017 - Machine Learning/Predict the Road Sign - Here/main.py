import pandas as pd
from sklearn.ensemble import RandomForestClassifier
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
print train.head()
