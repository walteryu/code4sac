# 02A - Load data into notebook

# load data into notebook; make sure file is in folder as notebook
df = pd.read_csv('caltrans-annual-vehicle-delay-2017.csv')

# example of converting column data type
# df[''] = pd.to_numeric(df[''])

# print out first 5 lines of dataset below
print(df.head(5))
