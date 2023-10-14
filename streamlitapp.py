import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os






def age_column(x : pd.DataFrame):
    x['Car_Age'] = 2023 - x['Year']
    x.drop('Year',axis=1 , inplace=True)
    return x



Model = joblib.load('/app/project/rff.h5')









def main() :
    
    st.write('Welcome To Final Project')

    brand = st.selectbox('Choose Car Brand.' , ('Hyundai','Chevrolet' , 'Fiat') )

    if brand == 'Hyundai' :
       model = st.selectbox('Choose Car Model' , ('Accent', 'Avante' ,'I10', 'Elantra' ,'Excel', 'Matrix' ,'Tucson' ,'Verna'))

    elif brand == 'Chevrolet' :
       model = st.selectbox('Choose Car Model' ,('Cruze' ,'Aveo', 'Lanos' ,'Optra'))

    else:
       model = st.selectbox('Choose Car Model' ,('128' ,'131' ,'Punto' ,'Shahin', 'Tipo' ,'Uno'))


    body = st.selectbox('Choose Car Body.' , ('Sedan', 'Hatchback' ,'SUV'))

    color = st.selectbox('Choose Car Color' , ('Black' ,'Silver' ,'Gray' ,'Blue- Navy Blue' ,'Green' ,'Red', 'Gold',
    'Other Color', 'Burgundy' ,'White' ,'Yellow' ,'Brown', 'Orange' ,'Beige'))

    year = st.number_input('Enter Car Manufacturing Year.')

    fuel = st.selectbox('Choose Car Fuel Type.' , ('Benzine' ,'Natural Gas'))

    kilos = st.selectbox('Choose Car Kilometers' , ('0 to 9999' ,'10000 to 19999' ,'100000 to 119999', '120000 to 139999',
    '140000 to 159999' ,'160000 to 179999' ,'180000 to 199999' ,'20000 to 29999',
    '30000 to 39999', '40000 to 49999' ,'50000 to 59999' ,'60000 to 69999',
    '70000 to 79999' ,'80000 to 89999' ,'90000 to 99999', 'More than 200000') )

    engine = st.selectbox('Choose Car Engine.' , ('1000 - 1300 CC' , '1400 - 1500 CC' , '1600 CC'))

    transmission = st.selectbox('Choose Car Transmission Type.' , ('Manual', 'Automatic'))

    gov = st.selectbox('Choose Car Location.' , ('Giza' ,'Qena' ,'Cairo' ,'Minya' ,'Alexandria' ,'Dakahlia' ,'Suez' ,'Sharqia',
    'Kafr al-Sheikh', 'Beheira' ,'Ismailia' ,'Sohag' ,'Monufia' ,'Qalyubia',
    'Beni Suef', 'Asyut' ,'Fayoum','Gharbia' ,'Matruh' ,'Damietta', 'Red Sea',
    'Port Said' ,'Luxor' ,'South Sinai', 'New Valley' ,'Aswan'))
    
    
    prediction = 'Prediction is not made yet, Click Predict Car Price to make prediction.'
    
    input_data = [brand,model,body,color,year,fuel,kilos,engine,transmission,gov]
    input_df = pd.DataFrame([input_data] ,columns=[ 'Brand', 'Model', 'Body', 'Color', 'Year', 'Fuel',
       'Kilometers', 'Engine', 'Transmission', 'Gov'])


    if st.button('Predict Car Price.'):
        prediction = f'Car Price is {"{:,}".format(int(Model.predict(input_df)[0] * 1000))} EGP'
        
    st.success(prediction)
    
if __name__ == '__main__':
    main()
    
    
