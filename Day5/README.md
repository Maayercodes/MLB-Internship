# Day 5 - Classification and Model Evaluation

## 1. What is Classification?

Classification is a supervised Machine Learning technique used to predict categories or classes based on input data.

For example:
- Predicting whether an email is Spam or Not Spam.
- Predicting whether a tumor is Malignant or Benign.
- Predicting the species of an Iris flower.

In Day 5, we practiced classification using Logistic Regression and Decision Tree models.

## 2. Difference Between Regression and Classification

| Regression | Classification |
|---|---|
| Predicts continuous numerical values. | Predicts categories or classes. |
| Example: House price prediction. | Example: Spam email detection. |
| Output is a numerical value. | Output is a class label. |
| Example: Linear Regression. | Example: Logistic Regression. |

## 3. Evaluation Metrics Used

We learned and practiced the following evaluation metrics:

- **Accuracy:** Measures the overall percentage of correct predictions.
- **Precision:** Measures how many positive predictions were actually correct.
- **Recall:** Measures how many actual positive cases were correctly identified.
- **F1-Score:** The harmonic mean of Precision and Recall.
- **Confusion Matrix:** Shows correct and incorrect predictions by comparing actual and predicted classes.

We also used the Classification Report to view Precision, Recall, F1-Score, and Support for each class.

## 4. Practice Tasks Completed

### Practice 1: Model Evaluation

- Trained a Logistic Regression classification model.
- Used the Breast Cancer Wisconsin dataset from Scikit-learn.
- Calculated Accuracy, Precision, Recall, and F1-Score.
- Generated a Confusion Matrix.
- Understood the purpose of each evaluation metric.

### Practice 2: Wine Classification

- Loaded the Wine dataset using Scikit-learn.
- Explored dataset features and target classes.
- Split the dataset into training and testing sets.
- Applied StandardScaler for feature scaling.
- Trained a Logistic Regression model.
- Made predictions and evaluated model performance.
- Generated a Confusion Matrix and Classification Report.

## 5. Mini Project: Iris Flower Classification System

Developed an Iris Flower Classification System using Machine Learning.

**Dataset:** Iris Dataset from Scikit-learn.

**Models Used:**
- Logistic Regression
- Decision Tree Classifier (Bonus)

**Tasks Completed:**
- Loaded and explored the Iris dataset.
- Checked missing values and class distribution.
- Split the dataset into training and testing sets.
- Applied feature scaling for Logistic Regression.
- Trained Logistic Regression and Decision Tree models.
- Predicted Iris flower species.
- Evaluated both models using Accuracy, Precision, Recall, and F1-Score.
- Generated Confusion Matrices.
- Displayed sample predictions with actual flower species.
- Compared the performance of both models.

## 6. Model Performance and Observations

Three classification datasets were used during Day 5:

- Breast Cancer Wisconsin Dataset
- Wine Dataset
- Iris Dataset

Logistic Regression was used in all three exercises. Decision Tree was additionally used in the Iris Mini Project.

Performance was evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. The Iris Mini Project also included a comparison between Logistic Regression and Decision Tree.

The actual model scores are available in the respective Jupyter Notebooks.

## Conclusion

Day 5 helped me understand Classification, the difference between Regression and Classification, and how to evaluate Machine Learning models.

I practiced classification using three Scikit-learn datasets and trained Logistic Regression and Decision Tree models.

**Day 5: Completed**
