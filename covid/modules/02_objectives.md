## Section 2A - Project Objectives

This notebook will focus on COVID-19 data analysis; objectives are as follows:

1. Exploratory data analysis
2. Identify trends
3. Create data visualizations

This notebook is organized by analysis of the datasets listed below. Analysis for each dataset consists of several modules for data import, cleaning, profiling and analysis; datasets are as follows:

### [NYTimes Case Data](https://github.com/nytimes/covid-19-data)

Individual cases prepared by NYTimes journalist staff and updated daily by US county. Data is provided in CSV format; it is an effort to clarify the reports by US states and counties on their case count. CSV dataset in the data folder contains total cases as of 04-03-2020; otherwise, URL reads from current data.

The source data documentation describes the project is as follows:

> The data is the product of dozens of journalists working across several time zones to monitor news conferences, analyze data releases and seek clarification from public officials on how they categorize cases.

### [KFF Testing Data](https://www.kff.org/health-costs/issue-brief/state-data-and-policy-actions-to-address-coronavirus/#stateleveldata)

COVID-19 testing with results prepared by the Kaiser Family Foundation (KFF). Results are aggregated by US state; null values indicate that data was not available for a particular record/state. Original file is in Excel format, so CSV was created with header/footer trimmed for data import.

The source data documentation describes the project is as follows:

> With enactment of the Families First Coronavirus Response Act on March 18, 2020, the federal government took action to ensure access to COVID-19 testing. The legislation requires Medicare, Medicaid, all group health plans, and individual health insurance policies to cover testing and associated visits related to the diagnosis of COVID-19 during the federally-declared emergency period. In addition, the new law gives states the option to provide Medicaid coverage of COVID-19 testing for uninsured residents with 100% federal financing.

### [GeoJSON Data](https://geojson.org/)

GeoJSON data of current/projected cases were imported and visualized based on the following resources/tutorials:

1. [Twilio Jupyter GeoJSON Tutorial](https://github.com/lesley2958/twilio-geospatial)
2. [Kaggle Jupyter GeoJSON Tutorial](http://thepythoncorner.com/dev/python-geographical-maps-coronavirus/)
3. [Kaggle COVID-19 Time Series Data](http://thepythoncorner.com/dev/python-geographical-maps-coronavirus/)
