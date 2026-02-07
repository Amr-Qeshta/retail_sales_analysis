import pandas as pd
import numpy as np
import retail_sales_cleaning as rsc

df = rsc.df
quartile_revenue = rsc.quartile_revenue

category_sales = rsc.df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=True)

monthly_gender_category = rsc.df.groupby(["Gender",
                          pd.Grouper(key="Date", freq="MS"),"Product Category"])["Total Amount"].sum().unstack("Product Category").fillna(0)

def get_gender_sales(gender):
    gender = gender.capitalize()
    gender_sales = monthly_gender_category.xs(gender, level="Gender")
    quarterly_sales = gender_sales.resample('QE').sum()
    quarters = ["Q" + f"{q.quarter}-{q.year}" for q in quarterly_sales.index]
    categories = list(gender_sales.columns)
    n_quarters = len(quarterly_sales)
    n_categories = len(categories)
    x = np.arange(n_quarters)
    return [gender, gender_sales, quarterly_sales, quarters, categories, n_quarters, n_categories, x]


def filt_cat_sales(dataframe, gender, category):
    gender = gender.capitalize()
    category = category.capitalize()
    filtered = dataframe.loc[
        (dataframe["Gender"] == gender) & (dataframe["Product Category"] == category), ["Total Amount"]].sort_values(by="Total Amount", ascending=True)
    
    detailed_filter = dataframe.loc[
        (dataframe["Gender"] == gender) & (dataframe["Product Category"] == category),
        [ "Quantity", "Price per Unit", "Total Amount"]
    ].sort_values(by="Total Amount", ascending=True)
    
    filtered.dropna(inplace=True)
    filtered = filtered.reset_index(drop=True)

    detailed_filter.dropna(inplace=True)
    detailed_filter = detailed_filter.reset_index(drop=True)

    return pd.DataFrame(filtered)


#returns quarterly revenue
qrt_sales = df.set_index(rsc.df["Date"])
qrt_sales = qrt_sales["Total Amount"].resample("BME").sum()
qrt_sales.index = qrt_sales.index.strftime("%b-%Y")


#top seller each month
top_months = df.groupby(["Product Category",
                          pd.Grouper(key="Date", freq="BME")])["Total Amount"].count().fillna(0)


top_per_month = top_months.groupby(level=1).idxmax()
top_month = top_months.loc[top_per_month]
top_month = top_month.reset_index()
top_month = top_month.set_index(top_month["Date"])
top_month.drop(columns="Date", inplace=True)
top_month = top_month.sort_index()
top_month["Month Label"] = top_month.index.strftime("%m-%Y")


desc = df
desc["Date"] = desc["Date"].dt.date
desc = desc.describe().loc[["mean", "std", "min", "max"]].T.round(2)

cat_count = df["Product Category"].value_counts().sort_values(ascending=True)
