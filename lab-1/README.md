# Lab-1: Bar Chart Tutorial - Data Visualization Course

This tutorial introduces beginners to basic data visualization using Python, focusing on creating and customizing bar charts.

---

## 📚 Key Concepts

### What is a Dataset?

A **dataset** is a collection of related data organized in a structured way. Think of it as a container that holds information about a particular subject.

**Characteristics of a Dataset:**
- Contains multiple data points or records
- Has a defined structure (rows and columns)
- Can be stored in various formats (CSV, Excel, JSON, etc.)
- Used for analysis, visualization, and machine learning

**Example:**
```
Student scores in different subjects:
- Mathematics: 85
- Physics: 78
- Chemistry: 82
```

---

### What is a DataFrame?

A **DataFrame** is a two-dimensional, tabular data structure provided by the pandas library in Python. It's like a spreadsheet or SQL table in your code.

**Key Features of DataFrames:**
- **Rows and Columns**: Data is organized in rows (records) and columns (features/variables)
- **Labeled Axes**: Both rows and columns can have labels/names
- **Mixed Data Types**: Different columns can contain different data types (numbers, strings, dates)
- **Easy Manipulation**: Built-in functions for filtering, sorting, grouping, and analyzing data

**Example:**
```python
import pandas as pd

data = {
    'Subject': ['Math', 'Physics', 'Chemistry'],
    'Score': [85, 78, 82]
}
df = pd.DataFrame(data)
```

**Output:**
```
     Subject  Score
0       Math     85
1    Physics     78
2  Chemistry     82
```

---

### Tabular Data Formats

Tabular data is data organized in a table with rows and columns. Here are common formats:

| Format | Description | Extension | Best For |
|--------|-------------|-----------|----------|
| **CSV** | Comma-Separated Values - Plain text with commas separating values | `.csv` | Simple data exchange, widely supported |
| **Excel** | Microsoft Excel spreadsheet format | `.xlsx`, `.xls` | Business data, multiple sheets, formatting |
| **JSON** | JavaScript Object Notation - Hierarchical text format | `.json` | Web APIs, nested data structures |
| **SQL** | Structured Query Language databases | `.db`, `.sqlite` | Large datasets, relational data |
| **Parquet** | Columnar storage format | `.parquet` | Big data, fast read/write operations |
| **TSV** | Tab-Separated Values - Similar to CSV but uses tabs | `.tsv` | Data with commas in values |

**Which Format to Choose?**
- **CSV**: Best for simple, flat data tables
- **Excel**: When you need formatting or multiple sheets
- **JSON**: For nested/hierarchical data from web APIs
- **SQL**: For large datasets requiring queries

---

## 💻 Example Code Breakdown

Let's break down the key parts of our bar chart tutorial:

### 1. Import Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```
- **pandas**: For data manipulation and creating DataFrames
- **matplotlib.pyplot**: For creating basic visualizations
- **seaborn**: For enhanced, statistical visualizations
- **numpy**: For numerical operations and array manipulation

### 2. Create a Dataset
```python
data = {
    'Subject': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English'],
    'Average_Score': [85, 78, 82, 90, 88]
}
df = pd.DataFrame(data)
```
- Creates a dictionary with two keys (columns)
- Converts the dictionary to a pandas DataFrame

### 3. Create a Basic Bar Chart
```python
plt.figure(figsize=(10, 6))
plt.bar(df['Subject'], df['Average_Score'])
plt.show()
```
- `plt.figure()`: Creates a new figure with specified size
- `plt.bar()`: Creates the bar chart
- `plt.show()`: Displays the chart

### 4. Add Customizations
```python
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Student Average Scores by Subject', fontsize=14, fontweight='bold')
```
- Adds axis labels and title
- Customizes font size and weight

### 5. Apply Colors
```python
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
plt.bar(df['Subject'], df['Average_Score'], color=colors, edgecolor='black')
```
- Defines custom color codes (hex format)
- Applies colors to bars with black borders

### 6. Create Grouped Bar Charts
```python
# Set up positions for multiple bars
bar_width = 0.25
x = np.arange(len(subjects))

# Create bars for each student
plt.bar(x - bar_width, alice_scores, bar_width, label='Alice')
plt.bar(x, bob_scores, bar_width, label='Bob')
plt.bar(x + bar_width, charlie_scores, bar_width, label='Charlie')
```
- **Grouped bar charts** compare multiple groups side-by-side
- Use `bar_width` to control spacing between groups
- Offset positions using `x - bar_width`, `x`, `x + bar_width`

