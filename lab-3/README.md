Lab 3 — Exploratory Data Analysis (Beginner) and Interactive Dashboard

Overview

This lab introduces basic exploratory data analysis (EDA) and shows how to create and share interactive visualizations using Plotly and Dash. It is targeted at beginners who completed Lab 1 and Lab 2 and are ready to move from static charts to interactive exploration.

Files in this folder

- `eda_and_dashboard.ipynb`: Jupyter notebook with step-by-step EDA, method explanations, and Plotly examples.
- `app.py`: Minimal Dash app that demonstrates simple interactivity (dropdown + slider) and how callbacks update charts.
- `requirements.txt`: Python packages needed to run the notebook and app.

Prerequisites

- Python 3.8+
- Basic familiarity with pandas, matplotlib, and seaborn (covered in Lab 1 & Lab 2)

Install dependencies (PowerShell)

```powershell
python -m pip install -r lab-3\requirements.txt
```

Run the notebook

- Start Jupyter: `jupyter notebook` and open `lab-3/eda_and_dashboard.ipynb`.

Run the dashboard

```powershell
python lab-3\app.py
```

Open `http://127.0.0.1:8050` in your browser.

Introduction to Plotly and Dash

Plotly
- Plotly (Plotly Express) is a high-level Python library for creating interactive charts. Charts produced with Plotly support zooming, panning, hover tooltips, and can be exported as standalone HTML files for sharing.
- Use Plotly when you want interactive exploration: hover to inspect values, zoom into regions of interest, and export sharable interactive reports.

Dash
- Dash is a minimal web framework built on top of Flask and Plotly that makes it easy to create interactive dashboards using Python only (no JavaScript required).
- Dash apps are composed of layout components (controls and graphs) plus callback functions that react to user inputs and update the visuals.
- Use Dash when you want a small interactive app with filters, linked charts, or a simple dashboard to share with others.

Lab outline and steps

This section explains the structure of the lab and the recommended sequence of steps for learners.

1) Introduction and objectives
	- Read the learning objectives and get familiar with the dataset (Seaborn `tips`).

2) Environment and imports
	- Install and import required libraries, set plotting styles, and explain what each import is for.

3) Load and inspect the data
	- Use `sns.load_dataset('tips')`, `df.shape`, `df.head()`, `df.info()`, and `df.describe()` to get a feel for the data.

4) Data cleaning and feature engineering
	- Add a `tip_pct` column, check for missing values, and cast types where necessary. Explain each operation in plain language.

5) Univariate analysis
	- Plot histograms and boxplots to inspect distributions and outliers. Explain when to use histogram vs boxplot.

6) Bivariate analysis
	- Scatter plots with regression line, colored by category (day/time). Compute and interpret a simple correlation matrix.

7) Multivariate exploration
	- Pairplots and correlation heatmap to spot multivariate patterns.

8) Interactive charts with Plotly
	- Build interactive scatter and bar charts using Plotly Express. Demonstrate hover data and saving to HTML.

9) Minimal dashboard with Dash
	- Walk through `app.py`: layout components (dropdown, slider), callback wiring, and how filters update charts. Run the app locally.

10) Exercises
	- Short, guided exercises to reinforce core skills (compute tip_pct stats, build scatter colored by day, extend the Dash app).

11) Summary and next steps
	- Suggestions for additional learning (interactive dashboards, simple model fitting, or larger datasets).

Recommended learning flow and time allocation (approximate)

- Inspect data and feature engineering: 10-15 minutes
- Univariate + bivariate plots: 20-25 minutes
- Multivariate views + correlations: 10-15 minutes
- Plotly interactive charts and saving HTML: 10-15 minutes
- Dash app walkthrough and running locally: 15-25 minutes

Exercises

1. Compute mean and median of `tip_pct` and plot a histogram. Describe the distribution.
2. Create a scatter plot of `total_bill` vs `tip` colored by `day`. Which day tends to have higher tips?
3. Run the Dash app in `app.py`, use the filters, and describe what changes when you select different days or party sizes.\\
4. (Optional) Extend `app.py` by adding a checkbox to toggle a regression line on the scatter plot.

Notes

- The notebook saves interactive HTML files in the `lab-3` folder. You can open them in a browser and share them as standalone interactive reports.
- If you want a completely self-contained dashboard without installing dependencies, export Plotly figures to HTML and share the HTML file instead of running Dash.
