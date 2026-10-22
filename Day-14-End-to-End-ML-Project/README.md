# Email Spam Detection – End-to-End Machine Learning Project

## Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to classify emails as **Spam** or **Ham (Not Spam)**. It uses the Enron email spam dataset and a Multinomial Naive Bayes classifier.

## Objectives

- Load and preprocess email data.
- Combine email subjects and message bodies.
- Convert email text into numerical features using TF-IDF.
- Train and evaluate a machine learning model.
- Predict whether new email text is spam or not spam.
- Save the trained model for reuse.

## Dataset

**Dataset:** Enron Email Spam Dataset  
**File:** `data/enron_spam_data.csv`

The dataset includes email subjects, message bodies, and labels indicating spam or ham.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Joblib

## Project Workflow

1. Load the email dataset.
2. Clean missing values, empty messages, and duplicate records.
3. Visualize the distribution of spam and ham emails.
4. Split the data into training and testing sets.
5. Convert text into numerical features using TF-IDF.
6. Train the Multinomial Naive Bayes model.
7. Evaluate performance using accuracy, precision, recall, F1-score, and a confusion matrix.
8. Save the trained model and prediction results.
9. Test the model using the interactive Python demo.

## Project Files

- `Spam_Detection_Project.ipynb` – Data preprocessing, training, and evaluation.
- `data/enron_spam_data.csv` – Email dataset.
- `spam_detection_model.pkl` – Saved model and TF-IDF vectorizer.
- `prediction_results.csv` – Actual and predicted labels.
- `spam_detection_demo.py` – Interactive email spam detection demo.
- `requirements.txt` – Required Python packages.
- `screenshots/` – Project output screenshots.

## Run the Project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the interactive demo from the project folder:

```bash
python spam_detection_demo.py
```

Enter an email subject or message to receive a spam prediction. Type `exit` to close the application.

## Model Evaluation

The model is evaluated using accuracy, precision, recall, F1-score, and a confusion matrix. Add the actual scores obtained by running the updated notebook.

## Conclusion

This project demonstrates an end-to-end text classification workflow, from email data preprocessing to model training, evaluation, saving, and prediction. It can serve as a starting point for building email spam filtering applications.
