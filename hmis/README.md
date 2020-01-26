# Sacramento Homelessness Data Analysis

## Code for Sacramento - Spring 2020

Data analysis of Sacramento homelessness case management; objectives are as follows:

1. Exploratory data analysis
2. Identify trends
3. Create data visualizations

## Implementation
This project uses Jupyter Notebook with Python for data analysis; notebook contains
instructions for running analysis and provides an introduction on data science.

1. Dataset is loaded and analysis begins starting on Section 2
2. Each section contains explanation followed by code/analysis
3. Analysis progresses from data cleaning, summary statistics and visualization

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

Original README: "This is a first publishing of data from Sacramento Steps Forward data on
the Sacramento Regional Homeless population and continuum of Care for dates from
approximately 2011 through Fall of 2019."
