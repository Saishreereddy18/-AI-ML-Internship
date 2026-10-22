# Day 14: End-to-End Machine Learning Project

## Project Title

**Spam Message Detection Using Machine Learning**

## 1. Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to classify text messages as Spam or Ham (Not Spam). The model learns patterns from labelled messages and predicts the category of new messages.

## 2. Objective

- Build a practical end-to-end Machine Learning project.
- Clean and explore the dataset.
- Convert text messages into numerical features.
- Train a classification model.
- Evaluate the model using appropriate metrics.
- Test new messages and save the trained model.

## 3. Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

## 4. Dataset

The project uses the SMS Spam Collection dataset from the UCI Machine Learning Repository.

Dataset source: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

The dataset contains text messages labelled as:

- **Ham:** A legitimate message.
- **Spam:** An unwanted or potentially fraudulent message.

## 5. Project Workflow

1. Load and inspect the dataset.
2. Handle missing values and remove duplicate messages.
3. Visualize the distribution of message categories.
4. Split the data into training and testing sets.
5. Convert message text into numerical features using TF-IDF.
6. Train a Multinomial Naive Bayes classifier.
7. Evaluate predictions using accuracy, precision, recall, F1-score, and a confusion matrix.
8. Test the model with new messages.
9. Save the trained model and evaluation results.

## 6. Machine Learning Algorithm

**Multinomial Naive Bayes** is a probabilistic classification algorithm commonly used for text classification. It learns patterns from labelled training examples and predicts whether a message is spam or ham.

TF-IDF is used to represent text as numerical features before training.

## 7. Model Evaluation

The model is evaluated on a separate test dataset.

- **Accuracy:** Measures the proportion of correct predictions.
- **Precision:** Measures how many messages predicted as spam are actually spam.
- **Recall:** Measures how many actual spam messages are detected.
- **F1-score:** Combines precision and recall.
- **Confusion matrix:** Shows correct and incorrect classifications.

**Actual evaluation results:** Add the accuracy, precision, recall, and F1-score from the completed notebook here.

## 8. Project Files

- `Spam_Detection_Project.ipynb` — complete project notebook.
- `spam_detection_model.pkl` — saved model and TF-IDF vectorizer.
- `prediction_results.csv` — actual and predicted test labels.
- `requirements.txt` — required Python libraries.
- `data/` — local dataset directory.
- `screenshots/` — project output screenshots.

## 9. How to Run the Project

1. Clone or download the repository.
2. Install the required dependencies using `python -m pip install -r requirements.txt`.
3. Download the SMS Spam Collection dataset from the official UCI source.
4. Place the extracted `SMSSpamCollection` file inside the `data/` directory.
5. Open `Spam_Detection_Project.ipynb` in VS Code or Jupyter Notebook.
6. Select the appropriate Python environment and run the notebook cells in order.

## 10. Conclusion

This project demonstrates an end-to-end Machine Learning workflow for text classification, including data cleaning, text vectorization, model training, evaluation, and prediction. It provides practical experience in applying NLP and Scikit-learn to a real-world classification problem.

## 11. Author

**Billa Sai Sree**

AI/ML Internship Project — Day 14
