
"""
HIT137 Assignment 2 - Question 2
Australian Weather Stations Temperature Analysis


This program analyzes temperature data of multiple Australian weather stations from the 'temperature_data' folder across different years.
It performs the following tasks:
1. Calculates average temperatures for each season across all years
2. Identifies stations with the largest temperature range
3. Determines the warmest and coolest stations

Output files:
- average_temp.txt: Contains seasonal average temperatures
- largest_temp_range_station.txt: Lists stations with the largest temperature variation
- warmest_and_coolest_station.txt: Details about the warmest and coolest stations
"""
# import required modules
import os
import re
import pandas as pd

# define directory containing temperature data CSV files
data_directory = 'temperature_data' 

# Define pattern for matching CSV files
file_pattern = r"stations_group_\d{4}\.csv"  

# Get list of all files in the directory
all_files = os.listdir(data_directory)

# Filter for CSV files matching our pattern
csv_files = [file for file in all_files if re.match(file_pattern, file)]

# Read and combine all CSV files into a single dataframe
dfs = []
for file in csv_files:
    file_path = os.path.join(data_directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)

print(df_all.head())

# Define seasons and their corresponding months
seasons = {
    'Spring': ['September', 'October', 'November'],
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August']
}

# calculate seasonal averages
def calculate_seasonal_avg(df, seasons):
    seasonal_avg = {}
    for season, months in seasons.items():
        seasonal_avg[season] = df[months].mean(axis=1)  
    return seasonal_avg

seasonal_avg_all = calculate_seasonal_avg(df_all, seasons)

for season, avg_temps in seasonal_avg_all.items():
    df_all[season] = avg_temps

seasonal_avg_across_years = {season: df_all[season].mean() for season in seasonal_avg_all.keys()}

# Save seasonal averages to file
with open('average_temp.txt', 'w') as f:
    for season, avg_temp in seasonal_avg_across_years.items():
        f.write(f"{season} Average Temperature: {avg_temp:.2f}°C\n")
        
# Calculate and identify stations with largest temperature range
df_all['Temp_Range'] = df_all.iloc[:, 4:16].max(axis=1) - df_all.iloc[:, 4:16].min(axis=1)
largest_temp_range_station = df_all.loc[df_all['Temp_Range'] == df_all['Temp_Range'].max()]

# Save stations with largest temperature range to file
with open('largest_temp_range_station.txt', 'w') as f:
    f.write("Station(s) with largest temperature range:\n")
    for _, row in largest_temp_range_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Temperature Range: {row['Temp_Range']:.2f}°C)\n")

# Calculate maximum and minimum temperatures for each station
df_all['Max_Temperature'] = df_all.iloc[:, 4:16].max(axis=1)
df_all['Min_Temperature'] = df_all.iloc[:, 4:16].min(axis=1)

warmest_station = df_all.loc[df_all['Max_Temperature'] == df_all['Max_Temperature'].max()]
coolest_station = df_all.loc[df_all['Min_Temperature'] == df_all['Min_Temperature'].min()]

# Save warmest and coolest stations to file
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest Station(s):\n")
    for _, row in warmest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Max Temperature: {row['Max_Temperature']:.2f}°C)\n")
    
    f.write("\nCoolest Station(s):\n")
    for _, row in coolest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Min Temperature: {row['Min_Temperature']:.2f}°C)\n")