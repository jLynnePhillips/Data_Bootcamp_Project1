#### This folder contains the analysis of data to answer the research questions for this project.

#### Fine Tune the Dataset :
    Jupyter Notebook Reference : Fine Tune Data Set.ipynb
    Goal : Merge the "Hospital Ratings" data with "County_Income_df" data
    Result : A final merged data set "Final_Merged_Data_Set.csv"

#### Analysis :
    Jupyter Notebook Reference :
        1. HCAHPS_Data_Analysis.ipynb
            Analysis to answer :
                a. The maximum "Overall HCAHPS Score" per County
                b. Impact of Household Income on Overall Hospital Rating, if any.
                c. Impact of Population on Overall Hospital Rating, if any.
                d. Misc : Distribution of a HCAHPS score (at a glance)
            Visualizations derived :
                a. MaxRating_perCounty.png
                b. Ratings_Income_ScatterPlot.png
                c. Rating_Population_ScatterPlot.png
                d. BoxPlot_HCAHPS.png
        2. Hospital Rating Analysis - Naz.ipynb
            Analysis to answer :
                a. Correlation between the different rating categories
                b. Correlation between Hospital Ownerships and Hospital Ratings
            Visualizations derived :
                a. Correlation_Graphs.png
                b. HospitalType_Rating_BoxPlot.png
        3.  Hospital ownership - new boxplot.ipynb
            Analysis to answer :
                a. Revisit Correlation between Hospital Ownerships and Hospital Ratings taking into consideration the number of hospitals per Ownersip Type.
                (Per question during presentation on do we know how many hospitals are there per Ownership Type in the data set.)
            Visualizations derived :
                a. HospitalType_Rating_BoxPlot_New.png
