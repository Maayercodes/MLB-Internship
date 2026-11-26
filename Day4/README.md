# Day 4 - Data Preprocessing & First Machine Learning Model

## Overview

Today I learned how to prepare datasets for Machine Learning and build my first Linear Regression model using Scikit-learn.

## 1. What I Learned About Data Preprocessing

- **Data Preprocessing:** Preparing raw data before using it in a Machine Learning model.
- **Features (X) and Target (y):** Understanding input and output variables.
- **Label Encoding:** Converting categorical text values into numerical values.
- **One-Hot Encoding:** Converting categorical columns into 0 and 1 values using `pd.get_dummies()`.
- **Feature Scaling:** Standardizing numerical features using `StandardScaler`.
- **Train-Test Split:** Dividing the dataset into training (80%) and testing (20%) sets.
- **Data Leakage:** Understanding why the scaler should only be fitted on training data.

## 2. Why Train-Test Splitting is Important

The dataset was divided into:

- **Training Data (80%):** Used to train the Machine Learning model.
- **Testing Data (20%):** Used to evaluate the model on unseen data.

Train-test splitting helps us understand how well a model performs on new data instead of only checking its training performance.

## 3. Machine Learning – Linear Regression

Built a Linear Regression model to predict students' `Average_Score`.

Steps performed:

- Loaded the dataset.
- Created the `Average_Score` column using Math, Reading, and Writing scores.
- Encoded categorical columns.
- Selected features (X) and target (y).
- Split the dataset into training and testing sets.
- Applied feature scaling.
- Trained the Linear Regression model.
- Made predictions on test data.
- Compared Actual vs Predicted scores.

## 4. Evaluation Metrics

Used the following metrics to evaluate the model:

- **Mean Absolute Error (MAE):** Measures the average prediction error.
- **Mean Squared Error (MSE):** Measures squared prediction errors.
- **R² Score:** Measures how well the model explains variations in the target values.

### Model Performance

| Metric | Result |
|---|---:|
| Training R² Score | 0.9937 |
| Testing R² Score | 0.9923 |
| MAE | 1.0668 |
| MSE | 1.6568 |

### Observations

1. The testing R² score of 0.9923 shows that the model explains approximately 99.23% of the variation in student average scores.
2. The MAE of 1.0668 means predictions differ from actual scores by approximately 1.07 points on average.
3. Training and testing R² scores are very close, showing consistent model performance.

## 5. Mini Project – Student Score Prediction System

Built a simple Machine Learning project that:

- Loads the student performance dataset.
- Preprocesses the data.
- Trains a Linear Regression model.
- Predicts student average scores.
- Displays evaluation metrics.
- Prints an Actual vs Predicted comparison table.
- Visualizes prediction results using a scatter plot.

### Generated Graph

`actual_vs_predicted.png`

The scatter plot compares actual student scores with predicted scores.

## 6. Folder Structure

```text
Day-4/
│
├── README.md
├── StudentsPerformance.csv
│
├── Practice_Scripts/
│   ├── data_preprocessing.py
│   └── linear_regression_model.py
│
└── Student_Score_Prediction_Project/
    ├── student_score_prediction.py
    └── actual_vs_predicted.png
```

## 7. Technologies & Libraries Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## 8. Learning Outcomes

- Learned how to preprocess datasets for Machine Learning.
- Understood Features and Target variables.
- Learned categorical encoding and feature scaling.
- Understood train-test splitting and data leakage.
- Built my first Linear Regression model.
- Learned how to make predictions and evaluate model performance.
- Created a scatter plot to visualize Actual vs Predicted scores.

**Day 4 Completed – Data Preprocessing & First Machine Learning Model.**