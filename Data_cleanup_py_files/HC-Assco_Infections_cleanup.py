import pandas as pd
HealthCare_Infections = pd.read_csv("Healthcare Associated Infections - Hospital.csv")
HealthCare_Infections.drop(['Address', 'City', 'ZIP Code', 'Phone Number'], axis = 1)
HealthCare_Infections_CA = HealthCare_Infections[HealthCare_Infections["State"] == "CA"]


