import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the dataset
data = pd.read_csv("D:\Projects\Bite\sinhala-book-recommendation-system\ml2\data.csv")  # Assuming CSV format from previous interactions

# Encode gender column
gender_encoder = LabelEncoder()
data['gender'] = gender_encoder.fit_transform(data['gender'])  # Male: 0, Female: 1

# Encode book name column
book_name_encoder = LabelEncoder()
data['book_name'] = book_name_encoder.fit_transform(data['book name'])

# Select features and target
X = data[['age', 'gender']]
y = data['book_name']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
knn.fit(X_scaled, y)

# Save the encoders, scaler, and model
joblib.dump(scaler, 'D:\\Projects\\Bite\\sinhala-book-recommendation-system\\backend\\bin\\knn\\scaler.joblib')
joblib.dump(gender_encoder, 'D:\\Projects\\Bite\\sinhala-book-recommendation-system\\backend\\bin\\knn\\gender_encoder.joblib')
joblib.dump(book_name_encoder, 'D:\\Projects\\Bite\\sinhala-book-recommendation-system\\backend\\bin\\knn\\book_name_encoder.joblib')
joblib.dump(knn, 'D:\\Projects\\Bite\\sinhala-book-recommendation-system\\backend\\bin\\knn\\knn_model.joblib')

print("Model retrained and saved successfully.")