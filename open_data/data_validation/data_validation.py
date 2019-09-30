# 02D - Data Validation

# Rule 01: Identify all rows with invalid county
valid_county = ['LA' 'ALA' 'SD' 'SCL' 'ORA' 'SON' 'SM' 'RIV' 'CC' 'VEN' 'SBD' 'SF' 'SAC'
 'SOL' 'SCR' 'MRN' 'YOL' 'FRE' 'SB' 'MON' 'SJ' 'PLA' 'KER' 'YUB' 'SLO'
 'STA' 'MAD' 'TUL' 'NAP' 'SBT' 'NEV' 'ED' 'TUO' 'BUT' 'MER' 'SUT' 'MAR']
df_county = df.loc[~df['County'].isin(valid_county)]

# Write results to output CSV file
df_county.to_csv('results/01_county_2017.csv')

# Rule 02: Identify all rows with annual VMT > 20M
df_annual_vmt = df.loc[df['Annual_VMT'] > 20000000]

# Write results to output CSV file
df_annual_vmt.to_csv('results/02_annual_vmt_2017.csv')

# Rule 03: Identify all rows with invalid vhd rank
df_vhd_rank = df.loc[df['VHD_Rank'] > 200]

# Write results to output CSV file
df_vhd_rank.to_csv('results/03_vhd_rank_2017.csv')

# Rule 04: Identify all rows with incident count > 200k
df_incident_count = df.loc[df['Incident_Count'] > 200000]

# Write results to output CSV file
df_incident_count.to_csv('results/04_incident_count_2017.csv')

# Rule 05: Identify all rows with incidents per day > 100
df_incidents_daily = df.loc[df['Incidents_Per_Day'] > 100]

# Write results to output CSV file
df_incidents_daily.to_csv('results/05_incidents_daily_2017.csv')

# Rule 06: Identify all rows with incidents per day < 0
df_incidents_daily_0 = df.loc[df['Incidents_Per_Day'] < 0]

# Write results to output CSV file
df_incidents_daily_0.to_csv('results/06_incidents_daily_2017.csv')

# Rule 07: Identify null values

# Identify all rows which contain any null values
df.isnull().any(axis=1)
df_null = df[df.isnull().any(axis=1)]

# Write results to output CSV file
df_null.to_csv('results/07_null_values_fy1819.csv')

# Rule 08: Detect non-conforming character from row values
df_route_name = df['Route'].str.contains('^\x0A\x0D\x20-\x7E')

# Write results to output CSV file
df['Route'].to_csv('results/08a_route_2017.csv')
df_route_name.to_csv('results/08b_route_name_2017.csv')

# Rule 09: Identify all duplicate rows
df_duplicates = df[df.duplicated()]
df_duplicates.to_csv('results/09_duplicate_rows_fy1819.csv')
