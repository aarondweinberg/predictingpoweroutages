# Predicting Power Outages

**Project Overview**:
Predicting Power Outages is based on a challenge posed by the ThinkOnward organization (https://thinkonward.com/app/c/challenges/dynamic-rhythms) with the goal of predicting power outages from extreme, rare weather events such as storms. Our goal is to develop a model which can accurately forecast power outages which will be useful to first responders, power companies, individuals, and businesses.

**Description of Dataset**:
Two datasets were provided as part of the challenge. First, a dataset of power outage information consisting of the number of people without power per county in the US between 2014 and 2023, reported every 15 minutes. Second, a NOAA dataset of storm events consisting of the start time, end time, location and narrative information of storm events between 2014 and 2024. We may also choose to draw from additional datasets, such as the ERA5 meteorological database.

**Stakeholders**:
According to ThinkOnward, predicting power outages is of interest to utility companies, emergency responders and hospitals, regulatory bodies, businesses, insurance companies, and the general public. Benefits of predict outages include:
- Enhancing public safety by enabling individuals, hospitals, emergency responders, and vulnerable populations to improve emergency response and prepare for loss of power
- Supporting faster power restoration by allowing utilities to minimize damage to infrastructure and use their repair crews more efficiently
- Reducing economic loss by allowing businesses and people to either implement backup solutions or take steps to preemptively mitigate damages related to power loss
- Preventing grid overload and failures by allowing utilities to preemptively adjust demand-response programs

**Key Performance Indicators**:
We will be responsible for developing custom metrics and evaluation scripts. Our goal is to evaluate our model primarily based on the extent to which it can predict whether an outage will occur and where an outage will occur. However, we also intend to measure how early we can make reliable predictions and our model’s ability to predict the severity and duration of the outages. Some metrics might include classifying rare events (e.g., precision-recall for imbalanced data), lead-time accuracy (e.g., mean time-to-event error), severity predictions (e.g., error in forecasted duration), and location accuracy. There could also be some KPIs related to the needs of businesses, such as the model’s ability to predict system resilience or costs associated with the outage.
