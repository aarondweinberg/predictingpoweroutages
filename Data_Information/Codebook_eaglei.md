# **Codebook** for the eaglei Data Set

## eaglei_outages_YEAR
- **fips_code**: The FIPS code of the county in which the power outages occurred
- **county**: The county name in which the power outages occurred spelled out in text
- **state**: The state in which the power outage occurred
- **customers_out**: The total number of customers without power for that county at that timestamp. This number is always an integer. Entries with 0 customers without power are not included in this dataset.
- **run_start_time**: Date and timestamp provided in UTC in the format “MM/DD/YY 00:00”. This timestamp marks the beginning of the collection run.

## coverage_history.csv 
*includes the modeled customer coverage rate of each state from 2018–2022*
- **Year**: The date used to derive the coverage for the given year. For example, the entry “1/1/2019” means all following information in the row is based on the date of Jan 1, 2019.
- **State**: Postal Service two-character state abbreviation, for example “AL” for Alabama.
- **Total Customers**: The total number of utility customers in the state on that given date. Customers are derived from the closest EIA-861 customer number updates to the provided date.
- **Min_covered**: The minimum number of utility customers covered by EAGLE-I in a given calendar year, as reported by EIA-861
- **Max_covered**: The maximum number of utility customers covered by EAGLE-I in a given calendar year, as reported by EIA-861
- **Min_pct_covered**: The minimum percentage of coverage for the state seen in a given year
- **Max_pct_covered**: The maximum percentage of coverage for the state seen in a given year

## MCC.csv
*provides the modeled number of electric customers per county as of 2022*
- **County_FIPS**: The FIPS code for each county for which we have modelled county customers. If a FIPS code is missing from this list, we are missing information in EAGLE-I for utilities that have customers in this county.
- **Customers**: The modelled result for the number of electric utility customers living in this county


## DQI.csv
*presents our Data Quality Index and the four sub-components by year by FEMA Region for 2018–2022*
- **fema**: The Federal Emergency Management Agency (FEMA) region. (From 1-10, as shown in the map on page 8)
- **year**: calendar year
- **success_rate**: The Success Rate component of the DQI
- **percent_enabled**: The Percent Enabled component of the DQI
- **spatial_precision**: The Spatial Precision component of the DQI
- **cust_coverage**: The Customer Coverage component of the DQI
- **max_covered**: The maximum number of customers covered in this region/year.
- **total_customers**: The estimated total number of customers in this region/year
- **DQI**: the final data quality index, as defined in Eq. 1. (On page 10)