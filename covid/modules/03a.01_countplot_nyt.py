# 03A.01 - create count plot

def count_plot(title, col, df, idx):
    # set plot size and title
    plt.figure(figsize=(12, 8))
    plt.title(title)
    # create countplot and sort categories by value
    # https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count
    sns.countplot(
        y=col,
        data=df,
        order=idx
    )

count_plot(
    'Count Plot: Total Case Count by US State',
    'state',
    df_total,
    df_total['state'].value_counts().index
)
count_plot(
    'Count Plot: Total Case Count in CA by County',
    "county",
    df_california,
    df_california['county'].value_counts().index
)
