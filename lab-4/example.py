import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
df = sns.load_dataset("iris")

# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()
