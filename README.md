# Cars365 - Car Price Predictor

## Overview
Cars365 is a web-based application designed to predict the selling price of used cars. The platform uses machine learning regression models to provide accurate price estimates based on various car features. The frontend is built using Streamlit, offering a simple and interactive interface for users to input car details and receive price predictions.

## Features
- **Price Prediction**: Get an estimated selling price for a car based on its features.
- **User-Friendly Interface**: The frontend, built with Streamlit, allows users to easily input car details and view predictions.
- **Multiple Regression Models**: Various regression algorithms are used to predict prices, ensuring high accuracy.

## Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**:
  - Regression algorithms were used for price prediction, including:
    - Linear Regression
    - Ridge Regression
    - Lasso Regression
    - Decision Tree Regression
    - Random Forest Regression
- **Database**: CSV or any database used to store and manage the dataset (replace as per your project details)

## Machine Learning Model
- **Algorithms Explored**: The system evaluates several regression algorithms, including:
  - **Linear Regression**: A basic regression model to predict prices.
  - **Ridge Regression**: A linear model with L2 regularization.
  - **Lasso Regression**: A linear model with L1 regularization.
  - **Decision Tree Regression**: A non-linear model that splits data into nodes for prediction.
  - **Random Forest Regression**: An ensemble method combining multiple decision trees to improve accuracy.
- **Selected Model**: The final model used is chosen based on performance metrics like Mean Absolute Error (MAE) and R-squared value.

## Streamlit Application
- The application uses Streamlit for frontend deployment, offering an interactive and responsive user experience.
- **Interface**:
  - Users can input features such as the car’s make, model, year, mileage, and more.
  - The system processes the input and provides a predicted price.



