# Superstore Sales Dashboard

This project is a simple sales analysis project using the **Sample Superstore** dataset.
I used Python to clean the data, study the sales and profit, and create an interactive dashboard.

## About the Project

The main goal of this project is to understand:

- How much the company sells
- How much profit the company makes
- Which products make more profit
- Which products are making a loss
- Which regions and states have more sales
- How sales change over time

## Tools Used

- Python
- Pandas
- HTML
- CSS
- JavaScript
- Chart.js
- GitHub

## What I Did

### 1. Cleaned the Data

The original file had some extra data added at the bottom.

I checked the file, removed the extra records, fixed the data types, and created a clean dataset.

The final dataset has **9,994 valid orders**.

### 2. Analyzed the Data

I used Python and Pandas to look at:

- Total sales
- Total profit
- Profit margin
- Sales by month and year
- Sales by region and state
- Sales by category
- Profit by sub-category
- Customer segments
- Product performance

### 3. Created a Dashboard

I created an interactive dashboard using HTML, JavaScript, and Chart.js.

The dashboard makes it easy to see the main sales and profit information through charts and numbers.

## Some Key Findings

- Total sales are around **$2.30 million**.
- The dataset contains **9,994 valid orders**.
- Some product groups make a loss even though they have sales.
- **Tables, Bookcases, and Supplies** show an overall loss in this analysis.
- Technology products are an important source of profit.
- Sales are generally stronger toward the end of the year.
- California and New York are among the major sales states.

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check it with:

```bash
python --version
```

### Step 2: Install Pandas

```bash
pip install pandas
```

### Step 3: Clean the Data

Run:

```bash
python clean_data.py
```

This creates:

```text
superstore_clean.csv
```

### Step 4: Run the Analysis

Run:

```bash
python analyze_real.py
```

This creates:

```text
dashboard_data_real.json
```

### Step 5: Open the Dashboard

Open this file in your browser:

```text
dashboard_real.html
```

You do not need to install a web server to view the dashboard.

## What I Learned

Through this project, I practiced:

- Working with real-world data
- Cleaning messy data
- Using Python and Pandas
- Finding useful information from data
- Understanding sales and profit
- Creating charts and dashboards
- Presenting data in a simple way

## Future Improvements

I can improve this project by:

- Creating the same dashboard in Power BI
- Adding more filters
- Adding sales forecasting
- Adding more charts
- Publishing the dashboard online
