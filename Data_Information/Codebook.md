# **Codebook**

# EAGLEI

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


# NOAA Storm Events
- BEGIN_YEARMONTH
- BEGIN_DAY
- BEGIN_TIME
- END_YEARMONTH
- END_DAY
- END_TIME
- episode_id: ID assigned by NWS to denote the storm episode; links the event details file with the
information within location file. The occurrence of storms and other significant weather phenomena having sufficient intensity to cause loss of life, injuries, significant property damage, and/or disruption to commerce. Rare, unusual, weather phenomena that generate media attention, such as snow flurries in South Florida or the San Diego coastal area; and Other significant meteorological events, such as record maximum or minimum temperatures or precipitation that occur in connection with another event.
- event_id: (Primary database key field) ID assigned by NWS to note a single, small part that goes into a specific storm episode; links the storm episode between the three files downloaded from SPC’s website
- state: The state name where the event occurred (no State ID’s are included here; State Name is spelled out in ALL CAPS)
- state_fips: A unique number (State Federal Information Processing Standard) is assigned to the county by the National Institute for Standards and Technology (NIST).
- year: Four digit year for the event in this record
- month_name: Name of the month for the event in this record (spelled out; not abbreviated)


- EVENT_TYPE
- CZ_TYPE
- CZ_FIPS
- CZ_NAME
- WFO
- BEGIN_DATE_TIME
- CZ_TIMEZONE
- END_DATE_TIME
- INJURIES_DIRECT
- INJURIES_INDIRECT
- DEATHS_DIRECT
- DEATHS_INDIRECT
- DAMAGE_PROPERTY
- DAMAGE_CROPS
- SOURCE
- MAGNITUDE
- MAGNITUDE_TYPE
- FLOOD_CAUSE
- CATEGORY
- TOR_F_SCALE
- TOR_LENGTH
- TOR_WIDTH
- TOR_OTHER_WFO
- TOR_OTHER_CZ_STATE
- TOR_OTHER_CZ_FIPS
- TOR_OTHER_CZ_NAME
- BEGIN_RANGE
- BEGIN_AZIMUTH
- BEGIN_LOCATION
- END_RANGE
- END_AZIMUTH
- END_LOCATION
- BEGIN_LAT
- BEGIN_LON
- END_LAT
- END_LON
- EPISODE_NARRATIVE
- EVENT_NARRATIVE
- DATA_SOURCE
