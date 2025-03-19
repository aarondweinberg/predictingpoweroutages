# Running Description of Anna's Work so Far

I have focused on taking the most straightforward approuch to our data using what was provided in the challenge, as a baseline that we can build on if we have time using more sources of data or different data aggregation. 

**Data Cleaning/Prep**:\
Using the provided notebook to aggregate the weather events and power outages datasets, I then did the following preprocessing steps:
1) Sort the timeseries, z-score normalize features (weather event counts), omit Nan and zero feature (for now, could try to impute later), train-test split
2) Create a function to get approximation fips county code for weather events based on start location latitude and longitude, and create new weather event file with fips code as an addtional column. Thus could allow us to do the next steps at the county, rather than state, level.
3) Create function to chunk the timeseries data into chunks of N_hours_X + N_hours_y, where N_days_X is the number of hours in a given chunk to train on, and N_hours_y is the next set of hours that we want to predict on and test against. 

**Data Visualization**:
1) Plot timeseries for each feature (weather event counts)
2) Calculate and plot correlations (Pearson's R) for each feature for a given state or county. Doesn't seem like there is that great of a correlation.
3) Calculate and plot the best lags that produce the highest correlation between each feature and the target (`customers_out`).

**Model Exploration**:
1) Attempted Varimax model (supposed to be good for multivariate timeseries) with little success.
2) Currenlty working on Neural Network which should allow us to take into account temporal (and potentially spatial) correlations in the data.
