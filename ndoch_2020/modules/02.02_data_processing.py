# 02.02 - data processing

# subset dataset by row values; for example, schools by count
# https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values
df_school_sac = df_school[
    df_school['CountyName'].str.contains('Sacramento')
]
df_school_amador = df_school[
    df_school['CountyName'].str.contains('Amador')
]
df_school_placer = df_school[
    df_school['CountyName'].str.contains('Placer')
]
df_school_yolo = df_school[
    df_school['CountyName'].str.contains('Yolo')
]
df_school_yuba = df_school[
    df_school['CountyName'].str.contains('Yuba')
]

# todo: process geojson
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson
# df_school_geojson = read_data("data/ca_school_2019-20.geojson")

# data profile data after import
# data_profile(df_sfpd, 'SFPD Reports (2003-18)')
# data_profile(df_school, 'CA Schools (2019-20)')
# data_profile(df_school_sac, 'CA Schools: Sacramento County (2019-20)')
# data_profile(df_school_amador, 'CA Schools: Amador County (2019-20)')
# data_profile(df_school_placer, 'CA Schools: Placer County (2019-20)')
# data_profile(df_school_yolo, 'CA Schools: Yolo County (2019-20)')
# data_profile(df_school_yuba, 'CA Schools: Yuba County (2019-20)')

rename_col(ca_county_csv, 'Name', 'county')
ca_covid_county_csv = merge_table(ca_covid_homeless_csv, ca_county_csv, 'county', 'right')
data_profile(ca_covid_county_csv, "ca covid homeless and county")
