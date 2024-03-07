import streamlit as st
import pandas as pd
import datetime
import pickle

df = pd.read_csv("cars24-car-price.csv")
st.header("Car Price Prediction Application")

col1, col2 = st.columns(2)

with col1:
    f1 = st.selectbox(
        'Select the fuel type',
        ('Diesel', 'Petrol', 'CNG','LPG', 'Electric'))

with col2:
   engine = st.slider('Engine power', 500, 5000, step = 100 )

col1, col2 = st.columns(2)

with col1:
    t1 = st.selectbox('Select the transmission type',('Automatic', 'Manual'))

with col2 :
    seats = st.selectbox('Select the number of seats', [4,5,6,7,9,11])

col1, col2 = st.columns(2)

with col1:
    year = st.number_input('Type the Year')

with col2:
    s1 = st.selectbox('Select the seller type', ('Dealer', 'Individual', 'Trustmark Dealer' ))

col1, col2 = st.columns(2)

with col1:
    km_driven = st.number_input('Type the KM Driven')

with col2:
    mileage = st.number_input('Type the mileage')



encode_dict = {
    'fuel_type' : {'Diesel' : 1 , 'Petrol' : 2, 'CNG' : 3, 'LPG' : 4, 'Electric' : 5},
    'transmission_type' : {'Manual' : 1, 'Automatic' : 2},
    'seller_type' : {'Dealer' : 1, 'Individual' : 2, 'Trustmark Dealer' : 3 }

}

def model_pred(fuel_type, engine, transmission_type, seats, year, seller_type, km_driven, mileage ):
    input_features = [[year,	seller_type,km_driven,fuel_type,transmission_type,mileage,engine,46.3,seats ]]
    with open('car_pred', "rb") as file:
        reg_model = pickle.load(file)
    return reg_model.predict(input_features)


if st.button('Predict'):
    fuel_type = encode_dict["fuel_type"][f1]
    transmission_type = encode_dict["transmission_type"][t1]
    seller_type = encode_dict['seller_type'][s1]
    pred = model_pred(fuel_type, engine, transmission_type, seats, year, seller_type, km_driven, mileage)
    st.text("Predicted price of the car is - " + str(pred))