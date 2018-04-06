This folder contains initial cleaned data.

Hospital Ratings file cleanup:

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
    Resulting Hospital Rating data set _*(Hospital Ratings.csv)*_ : 
        Renamed the column names from Original HCAHPS Measure ID to layman readable terms
        Also changed the data type of the ratings to int (Integer) [by default they are all strings]
