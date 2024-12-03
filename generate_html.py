import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the digits dataset
digits = datasets.load_digits()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train an SVM classifier
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm_clf.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Save test images with predictions
n_images = 5
image_filenames = []
for i in range(n_images):
    filename = f"digit_{i}.png"
    image_filenames.append(filename)
    plt.figure()
    plt.imshow(X_test[i].reshape(8, 8), cmap="gray")
    plt.title(f"Pred: {y_pred[i]}")
    plt.axis("off")
    plt.savefig(filename)
    plt.close()

# Generate the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digit Recognition</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }}
        .images {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }}
        img {{
            border: 1px solid #ddd;
            padding: 10px;
            width: 100px;
            height: 100px;
            margin: 10px;
        }}
    </style>
</head>
<body>
    <h1>Digit Recognition</h1>
    <p>Model Accuracy: <strong>{accuracy * 100:.2f}%</strong></p>
    <div class="images">
        {"".join([f'<img src="{filename}" alt="Digit Prediction">' for filename in image_filenames])}
    </div>
</body>
</html>
"""

# Save the HTML file
with open("digit_recognition.html", "w") as file:
    file.write(html_content)

print("HTML file 'digit_recognition.html' and associated images have been created. Open the HTML file in a browser to view the results.")
