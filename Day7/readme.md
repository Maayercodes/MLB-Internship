# Day 7 – K-Means Clustering & PCA

## Overview

Day 7 focused on learning Unsupervised Machine Learning techniques, including K-Means Clustering and Principal Component Analysis (PCA).

The practical work was completed using the Iris Dataset available in Scikit-learn. Three notebooks were created to understand clustering, dimensionality reduction, and data visualization.

## Topics Covered

### 1. K-Means Clustering

- Understanding Unsupervised Learning.
- Understanding Clustering.
- Applying the K-Means algorithm.
- Selecting the number of clusters (K).
- Using the Elbow Method.
- Visualizing clusters using scatter plots.
- Exploring real-world applications of clustering.

### 2. Principal Component Analysis (PCA)

- Understanding Dimensionality Reduction.
- Applying PCA.
- Reducing high-dimensional data into two dimensions.
- Understanding Principal Components.
- Visualizing transformed data.
- Understanding Explained Variance.
- Comparing PCA visualization with clustering results.

## Project Structure

```text
Day7/
│
├── 01_KMeans_Clustering.ipynb
├── 02_PCA_Analysis.ipynb
├── README.md
│
└── Iris_Flower_Clustering/
    │
    ├── Iris_Flower_Clustering.ipynb
    │
    └── outputs/
        ├── original_iris_data.png
        ├── elbow_method.png
        ├── kmeans_clusters.png
        ├── pca_visualization.png
        └── species_vs_clusters.png
```

## Mini Project: Iris Flower Clustering & Visualization

### Objective

The objective was to apply K-Means Clustering and PCA to the Iris Dataset, identify groups of similar flowers, and visualize the results.

### Dataset

The Iris Dataset was loaded using Scikit-learn.

- Total Samples: 150
- Original Features: 4
- Flower Species: Setosa, Versicolor, Virginica
- Dataset Library: Scikit-learn

### Implementation Steps

1. Loaded the Iris Dataset using `load_iris()`.
2. Converted the dataset into a Pandas DataFrame.
3. Explored the dataset using `head()`, `info()`, and `describe()`.
4. Checked dataset dimensions and missing values.
5. Selected Sepal Length and Sepal Width for original data visualization.
6. Applied StandardScaler to standardize the four numerical features.
7. Used the Elbow Method to examine different values of K.
8. Applied K-Means Clustering with 3 clusters.
9. Visualized the resulting clusters.
10. Applied PCA to reduce four features into two principal components.
11. Visualized the PCA-transformed dataset.
12. Compared actual flower species with K-Means clusters.
13. Saved all generated visualizations as PNG files.

## Key Concepts Explained

### What is Clustering?

Clustering is an Unsupervised Machine Learning technique that groups similar data points together.

It identifies patterns and similarities in data without requiring predefined labels during training.

In this project, K-Means grouped the Iris flower samples into three clusters based on their features.

### What is PCA?

Principal Component Analysis (PCA) is a dimensionality reduction technique.

It transforms a dataset with multiple features into fewer dimensions while preserving as much of the original data's variance as possible.

In this project, PCA reduced the Iris dataset from four features to two principal components, making it easier to visualize the data in a 2D scatter plot.

### How did you determine the best value of K?

The Elbow Method was used to examine the optimal number of clusters.

Different K values from 1 to 10 were tested. The inertia values were calculated and plotted against the number of clusters.

The graph was examined to identify the elbow point, where adding more clusters started producing smaller improvements.

Based on the Iris dataset and the Elbow Method, K = 3 was selected.

### What insights did you gain from the visualizations?

- The original data visualization showed how Iris flower samples were distributed based on Sepal Length and Sepal Width.
- The Elbow Method helped examine the suitable number of clusters.
- K-Means grouped the 150 samples into three clusters.
- PCA made it possible to visualize four original features in two dimensions.
- The PCA visualization showed that the first two principal components preserved approximately 95.81% of the total variance.
- Comparing actual species with predicted clusters showed that K-Means could identify meaningful groups, although the clusters did not perfectly match the actual flower species.

## Results

### K-Means Clustering

Number of Clusters: **3**

| Cluster | Number of Samples |
|---|---:|
| Cluster 0 | 53 |
| Cluster 1 | 50 |
| Cluster 2 | 47 |
| **Total** | **150** |

### PCA Results

| Description | Result |
|---|---:|
| Original Features | 4 |
| Reduced Features | 2 |
| Explained Variance | 95.81% |

PCA successfully reduced the dimensionality of the dataset while preserving approximately 95.81% of its variance.

## Generated Visualizations

All project graphs were saved as PNG files in the `outputs` folder.

### 1. Original Iris Data

![Original Iris Data](outputs/original_iris_data.png)

### 2. Elbow Method

![Elbow Method](outputs/elbow_method.png)

### 3. K-Means Clustering

![K-Means Clusters](outputs/kmeans_clusters.png)

### 4. PCA Visualization

![PCA Visualization](outputs/pca_visualization.png)

### 5. Actual Species vs K-Means Clusters

![Species vs Clusters](outputs/species_vs_clusters.png)

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Conclusion

Day 7 provided practical experience with Unsupervised Machine Learning, K-Means Clustering, and PCA.

I learned how to group similar data points, determine a suitable number of clusters using the Elbow Method, reduce dataset dimensions using PCA, and visualize machine learning results.

The Iris Flower Clustering project successfully formed three clusters from 150 samples and reduced the original four features to two principal components while preserving approximately 95.81% of the variance.

**Day 7 Status: Completed**