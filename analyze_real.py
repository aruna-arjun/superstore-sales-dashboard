import pandas as pd
import json

df = pd.read_csv("/home/claude/retail_project/superstore_clean.csv", parse_dates=["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders
profit_margin = total_profit / total_sales * 100

# Monthly trend
monthly = df.groupby("Month").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order ID", "nunique")).reset_index()

# Category breakdown
category = df.groupby("Category").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum")).reset_index().sort_values("Sales", ascending=False)

# Sub-category breakdown (real dataset has this extra layer)
subcategory = df.groupby("Sub-Category").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum")).reset_index().sort_values("Sales", ascending=False)

# Region breakdown
region = df.groupby("Region").agg(Sales=("Sales", "sum"), Orders=("Order ID", "nunique")).reset_index().sort_values("Sales", ascending=False)

# Top states
state = df.groupby("State").agg(Sales=("Sales", "sum")).reset_index().sort_values("Sales", ascending=False).head(8)

# Top products
product = df.groupby("Product Name").agg(Sales=("Sales", "sum"), Units=("Quantity", "sum")).reset_index().sort_values("Sales", ascending=False).head(8)
product["Product Name"] = product["Product Name"].str.slice(0, 32)

# Segment breakdown
segment = df.groupby("Segment").agg(Sales=("Sales", "sum")).reset_index().sort_values("Sales", ascending=False)

# Loss-making sub-categories (real, useful insight this dataset is famous for)
loss_makers = subcategory[subcategory["Profit"] < 0]

output = {
    "kpis": {
        "total_sales": round(total_sales, 0),
        "total_profit": round(total_profit, 0),
        "total_orders": int(total_orders),
        "avg_order_value": round(avg_order_value, 0),
        "profit_margin": round(profit_margin, 1),
    },
    "monthly": monthly.to_dict("records"),
    "category": category.to_dict("records"),
    "subcategory": subcategory.to_dict("records"),
    "region": region.to_dict("records"),
    "state": state.to_dict("records"),
    "product": product.rename(columns={"Product Name": "Product"}).to_dict("records"),
    "segment": segment.to_dict("records"),
}

with open("/home/claude/retail_project/dashboard_data_real.json", "w") as f:
    json.dump(output, f, indent=2, default=str)

print(json.dumps(output["kpis"], indent=2))
print("\nLoss-making sub-categories:")
print(loss_makers[["Sub-Category", "Profit"]])
