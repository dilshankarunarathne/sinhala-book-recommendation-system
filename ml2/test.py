import joblib
import pandas as pd

# Load the trained model and scaler
knn = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')
gender_encoder = joblib.load('gender_encoder.joblib')
book_name_encoder = joblib.load('book_name_encoder.joblib')

# Load the dataset for reference
data = pd.read_csv("D:\Projects\Bite\sinhala-book-recommendation-system\ml2\data.csv")

# Book recommendation function
def recommend_book(age, gender):
    # Encode inputs to match training data encoding
    gender_encoded = gender_encoder.transform([gender])[0]
    # Prepare input for KNN
    input_data = pd.DataFrame([[age, gender_encoded]], columns=['age', 'gender'])
    input_scaled = scaler.transform(input_data)
    # Predict the book name
    book_name_encoded = knn.predict(input_scaled)
    book_name = book_name_encoder.inverse_transform(book_name_encoded)
    # Get the recommended book details
    recommended_book = data[data['book name'] == book_name[0]].copy()
    return recommended_book

# Test recommendations
test_cases = [(25, 'Male'), (30, 'Female'), (45, 'Female'), (60, 'Male')]
for age, gender in test_cases:
    recommendations = recommend_book(age, gender)
    print(f"Recommendations for Age {age}, Gender {gender}:")
    if 'isbn' in recommendations.columns and 'book name' in recommendations.columns:
        print(recommendations[['isbn', 'book name']])
    else:
        print("Required columns are not present in the dataset.")