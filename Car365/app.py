import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the model
model = pk.load(open('model.pkl', 'rb'))

# Define a function to load and preprocess the data
def load_data():
    car_df = pd.read_csv('Cardetails.csv')
    
    def get_brand_name(car_name):
        words = car_name.split(' ')
        brand_name = ' '.join(words[:3])
        return brand_name
    
    car_df['name'] = car_df['name'].apply(get_brand_name)
    
    return car_df

if 'page' not in st.session_state:
     st.session_state.page = 'Home'


# Navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Predict Price", "About","Contact Us"])



# Load the dataset
car_df = load_data()

# Fit LabelEncoder on the 'name' column
label_encoder = LabelEncoder()
label_encoder.fit(car_df['name'])

if page == "Home":
    st.markdown("""
        <h1 style='text-align: center; font-size: 50px; color: #666;'>Cars365</h1>
        <h2 style='text-align: center; font-size: 30px; color: #666;'>"Connecting Buyers & Sellers"</h2>
        """, unsafe_allow_html=True)
    st.write("Welcome to Cars365! Use the navigation bar to switch between pages or click on the buttons here")
    st.image('image.jpeg', use_column_width=True)
  



elif page == "Predict Price":
    st.markdown("""
        <h1 style='text-align: center; font-size: 50px; color: #666;'>Predict Car Price</h1>
        """, unsafe_allow_html=True)
    
    name = st.selectbox('Select Car Model', car_df['name'].unique())
    year = st.slider('Car Manufactured Year', 1994, 2024)
    km_driven = st.slider('No of kms Driven', 1, 3000000)
    fuel = st.selectbox('Fuel type', car_df['fuel'].unique())
    seller_type = st.selectbox('Seller type', car_df['seller_type'].unique())
    transmission = st.selectbox('Transmission type', car_df['transmission'].unique())
    owner = st.selectbox('Seller type', car_df['owner'].unique())
    mileage = st.slider('Car Mileage', 0, 50)
    engine = st.slider('Engine CC', 600, 5000)
    max_power = st.slider('Max Power', 0, 400)
    seats = st.slider('No of Seats', 5, 10)
    
    if st.button("Predict"):
        name_encoded = label_encoder.transform([name])[0]
        input_data_model = pd.DataFrame(
            [[name_encoded, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
            columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
        )
        
        input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
        input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
        input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
        input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
        
        car_price = model.predict(input_data_model)
        car_price_rounded = round(car_price[0])
        
        st.markdown(f"""
            <div style="border: 2px solid #666; padding: 20px; text-align: center;">
                <h2 style="font-size: 50px; color: #666;">Predicted Price: {car_price_rounded}</h2>
            </div>
            """, unsafe_allow_html=True)

elif page == "About":
    st.markdown("""
        <h1 style='text-align: center; font-size: 50px; color: #666;'>About</h1>
        """, unsafe_allow_html=True)
    st.write("""
        Welcome to Cars375, your trusted platform for buying and selling cars. At Cars375, we are committed to providing a seamless and transparent experience for both car buyers and sellers.

        ### Our Mission
        Our mission is to connect car buyers and sellers in a way that is both efficient and enjoyable. We strive to offer the best deals and the most reliable information, ensuring that our users can make informed decisions with confidence.

        ### Why Choose Us?
        - **Wide Selection:** We offer a wide range of cars from different brands and models to suit every need and budget.
        - **Trusted Sellers:** We partner with reputable sellers to ensure that all cars listed on our platform are of high quality.
        - **User-Friendly Interface:** Our platform is designed to be easy to navigate, making it simple for users to find the car they are looking for.
        - **Advanced Pricing Tools:** Use our advanced pricing tools to estimate the value of your car and get the best possible price.
        - **Customer Support:** Our dedicated customer support team is always here to help you with any questions or concerns.

        ### Our Services
        - **Car Listings:** Browse through thousands of car listings to find the perfect car for you.
        - **Price Estimator:** Use our price estimator tool to get an accurate estimate of your car's value.
        - **Sell Your Car:** List your car on our platform and reach thousands of potential buyers.
        - **Financing Options:** Explore various financing options to make your car purchase more affordable.

        ### Contact Us
        Have any questions or need assistance? Visit our Contact Us page for more information on how to get in touch with us.

        Thank you for choosing Cars375. We look forward to helping you find your next car!
    """)


elif page == "Contact Us" or st.session_state.page == 'Contact Us':
    st.session_state.page = 'Contact Us'
    st.markdown("""
        <h1 style='text-align: center; font-size: 50px; color: #666;'>Contact Us</h1>
        """, unsafe_allow_html=True)
    
    st.write("""
        **Company Name:** Cars365  
        **Email:** contact@cars365.com  
        **Phone Number:** +1234567890  
        **Telephone Number:** 012-3456789  
        **Instagram ID:** @cars365  
    """)
    
    comments = st.text_area("Comments")
    
    if st.button("Submit"):
        st.write("Thank you for your comments!")
