import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
import seaborn as sns
from statsmodels.tsa.stattools import grangercausalitytests, ccf
import numpy as np
import plotly.express as px
from datetime import datetime
import geopandas as gpd
import warnings
import utils
import pickle
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=RuntimeWarning)

def make_ts_power_county(fips_code,
                  start_year,
                  start_month,
                  start_day,
                  end_year,
                  end_month,
                  end_day,
                  data_directory = './data/eaglei_data'):
    """
    Generate a time series dataframe of power outages for a specific county within a given date range.

    This function reads yearly CSV files containing power outage data, filters the data for a specified county,
    aggregates the number of customers without power, and returns a time series dataframe for the specified date range.

    Parameters:
    fips_code (int): fips code of county for which to generate the time series data.
    start_year (int): The starting year of the date range.
    start_month (int): The starting month of the date range.
    start_day (int): The starting day of the date range.
    end_year (int): The ending year of the date range.
    end_month (int): The ending month of the date range.
    end_day (int): The ending day of the date range.
    data_directory (str, optional): The directory containing the CSV files. Default is './data/eaglei_data'.

    Returns:
    pd.DataFrame: A dataframe with a datetime index ('time') and a column 'customers_out' representing the number of customers without power.

    Raises:
    FileNotFoundError: If any of the CSV files for the specified years do not exist in the data directory.
    """
    
    df_list = []
    for year in range(start_year, end_year + 1):
        # Construct the filename
        file_name = f"eaglei_outages_{year}.csv"
        file_path = os.path.join(data_directory, file_name)
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_name} does not exist in the directory {data_directory}.")
    
        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)
        df['run_start_time'] = pd.to_datetime(df['run_start_time'])
        df.dropna(subset=['customers_out'],inplace=True)
        
#        df_state = df[df['state']==state].copy(deep=True)
        df_county = df[df['fips_code']==fips_code].copy(deep=True)
        df_county_ts_cus = df_county.groupby('run_start_time')['customers_out'].sum().reset_index()
        df_county_ts_cus.drop(df_county_ts_cus.index[-1], inplace=True)
        df_county_ts_cus.set_index('run_start_time', inplace=True)
        df_county_ts_cus.rename_axis('time', inplace=True)
    
        
        # Append the dataframe to the list
        df_list.append(df_county_ts_cus)
    
    # Concatenate all dataframes in the list into a single dataframe
    concat_df = pd.concat(df_list, ignore_index=False)
    start_date = pd.Timestamp(year=start_year, month=start_month, day=start_day)
    end_date = pd.Timestamp(year=end_year, month=end_month, day=end_day+1)
    # Slice the dataframe
    df_county_ts_power = concat_df.loc[start_date:end_date].copy(deep=True)
    df_county_ts_power.drop(df_county_ts_power.index[-1], inplace=True)

    return df_county_ts_power


