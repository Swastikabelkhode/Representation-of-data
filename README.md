# Data Representation and Visualization Using Python

## Overview

This project demonstrates how the same dataset can be represented and analyzed in multiple ways using Python's data science libraries: NumPy, Pandas, Matplotlib, and Seaborn.

A synthetic dataset is generated containing two numerical features and one categorical feature. The program then explores different methods of data representation, ranging from raw numerical arrays to statistical summaries and visualizations.

## Features

### 1. Dataset Creation

* Generates a reproducible dummy dataset using NumPy.
* Creates:

  * **Feature1**: Random numerical values between 0 and 10.
  * **Feature2**: Values linearly related to Feature1 with added noise.
  * **Category**: Random categorical labels (A, B, and C).
* Stores the dataset in a Pandas DataFrame for structured analysis.

### 2. Raw Data Representation

* Displays the first few values of the generated numerical data.
* Demonstrates how data appears in its basic array format.

### 3. DataFrame Representation

* Shows dataset structure using `DataFrame.info()`.
* Displays sample records using `DataFrame.head()`.
* Highlights the benefits of tabular data organization.

### 4. Descriptive Statistics

* Generates statistical summaries including:

  * Count
  * Mean
  * Standard Deviation
  * Minimum and Maximum Values
  * Quartiles

### 5. Histogram Visualization

* Visualizes the distribution of **Feature1**.
* Includes a Kernel Density Estimate (KDE) curve for smoother distribution analysis.

### 6. Scatter Plot Visualization

* Displays the relationship between **Feature1** and **Feature2**.
* Uses color coding to distinguish different categories.
* Helps identify trends, clusters, and correlations.

### 7. Box Plot Visualization

* Compares the distribution of **Feature2** across categories.
* Highlights:

  * Median
  * Quartiles
  * Outliers
  * Data spread

### 8. Line Plot Visualization

* Sorts data based on **Feature1**.
* Displays trends and progression of values through a line graph.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

## Learning Objectives

This project is useful for beginners learning:

* Data generation and manipulation
* Exploratory Data Analysis (EDA)
* Statistical data summaries
* Data visualization techniques
* Understanding different forms of data representation

## Output

The program produces:

* Console-based statistical and tabular outputs.
* Multiple graphical visualizations including:

  * Histogram
  * Scatter Plot
  * Box Plot
  * Line Plot

These representations help users understand how the same dataset can be viewed from different analytical perspectives.
