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

## Data Schema and Cleaning
Data schema is listed below:

1. Dataset contains six tables, each connected via "Personal_ID" field
2. Each table contains data on a single entity, e.g. clients, projects, etc.
3. Dataset follows traditional relational schema since it is extracted from RDBMS

Cleaning was performed per steps below:

1. "Personal_ID" column name was made consistent across all tables
2. "Personal_ID" data type was made consistent across all tables

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
Github Source Data Repo: https://github.com/code4sac/sacramento-county-homeless-hmis-data

Original README: "This is a first publishing of data from Sacramento Steps Forward data on
the Sacramento Regional Homeless population and continuum of Care for dates from
approximately 2011 through Fall of 2019."
