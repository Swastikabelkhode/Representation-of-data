import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a dummy dataset
np.random.seed(42) # for reproducibility
data_size = 100

x = np.random.rand(data_size) * 10 # Feature 1
y = 2 * x + np.random.randn(data_size) * 2 # Feature 2 with some noise
categories = np.random.choice(['A', 'B', 'C'], data_size) # Categorical feature

# Combine into a pandas DataFrame for structured data
df = pd.DataFrame({
    'Feature1': x,
    'Feature2': y,
    'Category': categories
})

print("--- Dummy Dataset Created ---")
print(df.head())

# 2. Representation 1: Raw Data (first few values)
print("\n--- Representation 1: Raw Data (first 10 values) ---")
print(x[:10])

# 3. Representation 2: Pandas DataFrame
print("\n--- Representation 2: Pandas DataFrame (info) ---")
df.info()
print("\n--- Representation 2: Pandas DataFrame (first 5 rows) ---")
print(df.head())

# 4. Representation 3: Descriptive Statistics
print("\n--- Representation 3: Descriptive Statistics ---")
print(df.describe())

# 5. Representation 4: Histogram
print("\n--- Representation 4: Histogram of Feature1 ---")
plt.figure(figsize=(8, 5))
sns.histplot(df['Feature1'], kde=True)
plt.title('Distribution of Feature1')
plt.xlabel('Feature1 Value')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 6. Representation 5: Scatter Plot
print("\n--- Representation 5: Scatter Plot of Feature1 vs Feature2 ---")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Feature1', y='Feature2', hue='Category', palette='viridis')
plt.title('Feature1 vs Feature2 by Category')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 7. Representation 6: Box Plot
print("\n--- Representation 6: Box Plot of Feature2 by Category ---")
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Category', y='Feature2', palette='pastel')
plt.title('Box Plot of Feature2 by Category')
plt.xlabel('Category')
plt.ylabel('Feature2')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 8. Representation 7: Line Plot (example showing sorted Feature1 data)
# For a line plot, data often implies an order or sequence.
# Let's sort Feature1 and plot it against its index to show a trend, or just a single feature over its index
print("\n--- Representation 7: Line Plot of sorted Feature1 ---")
df_sorted = df.sort_values(by='Feature1').reset_index(drop=True)
plt.figure(figsize=(10, 6))
plt.plot(df_sorted.index, df_sorted['Feature1'], marker='o', linestyle='-', markersize=4, color='skyblue')
plt.title('Line Plot of Sorted Feature1')
plt.xlabel('Index (sorted by Feature1)')
plt.ylabel('Feature1 Value')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
