# Sacramento Homelessness Data Analysis

![hmis](https://github.com/walteryu/code4sac/blob/master/images/hmis_boxplot.png)

## Code for Sacramento - Spring 2020

This project focuses on Sacramento homelessness case management data analysis; objectives are as follows:

1. Exploratory data analysis
2. Date/time analysis
3. Data visualizations
4. Identify trends
5. Forecasts/predictions

## Implementation
This project uses Jupyter Notebook with Python for data analysis; notebook contains
instructions for running analysis and provides an introduction on data science.

1. Dataset is loaded and analysis begins starting on Section 2
2. Each section contains explanation followed by code/analysis
3. Analysis progresses from data cleaning, summary statistics and visualization

## Assumptions
1. Start/end date are based on client enrollment and exit data fields
2. Client ID is unique, so same individually is not recorded multiple times
3. Time enrolled in services is outcome of interest

## Data Exploration Ideas
1. Compare with Sacramento 311 or 911 data?
2. How or when do clients drop off once enrolled into services?
3. What are some factors which affect enrollment/exit duration?

## Data Portals
1. [Shelter Listings - Sacramento](https://www.shelterlistings.org/city/sacramento-ca.html)
2. [Sac 211 - Homelessness](http://www.211sacramento.org/211/online-database/categories/homeless/)
3. [Sac County Open Data - 311 Service Calls](https://data.cityofsacramento.org/datasets/08794a6695b3483f889e9bef122517e9_0)
4. [Sac County Open Data - 911 Service Calls]((https://data.cityofsacramento.org/datasets/396e0bc72dcd4b038206f4a7239792bb_0)
5. [HUD Open Data Portal](https://www.huduser.gov/portal/datasets/pdrdatas.html)

## TODO
1. Create additional plots
2. Identify variables which affect total time enrolled in services
3. Create time series to evaluate case management life cycle
4. Evaluate data quality and determine whether fit for machine learning
5. If fit for use, then create predictions once variables are identified

## Data Schema
Data schema is listed below:

1. Dataset contains six tables, each connected via personal_id field
2. Each table contains data on a single entity, e.g. clients, projects, etc.
3. Dataset follows traditional relational schema since it is extracted from RDBMS
4. Clients table is main table and connect to others via personal_id
5. Services table is the largest since it is a one-to-many with clients

## Data Cleaning
Cleaning was performed per steps below:

1. Column names were renamed across all tables with lower-case and underscore convention for consistency, i.e. like_this_column_name
2. Column name data types were manually converted to plain text, numeric and date types since RDBMS/Excel export resulted in formatted data types.
3. Columns with date values were converted to datetime type; original data contained typos, so they were suppressed to null values during conversion.

## Table Joins
Data tables were joined for analysis as follows:

1. Clients-Enrollments: client_enrollments
2. Clients-Enrollments-Exits: enrollments_exits
3. Enrollments-Services: enrollments_services

## Known Issues
1. Since data was manually entered, it contains some typos/errors
2. Some columns contain mostly null values, so may not be as useful for Analysis
3. Columns names and data types converted during  cleaning which varies from original data

## Filenames
Original data was extracted from an existing case management system, and files were
renamed as listed below for use within Jupyter Notebook:

1. "Sacramento_County_-_Assessment_Table_2019-09-05T0401_pTq3TT" > "assessments"
2. "Sacramento_County_-_Client_Table_2019-09-05T0101_Kky8n7" > "clients"
3. "Sacramento_County_-_Enrollment_Table_2019-09-05T0131_KptDcM" > "enrollments"
4. "Sacramento_County_-_Exit_Table_2019-09-01T0601_FDwNWs" > "exits"
5. "Sacramento_County_-_Project_Table_2019-09-05T0200_DdZb5N" > "projects"
6. "Sacramento_County_-_Service_Table_2019-09-05T0301_HZ8K2P" > "services"

## Citations
Source data and visualization examples are located here:

1. [Github Source Data Repo](https://github.com/code4sac/sacramento-county-homeless-hmis-data)
2. [Chicago](https://allchicago.org/dashboard-to-end-homelessness)
3. [Seattle](http://allhomekc.org/data-overview/)

Original README: "This is a first publishing of data from Sacramento Steps Forward data on the Sacramento Regional Homeless population and continuum of Care for dates from approximately 2011 through Fall of 2019."
