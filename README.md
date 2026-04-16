# real_-estate-price-Prediction-
# Real Estate Price Prediction System

A production-ready machine learning application that predicts real estate prices based on property features such as area, location, and number of rooms.

## Features

* Accurate price prediction using ML models (XGBoost, Random Forest, Linear Regression)
* End-to-end pipeline with preprocessing and model integration
* Interactive web interface using Streamlit
* Real-time predictions with confidence range

## Tech Stack

* Python, Pandas, NumPy
* Scikit-learn, XGBoost
* Streamlit (UI)
* Joblib (model persistence)

## Setup

```bash
pip install pandas numpy scikit-learn xgboost streamlit joblib
streamlit run app.py
```

## Usage

1. Enter property details (area, bedrooms, location, etc.)
2. Click **Predict Price**
3. View estimated price and range instantly

## Project Structure

```
├── app.py
├── real_estate_model.pkl
├── notebook.ipynb
└── data/
```

## Output

* Predicted property price
* Confidence range for estimation

## Author

Keerthana