def make_ts_events_county(fips_code, event_types, start_year, start_month, start_day, end_year, end_month, end_day, df):
    """
    Construct a DataFrame with 15-minute intervals indicating event occurrence.
   
    Parameters:
    - df (pd.DataFrame): The NOAA StormEvent database, with fips code added
    - fips_code (int): fips code of county of interest
    - event_types (list): The event types to filter (e.g., ["Winter Storm", "Hurricane"]).
    - start_year (int): The start year for the new DataFrame.
    - start_month (int): The start month for the new DataFrame.
    - start_day (int): The start day for the new DataFrame.
    - end_year (int): The end year for the new DataFrame.
    - end_month (int): The end month for the new DataFrame.
    - end_day (int): The end day for the new DataFrame.
   
    Returns:
    - pd.DataFrame: A DataFrame with 15-minute intervals and event counts.
    """
    # Generate the time range for the new DataFrame
    start_date = datetime(start_year, start_month, start_day)
    end_date = datetime(end_year, end_month, end_day, 23, 45)  # Include the last time interval
    time_index = pd.date_range(start=start_date, end=end_date, freq='15min')
   
    # Create the new DataFrame with 15-minute intervals
    new_df = pd.DataFrame({'time': time_index})
    
    # Initialize event count columns for each event type
    for event_type in event_types:
        new_df[f'event_count {event_type}'] = 0  # Initialize event counts to 0
   
    # Convert BEGIN and END times into datetime objects
    df['BEGIN_DATETIME'] = pd.to_datetime(
        df['BEGIN_YEARMONTH'].astype(str) + df['BEGIN_DAY'].astype(str).str.zfill(2) +
        df['BEGIN_TIME'].astype(str).str.zfill(4), format='%Y%m%d%H%M'
    )
    df['END_DATETIME'] = pd.to_datetime(
        df['END_YEARMONTH'].astype(str) + df['END_DAY'].astype(str).str.zfill(2) +
        df['END_TIME'].astype(str).str.zfill(4), format='%Y%m%d%H%M'
    )
    
    # Filter the NOAA data for the specified county and event type
    filtered_df = df[
        (df['FIPS'] == fips_code) & 
        (df['EVENT_TYPE'].isin(event_types)) & 
        (df['END_DATETIME'] >= start_date) & 
        (df['BEGIN_DATETIME'] <= end_date)
    ].copy(deep=True)
   
    # Iterate through the events and assign them to the closest time interval in the new DataFrame
    for event_type in event_types:
        event_subset = filtered_df[filtered_df['EVENT_TYPE']==event_type]
        
        for _, row in event_subset.iterrows():
            event_start = row['BEGIN_DATETIME']
            event_end = row['END_DATETIME']
       
            # Round the start and end times to the nearest 15-minute interval
            event_start_rounded = event_start.round('15min')
            event_end_rounded = event_end.round('15min')
       
            # Find the indices in the new DataFrame for the rounded times
            start_idx = new_df['time'].searchsorted(event_start_rounded)
            end_idx = new_df['time'].searchsorted(event_end_rounded)
       
            # Increment the event count for the affected time intervals
            if start_idx < len(new_df) and end_idx <= len(new_df):
                new_df.loc[start_idx:end_idx, f'event_count {event_type}'] += 1
   
    # Add YEAR, MONTH, DAY columns
    new_df['YEAR'] = new_df['time'].dt.year
    new_df['MONTH'] = new_df['time'].dt.month
    new_df['DAY'] = new_df['time'].dt.day
    
    # Re-order the columns to make sure the YEAR, MONTH, DAY, time start first
    cols_order = ['YEAR', 'MONTH', 'DAY', 'time'] + [col for col in new_df.columns if col not in ['YEAR', 'MONTH', 'DAY', 'time']]
    new_df = new_df[cols_order]

    
    # Return the new_df
    return new_df

