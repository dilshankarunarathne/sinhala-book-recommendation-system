import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import random
import joblib

# Load the dataset
data = pd.read_csv('dataset/chatgpt/data1.csv')  # Assuming CSV format from previous interactions

# Encode gender column
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])  # Male: 0, Female: 1

# Select features and target
X = data[['age', 'gender']]
y = data['isbn']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and fit the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)  # You can optimize the number of neighbors
knn.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Save the trained model and scaler
joblib.dump(knn, 'knn_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')

# Book recommendation function
def recommend_book(age, gender):
    # Encode gender input to match training data encoding
    gender_encoded = label_encoder.transform([gender])[0]
    # Prepare input for prediction
    input_data = pd.DataFrame([[age, gender_encoded]], columns=['age', 'gender'])
    input_scaled = scaler.transform(input_data)
    # Predict ISBN
    recommended_isbn = knn.predict(input_scaled)
    return recommended_isbn[0]

# Test recommendations
test_cases = [(25, 'Male'), (30, 'Female'), (45, 'Female'), (60, 'Male')]
for age, gender in test_cases:
    isbn_recommended = recommend_book(age, gender)
    print(f"Recommended ISBN for Age {age} and Gender {gender}: {isbn_recommended}")
