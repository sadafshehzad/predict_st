import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("# Predict sales: 👉")
st.write("### Determine the scenario:")

# Price of the product
price= st.slider('Price of the product? 💲', min_value=3,max_value=15,value=7,step=1)


# Advertisement budget:
ads= st.slider('What is the Advertisement Budget? 💲', min_value=35,max_value=65,value=50,step=2)


# promotions:
promo= st.slider('what is the promotional budget? 💲', min_value=35,max_value=65,value=45,step=2)


rows=[price,ads,promo]
columns=['dollar_price', 'advertisment','promotions']

mktg_scenario=pd.DataFrame(dict(zip(columns,rows)),index=[0])
st.table(mktg_scenario)

# Add Button
if st.button(label="Click The Predict:"):

    
     #Load The model:

     loaded_model=pickle.load(open('lm_model_prediction_class2.sav','rb'))

     # Make the predictions and get te prediction probabilities:
     pred=loaded_model.predict(mktg_scenario)[0]
 

     st.write(f"Predicted Unit Sales , 💲📊:{pred: .0f} units")