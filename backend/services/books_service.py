import joblib
import pandas as pd

# Load the trained model and scaler
knn = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')

# Assuming label_encoder is defined and used during training
label_encoder = joblib.load('label_encoder.joblib')


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


def get_recommendations(age: int, gender: str):
    return recommend_book(age, gender)
