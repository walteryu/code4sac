# 02A - load data and output column names

# load data into notebook; make sure file is in folder as notebook
df_assessments = pd.read_csv('data/assessments.csv')
df_clients = pd.read_csv('data/clients.csv')
df_enrollments = pd.read_csv('data/enrollments.csv')
df_exits = pd.read_csv('data/exits.csv')
df_projects = pd.read_csv('data/projects.csv')
df_services = pd.read_csv('data/services.csv')

# convert string to datetime
# note: original data contains date typos, e.g. yyyy = 2908
# solution: suppress typos with coerce flag
# reference: https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a

# index for plot based by date
# indexedDataset = dataset.set_index(['SampleDate'])

df_assessments['assessment_date'] = pd.to_datetime(
    df_assessments['assessment_date'],
    infer_datetime_format=True,
    errors = 'coerce'
)
df_clients['client_creation_date'] = pd.to_datetime(
    df_clients['client_creation_date'],
    infer_datetime_format=True,
    errors = 'coerce'
)
df_enrollments['entry_screen_creation_date'] = pd.to_datetime(
    df_enrollments['entry_screen_creation_date'],
    infer_datetime_format=True,
    errors = 'coerce'
)
df_exits['project_exit_date'] = pd.to_datetime(
    df_exits['project_exit_date'],
    infer_datetime_format=True,
    errors = 'coerce'
)

# example of converting column data type
# df['cost'] = pd.to_numeric(df['cost'])

# drop null values
# df = df.dropna()

# replace white spaces
# https://stackoverflow.com/questions/13757090/pandas-column-access-w-column-names-containing-spaces
# print("*** column names - assessments ***")
# df_assessments.columns = [c.replace(' ', '_') for c in df_assessments.columns]
# print(list(df_assessments.columns))
# print("")
# print("*** column names - clients ***")
# df_clients.columns = [c.replace(' ', '_') for c in df_clients.columns]
# print(list(df_clients.columns))
# print("")
# print("*** column names - enrollments ***")
# df_enrollments.columns = [c.replace(' ', '_') for c in df_enrollments.columns]
# print(list(df_enrollments.columns))
# print("")
# print("*** column names - exits ***")
# df_exits.columns = [c.replace(' ', '_') for c in df_exits.columns]
# print(list(df_exits.columns))
# print("")
# print("*** column names - projects ***")
# df_projects.columns = [c.replace(' ', '_') for c in df_projects.columns]
# print(list(df_projects.columns))
# print("")
# print("*** column names - services ***")
# df_services.columns = [c.replace(' ', '_') for c in df_services.columns]
# print(list(df_services.columns))
# print("")

# print out first 5 lines of dataset below
# print(df_assessments.head(5))
# print(df_clients.head(5))
# print(df_enrollments.head(5))
# print(df_exits.head(5))
# print(df_projects.head(5))
# print(df_services.head(5))

# inspect for data types and missing values (note: Pandas stores character strings as type 'object')
print("*** column names - assessments ***")
print(df_assessments.info())
print("")
print("*** column names - clients ***")
print(df_clients.info())
print("")
print("*** column names - enrollments ***")
print(df_enrollments.info())
print("")
print("*** column names - exits ***")
print(df_exits.info())
print("")
print("*** column names - projects ***")
print(df_projects.info())
print("")
print("*** column names - services ***")
print(df_services.info())
print("")
