# Interactive Heatmap and Correlation Matrix Visualization
Dr. Amr Amin  
Ahmed Alqassas   
Autumn 2025-2026  

## Introduction to Heatmaps and Correlation Matrices

Heatmaps are powerful visualizations that use color to represent data values in a matrix format. They are particularly useful for displaying correlation matrices, which show the relationships between numerical variables. A correlation matrix quantifies how variables change together, with values ranging from -1 (perfect negative correlation) to +1 (perfect positive correlation). Values near 0 indicate little to no linear relationship.

**Key Concepts:**
- **Correlation**: Measures the strength and direction of the linear relationship between two variables.
- **Heatmap**: A grid where each cell's color intensity represents the correlation value.
- **Interactivity**: Modern heatmaps allow hovering to see exact values, zooming, and filtering.

This project demonstrates creating an interactive heatmap of a correlation matrix using the Tips dataset from Seaborn.

## Understanding Correlation Matrices and Heatmaps

### What is a Correlation Matrix?
A correlation matrix is a table showing correlation coefficients between variables. For a dataset with n numerical variables, it's an n x n symmetric matrix where:
- Diagonal elements are always 1 (a variable correlates perfectly with itself).
- Off-diagonal elements range from -1 to 1.

### How Heatmaps Visualize Correlations
- **Color Scale**: Typically uses a diverging color scheme (e.g., blue for negative, red for positive correlations).
- **Annotations**: Numbers in cells show exact correlation values.
- **Symmetry**: The matrix is symmetric, so the heatmap mirrors across the diagonal.

### Interpreting Correlations
- **+1**: Perfect positive correlation (as one variable increases, the other increases proportionally).
- **-1**: Perfect negative correlation (as one variable increases, the other decreases proportionally).
- **0**: No linear correlation.
- **Strength**: Absolute values > 0.7 indicate strong correlations; 0.3-0.7 moderate; < 0.3 weak.

### Components of a Correlation Heatmap
- **Grid Cells**: Each intersection of variables shows their correlation.
- **Color Intensity**: Darker colors indicate stronger correlations.
- **Axis Labels**: Variable names along rows and columns.
- **Color Bar**: Legend showing the correlation scale.

### How Heatmaps Help Understand Data
- **Identify Relationships**: Quickly spot which variables are related.
- **Multivariate Analysis**: Understand complex interactions between multiple variables.
- **Feature Selection**: Guide decisions about which variables to include in models.
- **Data Quality Check**: Detect multicollinearity (highly correlated variables) that might affect analysis.

In this project, the heatmap reveals relationships in the Tips dataset, such as how total bill amount correlates with tip size.

## Project Overview

This notebook (`interactive_heatmap.ipynb`) loads the Tips dataset and creates an interactive heatmap visualization of the correlation matrix for numerical columns (total_bill, tip, size).

## How to Run

1. Ensure Python is installed.
2. Install dependencies: Run `pip install -r requirements.txt`.
3. Open `interactive_heatmap.ipynb` in Jupyter Notebook or VS Code.
4. Run all cells in order.
5. The Dash app will start at http://127.0.0.1:8050/. Open in a browser to interact with the heatmap.

## Requirements

- pandas
- seaborn
- plotly
- dash

For more details, see the notebook's code explanations.