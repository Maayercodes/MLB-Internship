# Day 6 – Model Evaluation & Hyperparameter Tuning

## Overview

Day 6 focused on understanding Model Evaluation and Hyperparameter Tuning in Machine Learning. I learned how to evaluate classification models, identify their performance, and improve model settings using GridSearchCV.

I also completed a **Breast Cancer Prediction System** using the Breast Cancer Wisconsin Diagnostic Dataset available in Scikit-learn.

## Topics Learned

### 1. Model Evaluation

- Train vs Test Performance
- Underfitting and Overfitting
- Cross Validation
- Learning Curves
- Choosing the Right Evaluation Metrics
- Accuracy, Precision, Recall, and F1-Score
- Confusion Matrix

### 2. Hyperparameter Tuning

- Understanding Hyperparameters
- GridSearchCV
- RandomizedSearchCV
- Selecting the Best Model Parameters
- Comparing Baseline and Tuned Models

## Practical Tasks

### 1. Dataset Exploration

Used the Breast Cancer Wisconsin Dataset from Scikit-learn.

- Loaded the dataset.
- Converted it into a Pandas DataFrame.
- Explored the dataset using `head()`, `info()`, and `describe()`.
- Checked target class distribution.
- Identified Malignant and Benign classes.

### 2. Baseline Model

Built a Logistic Regression classification model.

- Split the dataset into training and testing sets.
- Applied StandardScaler for feature scaling.
- Trained the Logistic Regression model.
- Evaluated performance using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

### 3. Hyperparameter Tuning

Applied GridSearchCV to find the best Logistic Regression parameters.

Parameters tested:

- C: 0.01, 0.1, 1, 10, 100
- Solver: liblinear, lbfgs
- Cross Validation: 5 folds

**Best Parameters Found:**

- C: [Add actual best C value]
- Solver: [Add actual best solver]

## Model Performance Comparison

| Evaluation Metric | Baseline Model | Tuned Model |
|---|---:|---:|
| Accuracy | 0.982456 (98.25%) | 0.982456 (98.25%) |
| Precision | 0.976190 (97.62%) | 0.976190 (97.62%) |
| Recall | 0.976190 (97.62%) | 0.976190 (97.62%) |
| F1-Score | 0.976190 (97.62%) | 0.976190 (97.62%) |

## Key Observations

- Both models achieved the same accuracy of 98.25%.
- Precision, Recall, and F1-Score were also identical at 97.62%.
- GridSearchCV tested different hyperparameter combinations using 5-fold cross-validation.
- Hyperparameter tuning did not improve the final test performance in this experiment.
- The baseline model was already performing very well on the test dataset.
- This demonstrates that hyperparameter tuning does not always guarantee better results.

## Mini Project – Breast Cancer Prediction System

Built a complete classification pipeline using:

- Scikit-learn
- Pandas
- Logistic Regression
- StandardScaler
- Pipeline
- GridSearchCV
- Matplotlib

The project includes dataset loading, preprocessing, model training, hyperparameter tuning, model evaluation, baseline vs tuned model comparison, and confusion matrix visualization.

## Conclusion

Day 6 helped me understand how to evaluate Machine Learning models and improve their configurations through hyperparameter tuning. I gained practical experience building and comparing baseline and tuned classification models using Scikit-learn.

Both models achieved an accuracy of 98.25%, showing that the baseline model was already performing well and tuning did not produce additional improvement on the test dataset.

**Status:** Completed