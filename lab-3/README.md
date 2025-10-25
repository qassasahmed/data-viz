# Interactive Data Visualization Dashboard

## Introduction to Interactive Plotting with Plotly and Dash

Interactive plotting is a powerful way to explore and present data dynamically. **Plotly** is a graphing library that creates interactive, web-based visualizations. It supports various chart types like bar charts, scatter plots, and box plots, allowing users to hover for details, zoom, and filter data in real-time. **Dash** is a productive Python framework for building web applications, particularly useful for data visualization dashboards. It integrates seamlessly with Plotly to create interactive web apps without needing extensive web development knowledge.

Key benefits include:
- **Interactivity**: Users can interact with charts (e.g., hover, click, zoom) to gain deeper insights.
- **Web-based**: Dashboards run in browsers, making them accessible and shareable.
- **Python-native**: Build complex apps using Python, leveraging libraries like Pandas for data manipulation.
- **Customization**: Easily add callbacks for dynamic updates based on user input.

This project demonstrates creating an interactive dashboard with multiple chart types using the Tips dataset from Seaborn.

## Project Overview

This notebook (`interactive_dashboard.ipynb`) loads the Tips dataset and creates five interactive visualizations:
- Bar chart: Average tip by day
- Pie chart: Gender distribution
- Donut chart: Smoker distribution
- Scatter plot: Total bill vs tip, colored by day
- Box plot: Tip distribution by day

The dashboard is built using Dash and runs on a local server for interactive exploration.

## Understanding Box Plots in Detail

A box plot (also known as a box-and-whisker plot) is a statistical visualization that summarizes the distribution of a dataset. It displays key statistical measures and helps identify outliers, variability, and central tendency.

### Components of a Box Plot:
- **Box**: Represents the interquartile range (IQR), containing the middle 50% of the data.
  - Bottom of the box: First quartile (Q1, 25th percentile)
  - Middle line: Median (Q2, 50th percentile)
  - Top of the box: Third quartile (Q3, 75th percentile)
- **Whiskers**: Extend from the box to show the range of the data.
  - Lower whisker: Typically Q1 - 1.5 × IQR (minimum value within this range)
  - Upper whisker: Typically Q3 + 1.5 × IQR (maximum value within this range)
- **Outliers**: Data points beyond the whiskers, plotted as individual dots or symbols.

### How to Read a Box Plot:
1. **Central Tendency**: The median line shows the middle value. Compare medians across groups to see differences.
2. **Spread**: The box height indicates variability. Wider boxes mean more spread in the middle 50% of data.
3. **Skewness**: If the median is closer to Q1 or Q3, the data is skewed left or right.
4. **Outliers**: Points outside whiskers highlight anomalies that may need investigation.
5. **Comparisons**: When grouped (e.g., by day), box plots reveal patterns like which groups have higher/lower medians or more outliers.

### How Box Plots Help Understand Data:
- **Summarize Distributions**: Quickly grasp key stats without raw data.
- **Identify Patterns and Anomalies**: Spot trends, variability, and outliers across categories.
- **Compare Groups**: Easily compare distributions (e.g., tip amounts by day) to find differences.
- **Guide Further Analysis**: Outliers may indicate errors or interesting cases; variability can suggest areas for deeper study.
- **Data Quality Check**: Detect skewness or unusual spreads that might affect modeling.

In this dashboard, the box plot shows tip distributions by day, helping analyze daily tipping consistency and identify days with more variability or outliers.

## How to Run

1. Ensure Python is installed.
2. Install dependencies: Run `pip install -r requirements.txt` or execute the pip install cell in the notebook.
3. Open `interactive_dashboard.ipynb` in Jupyter Notebook or VS Code.
4. Run all cells in order.
5. The Dash app will start at http://127.0.0.1:8051/. Open in a browser to interact with the dashboard.

## Requirements

- pandas
- seaborn
- plotly
- dash

For more details, see the notebook's code explanations.  

qassas.ahmed@mau.edu.eg 