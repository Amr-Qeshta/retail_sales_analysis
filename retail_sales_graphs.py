import matplotlib.pyplot as plt
import numpy as np
import retail_sales_analysis as rsa

# table describing the dataset
def describe():
    desc = rsa.desc
    fig, ax = plt.subplots(figsize=(14,6))
    ax.axis("off")

    table = ax.table(
        cellText=desc.values,
        colLabels=desc.columns,
        rowLabels=desc.index,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 3)
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\descriptive_statistics.png", bbox_inches="tight", dpi=300)    

#quarterly sales 
def monthly_rev():
    quarter_sales = rsa.qrt_sales
    plt.figure(figsize=(14, 8), layout="tight")
    plt.grid(axis="both", alpha=0.2, color="black")
    plt.title("Total Monthly Revenue", fontweight="bold", color="#243233", pad=10, fontsize = 16)
    plt.plot(quarter_sales.index, quarter_sales.values, marker="o", markerfacecolor="#222222", markeredgecolor="#F5E7C6",markersize=10, color="#CCA996", linewidth=5)
    plt.xlabel("Month", labelpad=15, weight="normal", fontsize=13, color="#1D2E21")
    plt.xticks(quarter_sales.index)
    plt.ylabel("Revenue", labelpad=15, weight="normal", fontsize=13, color="#1D2E21")
    plt.yticks(np.arange(0, quarter_sales.max() *1.3, 5000))
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Revenue\\Monthly_Revenue.png", bbox_inches="tight", dpi=300)    


