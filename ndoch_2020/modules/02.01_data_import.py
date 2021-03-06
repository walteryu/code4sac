# 02.01 - data import

# sf open data portal - sfpd reports (2003-2018)
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
# df_data = read_data("data/sfpd_report_2003-18.csv")

# note: reduce original file (500mb) by subset first 10k rows and replace file
# https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
# df_data = df_data[0:10000]
# output_result(df_data, "data/sfpd_report_2003-18.csv")

# read in reduced file after processing steps above
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
df_sfpd = read_data("data/sfpd_report_2003-18.csv")

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
df_school = read_data("data/ca_school_2019-20.csv")

# sacog - lihm community dataset (2016)
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0
sacog_lihm_csv = read_data("data/sacog_lihm_areas_2016.csv")

ca_covid_homeless_csv = read_data("data/homeless_impact.csv")
ca_county_csv = read_data("data/California_Counties.csv")

# verify data import
# data_profile(ca_covid_homeless_csv, "ca covid homeless")
# data_profile(ca_county_csv, "ca county")
# print(ca_covid_homeless_csv.head(5), '\n')
# print(ca_county_csv.head(5), '\n')

# scag - communities of concern dataset (2020)
# https://gisdata-scag.opendata.arcgis.com/datasets/communities-of-concern
scag_coc_csv = read_data("data/scag_coc_2020.csv")