### 7. Create Stacked Bar Charts
```python
plt.bar(x, alice_scores, label='Alice')
plt.bar(x, bob_scores, bottom=alice_scores, label='Bob')
plt.bar(x, charlie_scores, bottom=alice_scores + bob_scores, label='Charlie')
```
- **Stacked bar charts** show composition and total
- Use `bottom` parameter to stack bars on top of each other
- Each layer adds to the previous one

---

## 📊 Matplotlib vs Seaborn Comparison

| Feature | Matplotlib | Seaborn |
|---------|-----------|---------|
| **Level** | Low-level, more control | High-level, simpler syntax |
| **Ease of Use** | Requires more code | Less code, more automatic |
| **Default Styling** | Basic, requires customization | Beautiful defaults, modern themes |
| **Statistical Plots** | Manual implementation needed | Built-in statistical visualizations |
| **Customization** | Highly customizable, granular control | Less granular, but easier |
| **Learning Curve** | Steeper for beginners | Gentler for beginners |
| **Best For** | Custom, precise visualizations | Quick, attractive statistical plots |
| **Integration** | Standalone | Built on top of Matplotlib |
| **Plot Types** | Basic plots (bar, line, scatter) | Statistical (violin, box, regression) |
| **Data Input** | Lists, arrays | Works seamlessly with DataFrames |

### When to Use Which?

**Use Matplotlib when:**
- You need fine-grained control over every element
- Creating custom visualizations not available in Seaborn
- Building complex, multi-subplot layouts
- You're already familiar with its API

**Use Seaborn when:**
- You want beautiful plots with minimal code
- Working with pandas DataFrames
- Creating statistical visualizations
- You need modern, publication-ready aesthetics
- You're a beginner learning data visualization

**Pro Tip:** You can use both together! Seaborn is built on Matplotlib, so you can use Seaborn for quick plots and then customize with Matplotlib functions.

---

## 📊 Types of Bar Charts Covered

### 1. Simple Bar Chart
Best for comparing single values across categories.
- **Use case**: Comparing average scores across subjects
- **Example**: Average test score per subject

### 2. Grouped Bar Chart
Displays multiple groups side-by-side for easy comparison.
- **Use case**: Comparing scores of three students across subjects
- **Example**: Alice, Bob, and Charlie's scores in each subject
- **Advantage**: Easy to compare between groups

### 3. Stacked Bar Chart
Shows composition by stacking bars on top of each other.
- **Use case**: Showing total contribution of each student
- **Example**: Total class score broken down by student
- **Advantage**: Shows both individual parts and total

### 4. Percentage Stacked Bar Chart
Displays proportions as percentages (totals = 100%).
- **Use case**: Showing relative contribution when totals vary
- **Example**: Each student's proportion of total score
- **Advantage**: Easy to compare proportions

### 5. Horizontal Bar Charts
All types can be displayed horizontally for better label readability.
- **Use case**: When category names are long
- **Example**: Any of the above, rotated 90 degrees

---

## 🎯 Learning Outcomes

By completing this lab, you will:
- ✅ Understand what datasets and DataFrames are
- ✅ Know different tabular data formats
- ✅ Create simple bar charts using Matplotlib
- ✅ Customize chart colors, labels, and titles
- ✅ Use Seaborn for quick visualizations
- ✅ **Create grouped bar charts for comparing multiple groups**
- ✅ **Create stacked bar charts to show composition**
- ✅ **Create percentage stacked charts for proportions**
- ✅ Understand the difference between Matplotlib and Seaborn

---

##  Files in This Lab

1. **pychart_tutorial.ipynb** - Interactive Jupyter notebook with step-by-step tutorial
2. **README.md** - This file, containing conceptual explanations

---

## Getting Started

1. Open `pychart_tutorial.ipynb` in Jupyter Notebook or VS Code
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run each cell sequentially and observe the outputs
4. Experiment with the code by changing values and colors

---

## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Python Data Visualization Guide](https://realpython.com/python-data-visualization/)

---

## END - THANK YOU 




