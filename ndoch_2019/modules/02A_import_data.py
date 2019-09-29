# 02A - Load data into notebook

# load data into notebook; make sure file is in folder as notebook
df = pd.read_csv('caltrans-annual-vehicle-delay-2017-v2.csv')

# example of converting column data type
# df['Labor Cost'] = pd.to_numeric(df['Labor Cost'])

# print out first 5 lines of dataset below
print(df.head(5))

# inspect for data types and missing values (note: Pandas stores character strings as type 'object')
print('\nOur dataframe\'s column info including data types and null/missing values: \n')
print(df.info())

# we see from df.info() that some columns have null/missing values, let's retain only complete records
df = df.dropna()