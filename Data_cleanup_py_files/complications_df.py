import pandas as pd
import numpy as np
import csv
csvpath = "Complications and Deaths - Hospital.csv"
complications_original_df=pd.read_csv(csvpath)
del complications_original_df["Address"]
del complications_original_df["Phone Number"]
complications_df = complications_original_df.loc[complications_original_df["State"]=="CA",:]