#bar graph to show top selling categories
def top_cat():
    category = rsa.category_sales
    plt.figure(figsize=(14,8), layout="tight")
    plt.title("Revenue by Category", weight="bold", pad=10, fontsize=18, color="#243328")
    
    for i, value in enumerate(category): # returns index and name of columns eg. i=0, category = beauty
        pct = value / category.sum() * 100
        plt.text( value + 10000, i, f"{pct:0.2f} % ", ha="center", va="bottom", fontsize=14, weight="normal" )
    
    plt.barh(category.index, category.values, edgecolor="black", color = "#454D6E")
    
    plt.xlabel("Total Revenue", labelpad=10, weight="normal", fontsize=13, color="#1D2E21" )
    plt.ylabel("Category", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.xticks(np.arange(0, category.max() * 1.1, 10000))
    plt.xlim(0, category.max() * 1.15)
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Revenue\\category_revenue.png", bbox_inches="tight", dpi=300)

#bar graph to show revenue contribution of each quartile
def quartile_bar():
    quartile = rsa.quartile_revenue
    plt.figure(figsize=(14,8), layout="tight")
    plt.title("Revenue by Quartile", weight="bold", pad=10, fontsize=18, color="#243328")

    for i, value in enumerate(quartile): # returns index and name of columns eg. i=0, category = beauty
        pct = value / quartile.sum() * 100
        plt.text( value + 10000, i, f"{pct:0.0f} % ", ha="center", va="bottom", fontsize=14, weight="normal" )
    
    plt.barh(quartile.index, quartile.values, edgecolor="black", color = "#454D6E")
    
    plt.xlabel("Total Revenue", labelpad=10, weight="normal", fontsize=13, color="#1D2E21" )
    plt.ylabel("Quartile", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.xticks(np.arange(0, quartile.max() * 1.2, 25000))
    plt.xlim(0, quartile.max() * 1.10)
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Revenue\\quartile_revenue.png", bbox_inches="tight", dpi=300)

#bar graph for category purchase count
def cat_count():
    cat_count = rsa.cat_count
    plt.figure(figsize=(16,8))
    for i, value in enumerate(cat_count):
        pct = value / cat_count.sum() * 100
        plt.text( value *1.1, i, f"{value} ({pct:0.0f}%)", ha="center", va="bottom", fontsize=12, weight="normal" )

    plt.barh(cat_count.index, cat_count.values, edgecolor="black", color = "#454D6E")
    
    plt.xlabel("Count", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.xlim(0, cat_count.max() * 1.2)
    plt.ylabel("Product Category", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.title("Total Items Purchased by Product Category")
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Category\\category_count.png", bbox_inches="tight", dpi=300)


#bar graph to show highest selling category each month 
def top_m_cat():
    month = rsa.top_month
    category_colors = {
        "Beauty": "#E07A5F",
        "Clothing": "#81B29A",
        "Electronics": "#3D405B",
        "Furniture": "#F2CC8F"
    }
    
    plt.figure(figsize=(19.2,10.8), layout="tight")
    plt.title("Top Selling Category by Month", weight="bold", pad=10, fontsize=18, color="#243328")

    seen = set()
    handles = []

    for i, row in month.iterrows():
        month_label = row["Month Label"]    
        total = row["Total Amount"]
        category = row["Product Category"]
        color = category_colors[category]
        
        # draw the bar
        plt.bar(month_label, total, color=color, edgecolor="black")
        
        # add one entry per category to the legend
        if category not in seen:
            handles.append(plt.Rectangle((0,0),1,1, color=color, edgecolor="black", label=category))
            seen.add(category)

    plt.xlabel("Month", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.ylabel("Total Item count", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.legend(title="Product Category", handles=handles)
    plt.ylim(0, month["Total Amount"].max() * 1.10)
    plt.savefig("S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Category\\top_selling_category_monthly.png", bbox_inches="tight", dpi=300)

    
#gender unique category sales for each quarter in a combined bar plot
def prod_qrt_gen_sales(gender, gender_sales, quarter_sales, quarters, categories, n_quarters, n_categories, x):
    width = 0.20
    plt.figure(figsize=(16,6), dpi = 100, layout="tight")
    #to control y axis 
    ymin, ymax = plt.ylim(bottom=0, top=quarter_sales.max().max() * 1.15)
    #loop for the main bar plot 
    for i, category in enumerate(categories):
        plt.bar(x + i*width, quarter_sales[category].values,
            width=width, label=category)
        
    #loop to write the value of each category with its percentrage of the total sales in the corresponding quarter
    for i, category in enumerate(quarter_sales.columns): # returns index and name of columns eg. i=0, category = beauty
        for j, value in enumerate(quarter_sales[category].values): # returns index of a quarter and the value of category sales in that quarter 
            total = (quarter_sales.iloc[j].astype("int").sum()) # returns sum (total) categories sales of a given quarter eg. Q1-2023
            pct = value / total * 100
            plt.text(x[j] + i* width, value + 0.5, f"{value}\n  {pct:0.0f}% ", ha="center", va="bottom", fontsize=10 )
       
        #loop to write the total of the quarter on top of the bars 
        for m in range(n_quarters):    
            plt.text(x[m] + width * (n_categories - 1) / 2 ,
                    quarter_sales.iloc[m].max() + ymax - ymax * 0.908, f"Total: {quarter_sales.iloc[m].sum():0.0f}",
                     ha="center", va="bottom", fontsize=10, fontweight="normal")
  
    # customization of the plot                          
    plt.xticks(x + width*(n_categories-1)/2,
               [f"({quarters[q]}) Total: " + quarter_sales.iloc[q].sum().astype("int").astype("str") for q in range(n_quarters)])
    plt.xlabel("Quarter", labelpad=10, weight="bold", fontsize=12)
    plt.ylabel("Total Sales", labelpad= 10, weight="bold", fontsize=12)
    plt.title(f"Distribution of {gender} Sales by Product Category (2023 – 2024): Total {gender_sales.sum().sum():0.0f}", pad=15, weight="bold", fontsize=14)
    plt.legend(fontsize="large", loc="best")
    plt.savefig(f"S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\Category\\{gender}_category_sales.png", bbox_inches="tight", dpi=300)

#histogram of percentage distribution of total amount paid for a given gender in a certain category 
def gen_total_sales(gender, category):
    gender = gender.capitalize()
    category = category.capitalize()
    plt.figure(figsize=(12,8))

    cat_sales = rsa.filt_cat_sales(rsa.df, gender, category)
    weights = np.ones_like(cat_sales) / len(cat_sales) * 100
    bins = np.arange(0, cat_sales.values.max() + 100, 200)
    plt.hist(cat_sales.values, bins=bins,weights=weights, edgecolor="black", color = "#454D6E")
    
    plt.xticks(bins)
    plt.xlabel(f"Total Amount Paid", labelpad=10, weight="normal", fontsize=13, color="#1D2E21")
    plt.yticks(np.arange(0,65,5))
    plt.ylabel(f"Percentage", labelpad=15, weight="normal", fontsize=13, color="#1D2E21")
    plt.title(f"Percentage Distribution of {gender} Purchases in {category} Category", weight="bold", pad=10, fontsize=16, color="#243328")
    plt.savefig(f"S:\\Programming\\retail_sales_dataset\\retail_sales_figures\\demographic\\{gender}_{category}_distribution.png", bbox_inches="tight", dpi=300)

#examples, note that it accesses retail_sales_analysis.py file to call the get_gender_sales function, unpacking the return for this function
prod_qrt_gen_sales(*rsa.get_gender_sales("male"))
prod_qrt_gen_sales(*rsa.get_gender_sales("female"))

#examples
gen_total_sales("male", "beauty")
gen_total_sales("female", "beauty")
