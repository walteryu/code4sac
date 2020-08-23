# 02.01 - data import

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# function to read csv file
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
def read_data(path):
    df = pd.read_csv(path)
    return(df)

# function to output csv file
def output_result(df, filepath):
    df.to_csv(filepath)

# function to show table info
def data_profile(df, msg):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Table Info: %s ***' % msg, '\n')
    print(df.info(), '\n')
    print('*** Table Info: Table Dimensions ***', '\n')
    print(df.shape, '\n')

# function to show unique value for given column
def show_unique(df, col):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Unique Values: (%s) ***' % col, '\n')
    print(df[col].unique(), '\n')

# function to output summary stats
def summary_stats(df, col):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Summary Stats: (%s) ***' % col, '\n')
    print(df[col].describe(), '\n')
    # print(col.describe())

# function to rename columns
# https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/
def rename_col(df, old_col, new_col):
    df.rename(
        columns={old_col:new_col},
        inplace=True
    )
    return df

# sf open data portal - sfpd reports (2003-2018)
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
# df_data = read_data("data/sfpd_report_2003-18.csv")

# note: reduce original file (500mb) by subset first 10k rows and replace file
# https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
# df_data = df_data[0:10000]
# output_result(df_data, "data/sfpd_report_2003-18.csv")

# read in reduced file after processing steps above
df_sfpd = read_data("data/sfpd_report_2003-18.csv")

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
df_school = read_data("data/ca_school_2019-20.csv")

# subset dataset by row values; for example, schools by count
# https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values
df_school_sac = df_school[
    df_school['CountyName'].str.contains('Amador') |
    df_school['CountyName'].str.contains('Placer') |
    df_school['CountyName'].str.contains('Sacramento') |
    df_school['CountyName'].str.contains('Yolo') |
    df_school['CountyName'].str.contains('Yuba')
]

# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson
# df_school_geojson = read_data("data/ca_school_2019-20.geojson")

# data profile data after import
data_profile(df_sfpd, 'SFPD Reports (2003-18)')
data_profile(df_school, 'CA Schools (2019-20)')
data_profile(df_school_sac, 'CA Schools: Sac Area (2019-20)')