def combine_agg_ts_county(fips_code,
                   start_year,
                   start_month,
                   start_day,
                   end_year,
                   end_month,
                   end_day,
                   data_directory_power = './data/eaglei_data',
                   data_directory_events = './data/NOAA_StormEvents'):
    """
    Combine and aggregate time series data of power outages and weather events for a specific county within a given date range.

    This function generates time series data for power outages and weather events, aggregates them by hour and day,
    and merges the aggregated data into two combined dataframes.

    Parameters:
    fips_code (int): fips code of county for which to generate the time series data.
    start_year (int): The starting year of the date range.
    start_month (int): The starting month of the date range.
    start_day (int): The starting day of the date range.
    end_year (int): The ending year of the date range.
    end_month (int): The ending month of the date range.
    end_day (int): The ending day of the date range.
    data_directory_power (str, optional): The directory containing the power outage CSV files. Default is './eaglei_data'.
    data_directory_events (str, optional): The directory containing the weather events CSV files. Default is './NOAA_StormEvents'.

    Returns:
    tuple: Two dataframes - the first aggregated by hour and the second aggregated by day, both containing combined time series data of power outages and weather events.

    Raises:
    FileNotFoundError: If any of the required CSV files do not exist in the specified directories.
    """

    df_county_ts_power = make_ts_power_county(fips_code = fips_code,
                                      start_year = start_year,
                                      start_month = start_month,
                                      start_day = start_day,
                                      end_year = end_year,
                                      end_month = end_month,
                                      end_day = end_day,
                                      data_directory = data_directory_power)
    
    df_county_ts_power_hr = utils.aggregate_ts(df_county_ts_power, 'hour')
    df_county_ts_power_day = utils.aggregate_ts(df_county_ts_power, 'day')
    
    
    
    df_events = pd.read_csv(os.path.join(data_directory_events, "StormEvents_2014_2024_fips.csv"))
   # print('fips_code:',fips_code)
   #
   # print('df_events[FIPS]:',df_events['FIPS'])
    df_county_events=df_events[df_events['FIPS']==fips_code].copy(deep=True)
    event_types_county = list(df_county_events['EVENT_TYPE'].unique())
    
    df_county_ts_events = make_ts_events_county(fips_code = fips_code,
                                        event_types= event_types_county,
                                        start_year = start_year,
                                        start_month = start_month,
                                        start_day = start_day,
                                        end_year = end_year,
                                        end_month = end_month,
                                        end_day = end_day,
                                        df=df_events)
    
    
    df_county_ts_events['time'] = pd.to_datetime(df_county_ts_events['time'])
    df_county_ts_events.set_index('time', inplace=True)
    df_county_ts_events.drop(columns=['YEAR', 'DAY', 'MONTH'], inplace=True)

    df_county_ts_events_hr = utils.aggregate_ts(df_county_ts_events, 'hour')
    df_county_ts_events_day = utils.aggregate_ts(df_county_ts_events, 'day')

    df_county_ts_comb_hr = pd.merge(df_county_ts_events_hr, df_county_ts_power_hr, left_index=True, right_index=True)
    df_county_ts_comb_day = pd.merge(df_county_ts_events_day, df_county_ts_power_day, left_index=True, right_index=True)
    
    return df_county_ts_comb_hr, df_county_ts_comb_day

def make_data_chunks(days_per_chunk = 7, days_per_X = 5, days_per_y = 2, df_state_ts_comb_hr, start_year, end_year):
    """
    Chunk dataset into training samples of several days and save to pickle.

    Parameters:
    days_per_chunk (int): numer of days per data chunk
    days_per_X (int): number of days in the chunk to be used as predictors
    days_per_y (int): number of days in the chunk to be used as target
    df_state_ts_comb_hr (pandas dataframe): dataframe of aggregated hourly weather event data
    start_year (int): The starting year used to create the dataframe
    end_year (int): The starting year used to create the dataframe
    outpath (str): directory to save chunked data to
    Returns:
    None
    Raises:
    FileNotFoundError: if the output directory doesn't exist
    """

    hrs_per_chunk = 24*days_per_chunk
    hrs_per_X_chunk = 24*days_per_X

    # create chunked data
    n_chunks = int(len(df_state_ts_comb_hr)/hrs_per_chunk)
    chunked_X = np.zeros([hrs_per_X_chunk, len(df_state_ts_comb_hr.columns) - 1, n_chunks])*np.nan
    chunked_y = np.zeros([hrs_per_chunk - hrs_per_X_chunk, 1, n_chunks])*np.nan
    for i in range(n_chunks):
        chunk = df_state_ts_comb_hr.iloc[i*hrs_per_chunk:(i+1)*hrs_per_chunk,:]
        X = chunk.iloc[:hrs_per_X_chunk,:].drop(columns=['customers_out'])
        y = chunk.iloc[hrs_per_X_chunk:,:]['customers_out']
        chunked_X[:,:,i] = X 
        chunked_y[:,:,i] = np.array(y).reshape(-1,1)
    
    # save chunked data
    if not os.path.isdir(outpath):
        raise FileNotFoundError(outpath + ' does not exist.')
    out_file = open(outpath + '/X_chunked_'+str(start_year)+'_'+str(end_year)+'.pkl', 'ab')
    pickle.dump(chunked_X, out_file)
    out_file.close()
    out_file = open(outpath + '/y_chunked_'+str(start_year)+'_'+str(end_year)+'.pkl', 'ab')
    pickle.dump(chunked_y, out_file)
    out_file.close()
    
    return
       