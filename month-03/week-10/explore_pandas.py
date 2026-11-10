import pandas as pd

pop = pd.read_csv("data/raw/streams_data.csv")

print(pop.head())
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
print(pop[""])