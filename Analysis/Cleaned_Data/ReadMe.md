
#### This folder contains the cleaned up data sets ready for to be used for final analysis.

#### Hospital Ratings file cleanup:

    Original File =  HCAHPS-CA-Hospital.xlsx
    Deleted following columns :
    "ZIP Code","Phone Number", and all 'Foot Notes'
        "Patient Survey Star Rating Footnote",
        "HCAHPS Answer Percent Footnote",
        "Number of Completed Surveys Footnote",
        "HCAHPS Answer Percent","HCAHPS Linear Mean Value",
        "Survey Response Rate Percent Footnote","Measure Start Date", "Measure End Date"
    Dropped all Data with 
        Patient Survey Star Rating  as 'Not Available' and 'Not Applicable'
    Pivoted the table so:
        HCAHPS Measure ID are columns and their respective Patient Survey Star Rating as values
    Resulting Hospital Rating data set (Cleaned data set name : "Hospital Ratings.csv")
        Renamed the column names from Original HCAHPS Measure ID to layman readable terms
        Also changed the data type of the ratings to int (Integer) [by default they are all strings]

    *** Jupyter Notebook Reference : Hospital Rating Cleanup - Naz.ipynb ***

#### Hospital General Information Data Set Clean up:

    Original File = Hospital General Information.csv
    Deleted following columns :
        "Emergency Services",
        "Meets criteria for meaningful use of EHRs",
        "Hospital overall rating",
        "Hospital overall rating footnote",
        "Mortality national comparison","Mortality national comparison footnote",
        "Safety of care national comparison","Safety of care national comparison footnote",
        "Readmission national comparison","Readmission national comparison footnote",
        "Patient experience national comparison","Patient experience national comparison footnote",
        "Effectiveness of care national comparison","Effectiveness of care national comparison footnote",
        "Timeliness of care national comparison","Timeliness of care national comparison footnote",
        "Efficient use of medical imaging national comparison",
        "Efficient use of medical imaging national comparison footnote"
    Resulted in Hospital Type Ownership info data set:
        Cleaned Data Set Name: Hospital Type Ownership info.csv
        Columns in cleaned data set:
            Provider ID,
            Hospital Name,
            Address,City,State,ZIP Code,
            County Name,Phone Number,
            Hospital Type,Hospital Ownership
        
        *** Jupyter Notebook Reference : HospitalGeneralInformation.ipynb ***

#### County Rankings File cleanup:

    Original File = 2016 County Health Rankings California Data - v3.xls
    This workbook had wide range of data in separate sheets.
    For our project we used the income and health data sheets from the workbook.
    Major Obstacles:
        Data sets had 2 -fold column names where each column had sub columns and the sub column names are duplicates
    Resulting Data Sets:
        county_health_df.csv
            Years of Potential Life Lost Rate,
            # Uninsured,% Uninsured,# Primary Care Physicians,
            # Mental Health Providers,# Medicare Enrollees,Preventable Hosp. Rate,
            Graduation Rate,# Some College,% Some College,# Unemployed,% Unemployed,
            # Children in Poverty,% Children in Poverty,80th Percentile Income,
            20th Percentile Income,Income Ratio,# Single-Parent Households,% Single-Parent Households,
            # Violent Crimes,Violent Crime Rate,# Households with Severe Problems,% Severe Housing Problems
        County_income_df.csv
            County,# Premature Deaths,# Child Deaths,# Infant Deaths,# Limited Access,
            % Limited Access,# Uninsured Adults,# Uninsured Children,% Uninsured Adults,
            % Uninsured Children,Household Income,# Not Proficient in English,
            % Not Proficient in English,Population
    For our final analysis we ended up using only the County_income_df.csv data set.

    *** Jupyter Notebook Reference : ca_health_county.ipynb ***


#### Merging of data sets:

    We wanted to have one data set with HCAHPS Scores for each hospital, along with Hospital Type.
        This was accomplished by merging :
            Hospital Ratings.csv and  Hospital Type Ownership info.csv
    Outcome :- Hospital Ratings Merged.csv 

    *** Jupuyter Notebook Reference : Hospital Ratings_Type Merged.ipynb ***
