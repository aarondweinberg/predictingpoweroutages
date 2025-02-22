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
- begin_time: Time storm event began (24 hour time)
- END_YEARMONTH
- END_DAY
- end_time: Time that storm event ended (24 hour time)
- episode_id: ID assigned by NWS to denote the storm episode; links the event details file with the information within location file. The occurrence of storms and other significant weather phenomena having sufficient intensity to cause loss of life, injuries, significant property damage, and/or disruption to commerce. Rare, unusual, weather phenomena that generate media attention, such as snow flurries in South Florida or the San Diego coastal area; and Other significant meteorological events, such as record maximum or minimum temperatures or precipitation that occur in connection with another event.
- event_id: (Primary database key field) ID assigned by NWS to note a single, small part that goes into a specific storm episode; links the storm episode between the three files downloaded from SPC’s website
- state: The state name where the event occurred (no State ID’s are included here; State Name is spelled out in ALL CAPS)
- state_fips: A unique number (State Federal Information Processing Standard) is assigned to the county by the National Institute for Standards and Technology (NIST).
- year: Four digit year for the event in this record
- month_name: Name of the month for the event in this record (spelled out; not abbreviated)
- EVENT_TYPE: The only events permitted in Storm Data are listed in Table 1 of Section 2.1.1 of NWS Directive 10-1605 at http://www.nws.noaa.gov/directives/sym/pd01016005curr.pdf. The chosen event name should be the one that most accurately describes the meteorological event leading to fatalities, injuries, damage, etc. However, significant events, such as tornadoes, having no impact or causing no damage, should also be included in Storm Data.
- cz_type: Indicates whether the event happened in a (C) county/parish, (Z) zone or (M) marine
- cz_fips: The county FIPS number is a unique number assigned to the county by the National Institute for Standards and Technology (NIST) or NWS Forecast Zone Number (See addendum)
- cz_name: County/Parish, Zone or Marine Name assigned to the county FIPS number or NWS Forecast Zone
- wfo: National Weather Service Forecast Office’s area of responsibility (County Warning Area) in which the event occurred)
- begin_date_time: Date and time that storm event began (MM/DD/YYYY 24 hour time AM/PM)
- cz_timezone: Time Zone for the County/Parish, Zone or Marine Name (Eastern Standard Time (EST), Central Standard Time (CST), Mountain Standard Time (MST), etc.
- end_date_time: Date and time that storm event ended (MM/DD/YYYY 24 hour time AM/PM)
- injuries_direct: The number of injuries directly related to the weather event
- injuries_indirect: The number of injuries indirectly related to the weather event
- deaths_direct: The number of deaths directly related to the weather event.
- deaths_indirect: The number of deaths indirectly related to the weather event
- damage_property: The estimated amount of damage to property incurred by the weather event. (e.g. 10.00K = $10,000; 10.00M = $10,000,000)
- damage_crops: The estimated amount of damage to crops incurred by the weather event (e.g. 10.00K = $10,000; 10.00M = $10,000,000)
- source: Source reporting the weather event
- magnitude: measured extent of the magnitude type ~ only used for wind speeds and hail size (e.g. 0.75” of hail; 60 mph winds)
- magnitude_type: EG = Wind Estimated Gust; ES = Estimated Sustained Wind; MS = Measured Sustained Wind; MG = Measured Wind Gust (no magnitude is included for instances of hail)
- flood_cause: Reported or estimated cause of the flood
- category: Unknown (During the time of downloading this particular file, NCDC has never seen anything provided within this field.)
- tor_f_scale: Enhanced Fujita Scale describes the strength of the tornado based on the amount and type of damage caused by the tornado. The F-scale of damage will vary in the destruction area; therefore, the highest value of the F-scale is recorded for each event.
  - EF0 – Light Damage (40 – 72 mph)
  - EF1 – Moderate Damage (73 – 112 mph)
  - EF2 – Significant damage (113 – 157 mph)
  - EF3 – Severe Damage (158 – 206 mph)
  - EF4 – Devastating Damage (207 – 260 mph)
  - EF5 – Incredible Damage (261 – 318 mph)
- tor_length: Length of the tornado or tornado segment while on the ground (minimal of tenths of miles)
- tor_width: Width of the tornado or tornado segment while on the ground (in feet)
- tor_other_wfo: Indicates the continuation of a tornado segment as it crossed from one National Weather Service Forecast Office to another. The subsequent WFO identifier is provided within this field.
- tor_other_cz_state: The two character representation for the state name of the continuing tornado segment as it crossed from one county or zone to another. The subsequent 2-Letter State ID is provided within this field.
- tor_other_cz_fips: The FIPS number of the county entered by the continuing tornado segment as it crossed from one county to another. The subsequent FIPS number is provided within this field.
- tor_other_cz_name: The FIPS name of the county entered by the continuing tornado segment as it crossed from one county to another. The subsequent county or zone name is provided within this field in ALL CAPS.
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
