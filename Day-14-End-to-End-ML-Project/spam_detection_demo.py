
import joblib

# Load the trained email spam detection model
saved_data = joblib.load("spam_detection_model.pkl")
model = saved_data["model"]
vectorizer = saved_data["vectorizer"]

print("=" * 55)
print("       EMAIL SPAM DETECTION SYSTEM")
print("=" * 55)
print("Enter an email subject or email text to check for spam.")
print("Type 'exit' to close the application.\n")

while True:
    email_text = input("Enter email text: ").strip()

    if email_text.lower() == "exit":
        print("Thank you for using the Email Spam Detection System!")
        break

    if not email_text:
        print("Please enter some email text.\n")
        continue

    # Convert email text into TF-IDF features
    email_tfidf = vectorizer.transform([email_text])

    # Predict whether the email is spam
    prediction = model.predict(email_tfidf)[0]

    if prediction == "spam":
        print("Result: SPAM EMAIL")
    else:
        print("Result: NOT SPAM (HAM)")

    print("-" * 55)
