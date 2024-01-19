import pandas as pd

data_source = "misingvalue.csv"

df = pd.read_csv(data_source, delimiter = ';')

print(df)

print(df.isna().sum())
