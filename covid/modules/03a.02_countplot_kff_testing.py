# 03A.02 - create count plot

# show data elements
# 0   location                      63 non-null     object
# 1   tests_with_results            56 non-null     float64
# 2   percentage_test_positive      39 non-null     float64
# 3   total_tests_per_1k_residents  53 non-null     float64
# print(df_total_kff.info())

# subset data and drop null values for plot
df_results_plot = df_total_kff[['location', 'tests_with_results']]

# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
df_results_plot['tests_with_results'].fillna(0)

# drop total count to scale plot correctly
# https://stackoverflow.com/questions/16396903/delete-the-first-three-rows-of-a-dataframe-in-pandas
df_results_plot = df_results_plot.iloc[1:]

# create distplot with settings
def create_displot(title, df, count):
    # create histogram
    plt.figure(figsize=(12, 8))
    plt.title(title),
    sns.distplot(df, bins=count)

create_displot(
    'Historgram: Total COVID-19 Tests with Results\n Note: Each Record = Total for Single US State',
    df_results_plot['tests_with_results'],
    50
)

# create histogram
# plt.figure(figsize=(12, 8))
# plt.title('Historgram: Total COVID-19 Tests with Results\n Note: Each Record = Total for Single US State')
# sns.distplot(df_results_plot['tests_with_results'], bins=50)

# aggregate and sort for plot
# https://gist.github.com/fomightez/bb5a9c727d93d1508187677b4d74d7c1
df_results_sort = df_results_plot.groupby(['location'])['tests_with_results'].aggregate(np.median).reset_index()

# create barplot with settings
def create_barplot(title, y_col, x_col, df):
    # create countplot
    plt.figure(figsize=(12, 8))
    plt.title(title),
    ax = sns.barplot(
        y=y_col,
        x=x_col,
        data=df
    )

create_barplot(
    'Bar Plot: Total COVID-19 Tests with Results by US State\n Note: Each Record = Total for Single US State',
    'location',
    'tests_with_results',
    df_results_sort
)

# create_barplot(
#     'Bar Plot: Total COVID-19 Tests with Results by US State\n Note: Each Record = Total for Single US State',
#     'location',
#     'tests_with_results',
#     df_results_sort
# )

# subset data and drop null values for plot
df_positive_plot = df_total_kff[['location', 'percentage_test_positive']]

# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# print(pd.isna(df_results_plot))
df_positive_plot['percentage_test_positive'].fillna(0)

# drop total count to scale plot correctly
# https://stackoverflow.com/questions/16396903/delete-the-first-three-rows-of-a-dataframe-in-pandas
df_positive_plot = df_positive_plot.iloc[1:]

# create distplot
# plt.figure(figsize=(12, 8))
# plt.title('Historgram: Percentage of COVID-19 Tests with Positive Result\ Note: Each Record = Individual US State')
# sns.distplot(df_positive_plot['percentage_test_positive'], bins=50)

create_barplot(
    'Bar Plot: Total COVID-19 Percent with Positive Results by US State\n Note: Each Record = Total for Single US State',
    'location',
    'percentage_test_positive',
    df_positive_plot
)

# create barplot
# plt.figure(figsize=(12, 8))
# plt.title('Bar Plot: Total COVID-19 Percent with Positive Results by US State\n Note: Each Record = Total for Single US State')
# sns.barplot(y = "location", x="percentage_test_positive", data=df_positive_plot)

# subset data and drop null values for plot
df_1k_plot = df_total_kff[['location', 'total_tests_per_1k_residents']]

# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# print(pd.isna(df_results_plot))
df_1k_plot['total_tests_per_1k_residents'].fillna(0)

# drop total count to scale plot correctly
# https://stackoverflow.com/questions/16396903/delete-the-first-three-rows-of-a-dataframe-in-pandas
df_1k_plot = df_1k_plot.iloc[1:]

# create histogram
# plt.figure(figsize=(12, 8))
# plt.title('Historgram: Total COVID-19 Tests per 1k Residents\n Note: Each Record = Total for Single US State')
# sns.distplot(df_1k_plot['total_tests_per_1k_residents'], bins=50)

df_1k_plot = df_1k_plot.groupby(["location"])['total_tests_per_1k_residents'].aggregate(np.median).reset_index()

# create barplot
create_barplot(
    'Bar Plot: Total COVID-19 Tests per 1k Residents by US State\n Note: Each Record = Total for Single US State',
    'location',
    'total_tests_per_1k_residents',
    df_1k_plot
)
