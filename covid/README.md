# Code for Sacramento

![covid](https://github.com/walteryu/code4sac/blob/master/images/covid_countplot.png)

## COVID-19 Resources

This page contains resources and analysis which may be useful for Code4Sac hack night project ideas; specifically, datasets, portals and open data links for developing analysis and visualizations.

### COVID Data
* [COVID-19 API](https://covid19api.com/)
* [Allen Institute COVID-19 Data](https://pages.semanticscholar.org/coronavirus-research)

### Data Portals
1. [CA Open Data Portal](https://data.ca.gov/)
2. [CHHS Open Data Portal](https://data.chhs.ca.gov/)
3. [CDC Open Data Portal](https://data.cdc.gov/)
4. [WHO Open Data Portal](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/global-research-on-novel-coronavirus-2019-ncov)
5. [Kaiser Family Foundation Data Portal](https://www.kff.org/health-costs/issue-brief/state-data-and-policy-actions-to-address-coronavirus/#stateleveldata)
6. [Tableau COVID-19 Data Hub](https://www.tableau.com/covid-19-coronavirus-data-resources)

### Github
1. [NYTimes COVID-19 Data](https://github.com/nytimes/covid-19-data)
2. [Imperial College COVID-19 Model](https://github.com/ImperialCollegeLondon/covid19model)
3. [CA COVID-19 Website](https://github.com/cagov/covid19)

### Kaggle
* [COVID-19 Community Contributions](https://www.kaggle.com/covid-19-contributions)
* [COVID-19 Open Research Dataset Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

### Johns Hopkins University
* [JHU CSSE Data on Github](https://github.com/CSSEGISandData/COVID-19)
* [JHU COVID-19 Resource Center](https://coronavirus.jhu.edu/)
* [JHU Center for Health Security: Ventilator Availability](http://www.centerforhealthsecurity.org/resources/COVID-19/200214-VentilatorAvailability-factsheet.pdf)

## Jupyter Notebook

This project includes a notebook which contains analysis of the datasets below; objectives are as follows:

1. Exploratory data analysis
2. Date/time analysis
3. Data visualizations

### Implementation
This project uses Jupyter Notebook with Python for data analysis; notebook contains
instructions for running analysis and provides an introduction on data science.

1. Dataset is loaded and analysis begins starting on Section 2
2. Each section contains explanation followed by code/analysis
3. Analysis progresses from data cleaning, summary statistics and visualization

### Assumptions
1. Data types are assumed to be correct or else cleaned before analysis
2. Null values within numeric columns are filled in with zero for plots
3. Data cleaning and analysis is intended to help start other projects

### Data Exploration Ideas
1. How can this data be combine or analysis extended?
2. What are some questions which can be answered by doing so?
3. What are some factors which affect COVID curve, response and improvement?

### Next Steps
1. Source additional data for analysis
2. Create additional plots
3. Evaluate data quality of datasets

### Data Schema
Data schema is listed below:

1. Most datasets are a single table in CSV format unless otherwise noted
2. Most datasets contain primary ID for working with data
3. Most datasets contain datetime to identify new cases

### Data Cleaning
Cleaning was performed per steps below:

1. Column names were renamed across all tables with lower-case and underscore convention for consistency, i.e. like_this_column_name
2. Column name data types are converted to plain text, numeric and date types
3. Columns with date values were converted to datetime type

### Table Joins
Data tables were joined for analysis as listed below.
