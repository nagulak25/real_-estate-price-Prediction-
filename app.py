
import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(page_title="Real Estate Price Predictor", layout="centered")

# Title
st.title("Real Estate Price Prediction")
st.write("Enter property details to predict price")

# Load model safely
model_path = "real_estate_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found! Please make sure it is in the same folder.")
else:
    model = joblib.load(model_path)

    # Input fields
    area = st.number_input("Area (sqft)", min_value=100.0, step=50.0)
    bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
    age = st.number_input("Property Age (years)", min_value=0, step=1)

    location = st.text_input("Location")
    property_type = st.selectbox("Property Type", ["Apartment", "Villa", "House"])

    # Predict button
    if st.button("Predict Price"):
        input_data = pd.DataFrame([{
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age": age,
            "location": location,
            "property_type": property_type
        }])

        try:
            prediction = model.predict(input_data)[0]

            # Confidence range (±10%)
            lower = prediction * 0.9
            upper = prediction * 1.1

            st.success(f"Estimated Price: Rs {prediction:,.2f}")
            st.info(f"Price Range: Rs {lower:,.2f} - Rs {upper:,.2f}")

        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")
