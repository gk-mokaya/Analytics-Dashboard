# importing required libs
import streamlit as st 
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import plotly.express as px 
import seaborn as sns 
import altair as alt 
from matplotlib import pyplot as plt 
from streamlit_extras.dataframe_explorer import dataframe_explorer
from sklearn import datasets
from streamlit_extras.metric_cards import style_metric_cards


# pnumeric_Branch configuration
st.set_page_config(page_title="Descriptive analytics", page_icon= "📈", layout="wide")

st.markdown(""" <h3 style="color:#2200ff; font-size:60px"> REALTIME INCOME PREDICTION MODEL </h3>""", unsafe_allow_html=True)

# sidebar
#logo
st.sidebar.image("static/logod.png")


st.write("""
# Income Prediction
""")
st.write('---')


# Loading the  Dataset

kskdf = pd.read_csv("dataksk.csv")

#Dropping null values
kskdf.dropna(inplace=True)

kskdf.info()

#Branchulation and Gender are not numerical variables, lets convert them to numerical ones in order to 
#apply Multiple Linear Regression using them


Branch_dict = {"A": 0, "B": 1, "C":2}
kskdf["numeric_Branch"]=kskdf["Branch"].map(Branch_dict)

City_dict = {"Yangon": 0, "Naypyitaw": 1, "Mandalay":2}
kskdf["numeric_City"]=kskdf["City"].map(City_dict)

Customer_dict = {"Normal": 0, "Member": 1}
kskdf["numeric_Customer"]=kskdf["Customer type"].map(Customer_dict)

Gender_dict = {"Male": 0, "Female":1}
kskdf["numeric_Gender"]=kskdf["Gender"].map(Gender_dict)

Productline_dict = {"Electronic accessories": 0, "Fashion accessories": 1, "Food and bevernumeric_Branchs": 2, "Health and beauty": 3, "Home and lifestyle": 4, "Sports and travel":5}
kskdf["numeric_Productline"]=kskdf["Product line"].map(Productline_dict)

Payment_dict = {"Cash": 0, "Credit card":1, "Ewallet":2}
kskdf["numeric_Payment"]=kskdf["Payment"].map(Payment_dict)

# Outputing updated dataframe
st.subheader("Updated categorical data transformed into numerical format")
with st.expander("Expand to apply filters on dataframe"):
    filtered_df = dataframe_explorer(kskdf, case=False)
    st.dataframe(filtered_df, use_container_width=True)



X = kskdf[['numeric_Branch', 'numeric_City', 'numeric_Customer','numeric_Gender', 'numeric_Productline', 'numeric_Payment', 'Unitprice', 'Quantity', 'Total', 
        'cogs','Rating']]
Y = kskdf['gross income']


# st.write(X)

 #Sidebar
 #Header of Specify Input Parameters
st.write('---')
st.subheader('Specify Your Input Parameters')
st.write('---')

# #BUG -> added float

def user_input_features():
      
      col1,col2,col3 = st.columns(3)

      with col1:    
        Branch = st.radio('Preferred Branch', ["A","B","C"])
        numeric_Branch = Branch_dict[Branch]

        City = st.radio('Choose City', ["Yangon","Naypyitaw","Mandalay"])
        numeric_City = City_dict[City]

        Customer_type = st.radio('Select Customer Type', ["Normal","Member"])
        numeric_Customer = Customer_dict[Customer_type]

        Gender = st.radio('Select Preferred Gender', ["Male","Female"])
        numeric_Gender = Gender_dict[Gender]


      with col2:
        Productline = st.radio('Choose your Productline', ["Electronic accessories","Fashion accessories","Food and beverages","Health and beauty","Home and lifestyle","Sports and travel"])
        numeric_Productline = Productline_dict[Productline]

        Payment = st.radio('numeric_Payment', ["Cash","Credit card","Ewallet"])
        numeric_Payment = Payment_dict[Payment]

      with col3:
        Unitprice = st.slider('Unit_price', float(X.Unitprice.min()), float(X.Unitprice.max()), float(X.Unitprice.mean()))
        Quantity = st.slider('Quantity', float(X.Quantity.min()), float(X.Quantity.max()), float(X.Quantity.mean()))
        Total = st.slider('Total', float(X.Total.min()), float(X.Total.max()), float(X.Total.mean()))
        cogs = st.slider('cogs', float(X.cogs.min()), float(X.cogs.max()), float(X.cogs.mean()))
        Rating = st.slider('Rating', float(X.Rating.min()), float(X.Rating.max()), float(X.Rating.mean()))

      data = {'numeric_Branch': numeric_Branch,
             'numeric_City': numeric_City,
             'numeric_Customer': numeric_Customer,
             'numeric_Gender': numeric_Gender,
             'numeric_Productline': numeric_Productline,
             'numeric_Payment': numeric_Payment,
             'Unitprice': Unitprice,
             'Quantity': Quantity,
             'Total': Total,
             'cogs': cogs,
             'Rating': Rating}
      
      features = pd.DataFrame(data, index=[0])

      
      return features



df = user_input_features()

# # Main Panel

st.write('---')
# Print specified input parameters
st.header('Specified Input parameters for prediction')
st.write(df)
st.write('---')

# # Building Regression Model
model = RandomForestRegressor()
#model = LinearRegression()
model.fit(X, Y)
# # Apply Model to Make Prediction
prediction = model.predict(df)

st.write('---')

st.header('Predicted Gross Income based on Specified Parameters is;')

style_metric_cards(background_color="##000000",border_left_color="#22ff00",border_color="#0f00e8")

st.metric(label="Projected Income is:", value = f' KSH.{prediction}', delta="Projected Gross Income based on Input Parameters")

st.write('---')
