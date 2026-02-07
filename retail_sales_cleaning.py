import pandas as pd

df = pd.read_csv("retail_sales_dataset.csv")

#making sure there are no white spaces
df.columns.str.strip()

#remove duplicates 
df = df.drop_duplicates()

#converting Date to datetime instead of an object
df["Date"] = pd.to_datetime(arg= df["Date"])

df.set_index(keys=df["Transaction ID"], inplace=True)
df = df.reset_index(drop=True)
df.drop(columns="Transaction ID", inplace=True)


# adds quartile column
quartiles = df['Total Amount'].quantile([0.25, 0.5, 0.75])
q1, q2, q3 = quartiles[0.25], quartiles[0.5], quartiles[0.75]
# Assign each transaction to a quartile
def assign_quartile(x):
    if x <= q1:
        return 'Q1'
    elif x <= q2:
        return 'Q2'
    elif x <= q3:
        return 'Q3'
    else:
        return 'Q4'

df['Quartile'] = df['Total Amount'].apply(assign_quartile)
# Sum revenue per quartile
quartile_revenue = df.groupby('Quartile')['Total Amount'].sum().sort_values(ascending=True)
