import pandas as pd
import numpy as np
import csv
csvpath = "Timely and Effective Care - Hospital.csv"
timely_care_original_df=pd.read_csv(csvpath,encoding="latin-1")
del timely_care_original_df["Address"]
del timely_care_original_df["Phone Number"]
timely_care_df = timely_care_original_df.loc[timely_care_original_df["State"]=="CA",:]