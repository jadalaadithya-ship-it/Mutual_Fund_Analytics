import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n" + "="*70)
        print("FILE:", file)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDTYPES:")
        print(df.dtypes)

        print("\nHEAD:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())