
import joblib
import pandas as pd
import os

print("=" * 45)
print("   STUDENT MARKS PREDICTION SYSTEM")
print("       Machine Learning Demo")
print("=" * 45)

model_path = "linear_regression_model.pkl"

if not os.path.exists(model_path):
    print("Model file not found!")
    print("Please run ML_Practice.ipynb first.")
else:
    model = joblib.load(model_path)
    print("Model loaded successfully!")

    while True:
        try:
            user_input = input(
                "\nEnter study hours (or type 'exit' to stop): "
            )

            if user_input.lower() == "exit":
                print("Thank you for using the predictor!")
                break

            hours = float(user_input)

            if hours < 0:
                print("Please enter a non-negative number.")
                continue

            new_data = pd.DataFrame({
                "Study_Hours": [hours]
            })

            predicted_marks = model.predict(new_data)[0]

            print(f"Study Hours: {hours}")
            print(f"Predicted Marks: {predicted_marks:.2f}")

            if hours > 10.5:
                print(
                    "Note: This is outside the training data range, "
                    "so the prediction may be less reliable."
                )

        except ValueError:
            print("Invalid input! Enter a number, like 5 or 7.5.")
