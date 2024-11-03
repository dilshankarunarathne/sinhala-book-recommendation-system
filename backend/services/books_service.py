import joblib
import pandas as pd

# Load the trained model and scaler
knn = joblib.load('bin\\knn\\knn_model.joblib')
scaler = joblib.load('bin\\knn\\scaler.joblib')
gender_encoder = joblib.load('bin\\knn\\gender_encoder.joblib')
book_name_encoder = joblib.load('bin\\knn\\book_name_encoder.joblib')


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
    return book_name


def get_recommendations(age: int, gender: str):
    return recommend_book(age, gender)
