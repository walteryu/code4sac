# 02A - Load data into notebook

# load data into notebook; make sure file is in folder as notebook
df = pd.read_csv('caltrans-annual-vehicle-delay-2017-v1.csv')

# example of converting column data type
# df['Labor Cost'] = pd.to_numeric(df['Labor Cost'])

# print out first 5 lines of dataset below
print(df.head(5))
